# Generated by Django 4.2.6 on 2023-11-16 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdms_app', '0003_blog_category_blog_writer_alter_blog_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='writer',
            field=models.CharField(max_length=100),
        ),
    ]