# Generated by Django 4.1 on 2022-08-23 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webid', '0002_employee_midle_iniatial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='midle_iniatial',
            new_name='midle_initial',
        ),
    ]
