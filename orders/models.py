from common.models import TimeStampedModel
from django.db import models
from hashid_field import HashidAutoField
from simple_history.models import HistoricalRecords


class Order(TimeStampedModel):
    serial_id = HashidAutoField(primary_key=True)
    barcode = models.CharField('바코드', max_length=255, blank=True, default='')
    delivery_tracking_no = models.CharField('송장번호', max_length=255, blank=True, default='')
    postal_code = models.CharField('우편번호', max_length=255)
    address_head = models.CharField('주소', max_length=255)
    address_body = models.CharField('주소상세', max_length=255)
    applicant_name = models.CharField('신청인 성함', max_length=255)
    contact1 = models.CharField('연락처1', max_length=255)
    contact2 = models.CharField('연락처2', max_length=255, blank=True, default='')

    history = HistoricalRecords()
