# Generated by Django 4.0.4 on 2022-11-22 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookmaker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionrecord',
            name='bet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookmaker.bet'),
        ),
    ]
