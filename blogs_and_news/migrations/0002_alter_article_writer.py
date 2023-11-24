# Generated by Django 4.2.6 on 2023-11-23 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_and_news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='writer',
            field=models.ForeignKey(limit_choices_to={'role': 'writer'}, on_delete=django.db.models.deletion.CASCADE, to='blogs_and_news.userprofile'),
        ),
    ]