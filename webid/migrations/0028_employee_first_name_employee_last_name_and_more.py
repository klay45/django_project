# Generated by Django 4.0.5 on 2022-09-02 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webid', '0027_alter_employee_options_alter_employee_disignation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='disignation',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='id',
            name='status',
            field=models.CharField(choices=[('For Edit', 'For Edit'), ('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', max_length=150),
        ),
    ]
