# Generated by Django 3.2.23 on 2023-12-26 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vyaparapp', '0022_auto_20231222_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loanaccounts',
            name='balance_amount',
        ),
        migrations.AddField(
            model_name='additionalloan',
            name='cheque_number',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='additionalloan',
            name='loan_received',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='additionalloan',
            name='upi_id',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loanaccounts',
            name='account_name',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loanaccounts',
            name='cheque_number',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loanaccounts',
            name='cheque_number_for_fee',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loanaccounts',
            name='upi_id',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loanaccounts',
            name='upi_id_for_fee',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='makepayment',
            name='cheque_number',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='makepayment',
            name='upi_id',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
    ]