from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class Event(models.Model):
    DURATION_UNITS = [
        ('hours', 'Hours'),
        ('days', 'Days'),
    ]

    name = models.CharField(verbose_name="Name", max_length=250, unique=True)
    description = models.TextField(verbose_name="Description")
    event_date = models.DateField(verbose_name='Date')    
    event_duration_value = models.PositiveIntegerField(verbose_name="Duration Value")
    event_duration_unit = models.CharField(
        verbose_name="Duration Unit",
        max_length=11,
        choices=DURATION_UNITS,
        default='hours',
    )    
    venue = models.CharField(verbose_name="Venue", max_length=250)
    organizer = models.CharField(verbose_name="Organizer", max_length=250)
    banner = models.FileField(upload_to='events_banner/', null=True, blank=True)
    tickets = models.PositiveBigIntegerField(verbose_name="Tickets", editable=False, default=0)
    def total_tickets(self):
        return self.event_tickets.aggregate(total_quantity=models.Sum('quantity'))['total_quantity'] or 0
    


class EventTicket(models.Model):
    TICKET_TYPES = [
        ('vvip', 'VVIP'),
        ('vip', 'VIP'),
        ('regular', 'Regular'),
    ]
    PAYMENT_METHODS = [
        ('mpesa', 'Mpesa'),
        ('bank', 'Bank'),
        ('credit', 'Credit'),
        ('visa', 'Visa'),
    ]
    ticket_no = models.IntegerField(verbose_name="Ticket No", unique=True,  editable=False)
    ticket_type = models.CharField(verbose_name="Ticket Type", choices=TICKET_TYPES, max_length=50)
    quantity = models.IntegerField(verbose_name="Quantity", default=1)
    payment_method = models.CharField(verbose_name="Payment Method", choices=PAYMENT_METHODS, max_length=50)
    amount = models.PositiveBigIntegerField(verbose_name="Amount", editable=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_tickets')

    

    def save(self, *args, **kwargs):
        # Calculate amount based on ticket type and quantity
        ticket_prices = {
            'vvip': 1500,  # Custom price for VVIP ticket type
            'vip': 1000,   # Custom price for VIP ticket type
            'regular': 500  # Custom price for Regular ticket type
            # Add more ticket types and prices as needed
        }

        self.amount = ticket_prices.get(self.ticket_type, 0) * self.quantity

        if not self.ticket_no:
            # Generate a new ticket number
            last_ticket = EventTicket.objects.all().order_by('-id').first()
            last_number = int(last_ticket.ticket_no) if last_ticket else 0
            while True:
                last_number += 1
                new_number = f'{last_number:04d}'
                
                # Check if the new number is already in use
                if not EventTicket.objects.filter(ticket_no=new_number).exists():
                    self.ticket_no = int(new_number)
                    break

        super(EventTicket, self).save(*args, **kwargs)

@receiver(post_save, sender=EventTicket)
@receiver(post_delete, sender=EventTicket)
def update_event_tickets(sender, instance, **kwargs):
    # Update the total number of tickets in the associated Event
    event = instance.event
    event.tickets = event.total_tickets()
    event.save()