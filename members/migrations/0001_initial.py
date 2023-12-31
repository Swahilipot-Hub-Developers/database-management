# Generated by Django 4.2.6 on 2023-11-23 14:04

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.CharField(default='SPH-M0000', max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('year_of_birth', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2023)])),
                ('phone_number', models.CharField(max_length=15)),
                ('email_address', models.EmailField(max_length=254)),
                ('country', models.CharField(default='Kenya', max_length=50)),
                ('county', models.CharField(default='Mombasa', max_length=50)),
                ('sub_county', models.CharField(choices=[('Mvita', 'Mvita'), ('Jomvu', 'Jomvu'), ('Changamwe', 'Changamwe'), ('Kisauni', 'Kisauni'), ('Nyali', 'Nyali'), ('Likoni', 'Likoni')], max_length=50)),
            ],
        ),
    ]
