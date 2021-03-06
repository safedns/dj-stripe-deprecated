# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 03:28
from __future__ import unicode_literals

from django.db import migrations, models

import djstripe.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0010_event_idempotency_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_id', djstripe.fields.StripeIdField(max_length=255, unique=True)),
                ('livemode', djstripe.fields.StripeNullBooleanField(default=None, help_text='Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.')),
                ('stripe_timestamp', djstripe.fields.StripeDateTimeField(help_text='The datetime this object was created in stripe.', null=True)),
                ('metadata', djstripe.fields.StripeJSONField(blank=True, help_text='A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.', null=True)),
                ('description', djstripe.fields.StripeTextField(blank=True, help_text='A description of this object.', null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('amount', djstripe.fields.StripeCurrencyField(decimal_places=2, help_text='Amount to be transferred to your bank account or debit card.', max_digits=8)),
                ('arrival_date', djstripe.fields.StripeDateTimeField(help_text='Date the payout is expected to arrive in the bank. This factors in delays like weekends or bank holidays.')),
                ('currency', djstripe.fields.StripeCharField(help_text='Three-letter ISO currency code.', max_length=3)),
                ('failure_code', djstripe.fields.StripeCharField(blank=True, choices=[('account_closed', 'Bank account has been closed.'), ('account_frozen', 'Bank account has been frozen.'), ('bank_account_restricted', 'Bank account has restrictions on payouts allowed.'), ('bank_ownership_changed', 'Destination bank account has changed ownership.'), ('could_not_process', 'Bank could not process payout.'), ('debit_not_authorized', 'Debit transactions not approved on the bank account.'), ('insufficient_funds', 'Stripe account has insufficient funds.'), ('invalid_account_number', 'Invalid account number'), ('invalid_currency', 'Bank account does not support currency.'), ('no_account', 'Bank account could not be located.'), ('unsupported_card', 'Card no longer supported.')], help_text='Error code explaining reason for transfer failure if available. See https://stripe.com/docs/api/python#transfer_failures.', max_length=23, null=True)),
                ('failure_message', djstripe.fields.StripeTextField(blank=True, help_text='Message to user further explaining reason for payout failure if available.', null=True)),
                ('method', djstripe.fields.StripeCharField(choices=[('instant', 'Instant'), ('standard', 'Standard')], help_text='The method used to send this payout. `instant` is only supported for payouts to debit cards.', max_length=8)),
                ('statement_descriptor', djstripe.fields.StripeCharField(help_text='Extra information about a payout to be displayed on the user???s bank statement.', max_length=255, null=True, blank=True)),
                ('status', djstripe.fields.StripeCharField(choices=[('canceled', 'Canceled'), ('failed', 'Failed'), ('in_transit', 'In transit'), ('paid', 'Paid'), ('pending', 'Pending')], help_text='Current status of the payout. A payout will be `pending` until it is submitted to the bank, at which point it becomes `in_transit`. I t will then change to paid if the transaction goes through. If it does not go through successfully, its status will change to `failed` or `canceled`.', max_length=10)),
                ('type', djstripe.fields.StripeCharField(choices=[('bank_account', 'Bank account'), ('card', 'Card')], max_length=12)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='transfer',
            name='destination_type',
            field=djstripe.fields.StripeCharField(blank=True, choices=[('card', 'Card'), ('bank_account', 'Bank Account'), ('stripe_account', 'Stripe Account')], help_text='The type of the transfer destination.', max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='failure_code',
            field=djstripe.fields.StripeCharField(blank=True, choices=[('account_closed', 'Bank account has been closed.'), ('account_frozen', 'Bank account has been frozen.'), ('bank_account_restricted', 'Bank account has restrictions on payouts allowed.'), ('bank_ownership_changed', 'Destination bank account has changed ownership.'), ('could_not_process', 'Bank could not process payout.'), ('debit_not_authorized', 'Debit transactions not approved on the bank account.'), ('insufficient_funds', 'Stripe account has insufficient funds.'), ('invalid_account_number', 'Invalid account number'), ('invalid_currency', 'Bank account does not support currency.'), ('no_account', 'Bank account could not be located.'), ('unsupported_card', 'Card no longer supported.')], help_text='Error code explaining reason for transfer failure if available. See https://stripe.com/docs/api/python#transfer_failures.', max_length=23, null=True),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='failure_message',
            field=djstripe.fields.StripeTextField(blank=True, help_text='Message to user further explaining reason for transfer failure if available.', null=True),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='status',
            field=djstripe.fields.StripeCharField(blank=True, choices=[('canceled', 'Canceled'), ('failed', 'Failed'), ('in_transit', 'In transit'), ('paid', 'Paid'), ('pending', 'Pending')], help_text='The current status of the transfer. A transfer will be pending until it is submitted to the bank, at which point it becomes in_transit. It will then change to paid if the transaction goes through. If it does not go through successfully, its status will change to failed or canceled.', max_length=10, null=True),
        ),
    ]
