# Generated by Django 4.2.6 on 2023-11-20 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('category', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('attachment', models.FileField(blank=True, null=True, upload_to='feedback_attchments/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
