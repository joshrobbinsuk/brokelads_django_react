# Generated by Django 4.0.4 on 2022-11-22 13:39

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_id', models.IntegerField()),
                ('datetime', models.DateTimeField()),
                ('venue', models.CharField(max_length=255)),
                ('home_team', models.CharField(max_length=255)),
                ('home_team_logo', models.CharField(max_length=255)),
                ('away_team', models.CharField(max_length=255)),
                ('away_team_logo', models.CharField(max_length=255)),
                ('home_odds', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('away_odds', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('draw_odds', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('home_goals', models.IntegerField(null=True)),
                ('away_goals', models.IntegerField(null=True)),
                ('voided', models.BooleanField(default=False)),
                ('voided_message', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Matches',
                'ordering': ('datetime',),
            },
        ),
        migrations.CreateModel(
            name='TransactionRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('type', models.CharField(choices=[('BET', 'Bet'), ('PAYOUT', 'Payout')], max_length=6)),
                ('user_balance_before', models.DecimalField(decimal_places=2, max_digits=5)),
                ('user_balance_after', models.DecimalField(decimal_places=2, max_digits=5)),
                ('bet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='account.customeruser')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('choice', models.CharField(choices=[('HOME', 'Home'), ('AWAY', 'Away'), ('DRAW', 'Draw')], max_length=5)),
                ('stake', models.DecimalField(decimal_places=2, max_digits=5)),
                ('returns', models.DecimalField(decimal_places=2, max_digits=5)),
                ('outcome', models.CharField(choices=[('UNDECIDED', 'Undecided'), ('WON', 'Won'), ('LOST', 'Lost')], default='UNDECIDED', max_length=10)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookmaker.match')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='account.customeruser')),
            ],
            options={
                'ordering': ('match__datetime',),
            },
        ),
    ]
