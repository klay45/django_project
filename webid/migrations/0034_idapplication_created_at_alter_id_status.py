# Generated by Django 4.0.5 on 2022-09-05 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webid', '0033_forclaim_transaction_no_alter_id_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='idapplication',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='id',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('For Edit', 'For Edit')], default='Pending', max_length=150),
        ),
    ]