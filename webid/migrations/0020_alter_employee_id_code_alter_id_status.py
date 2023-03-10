# Generated by Django 4.0.5 on 2022-08-28 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webid', '0019_alter_employee_name_extension_alter_id_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id_code',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='id',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('For Edit', 'For Edit')], default='Pending', max_length=150),
        ),
    ]
