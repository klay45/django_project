# Generated by Django 4.0.5 on 2022-08-25 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webid', '0005_alter_id_remarks_alter_id_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='id',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('For Edit', 'For Edit'), ('Completed', 'Completed')], default='Pending', max_length=150),
        ),
    ]