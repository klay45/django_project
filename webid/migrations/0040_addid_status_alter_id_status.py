# Generated by Django 4.0.5 on 2022-10-27 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webid', '0039_remove_addid_user_alter_id_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='addid',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('For Edit', 'For Edit'), ('Pending', 'Pending')], default='Pending', max_length=150),
        ),
        migrations.AlterField(
            model_name='id',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('For Edit', 'For Edit'), ('Pending', 'Pending')], default='Pending', max_length=150),
        ),
    ]
