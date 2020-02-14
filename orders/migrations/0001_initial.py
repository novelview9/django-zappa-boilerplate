# Generated by Django 3.0.2 on 2020-01-28 05:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import hashid_field.field
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='생성')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='업데이트')),
                ('serial_id', hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7, primary_key=True, serialize=False)),
                ('barcode', models.CharField(blank=True, default='', max_length=255, verbose_name='바코드')),
                ('delivery_tracking_no', models.CharField(blank=True, default='', max_length=255, verbose_name='송장번호')),
                ('postal_code', models.CharField(max_length=255, verbose_name='우편번호')),
                ('address_head', models.CharField(max_length=255, verbose_name='주소')),
                ('address_body', models.CharField(max_length=255, verbose_name='주소상세')),
                ('applicant_name', models.CharField(max_length=255, verbose_name='신청인 성함')),
                ('contact1', models.CharField(max_length=255, verbose_name='연락처1')),
                ('contact2', models.CharField(max_length=255, verbose_name='연락처2')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalOrder',
            fields=[
                ('created', models.DateTimeField(blank=True, editable=False, verbose_name='생성')),
                ('updated', models.DateTimeField(blank=True, editable=False, verbose_name='업데이트')),
                ('serial_id', models.IntegerField(blank=True, db_index=True)),
                ('barcode', models.CharField(blank=True, default='', max_length=255, verbose_name='바코드')),
                ('delivery_tracking_no', models.CharField(blank=True, default='', max_length=255, verbose_name='송장번호')),
                ('postal_code', models.CharField(max_length=255, verbose_name='우편번호')),
                ('address_head', models.CharField(max_length=255, verbose_name='주소')),
                ('address_body', models.CharField(max_length=255, verbose_name='주소상세')),
                ('applicant_name', models.CharField(max_length=255, verbose_name='신청인 성함')),
                ('contact1', models.CharField(max_length=255, verbose_name='연락처1')),
                ('contact2', models.CharField(max_length=255, verbose_name='연락처2')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical order',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]