# Generated by Django 4.0.5 on 2022-08-30 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webid', '0023_alter_forclaim_date_printed_alter_id_status_idcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='disignation',
            field=models.CharField(choices=[('Welder', 'Welder'), ('Field Engineer', 'Field Engineer'), ('Benifit Processor', 'Benifit Processor'), ('I.T. Staff', 'I.T. Staff')], max_length=250, null=True),
        ),
    ]
