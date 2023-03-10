# Generated by Django 4.0.5 on 2022-08-28 03:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webid', '0013_employee_birth_date_employee_blood_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forclaim',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='id',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('For Edit', 'For Edit'), ('Pending', 'Pending')], default='Pending', max_length=150),
        ),
    ]
