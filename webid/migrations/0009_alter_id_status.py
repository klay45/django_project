# Generated by Django 4.0.5 on 2022-08-25 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webid', '0008_alter_id_status_forclaim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='id',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('For Edit', 'For Edit')], default='Pending', max_length=150),
        ),
    ]
