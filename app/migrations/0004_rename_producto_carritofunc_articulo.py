# Generated by Django 5.0.6 on 2024-07-05 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_carritofunc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carritofunc',
            old_name='producto',
            new_name='articulo',
        ),
    ]
