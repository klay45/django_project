# Generated by Django 4.0.5 on 2022-09-04 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webid', '0030_alter_id_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='id',
            name='date_printed',
            field=models.DateField(null=True),
        ),
    ]