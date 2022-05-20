import textwrap
from typing import Final, final

from django.db import models

#: That's how constants should be defined.
STANDARD_CHAR_FIELD_MAX_LENGTH: Final = 255


@final
class Worker(models.Model):
    name = models.CharField(max_length=STANDARD_CHAR_FIELD_MAX_LENGTH)
    phone_number = models.CharField(max_length=STANDARD_CHAR_FIELD_MAX_LENGTH)

    class Meta(object):
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'

    def __str__(self) -> str:
        return textwrap.wrap(self.name, STANDARD_CHAR_FIELD_MAX_LENGTH // 4)[0]


@final
class TradePoint(models.Model):
    title = models.CharField(max_length=STANDARD_CHAR_FIELD_MAX_LENGTH)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    class Meta(object):
        verbose_name = 'Trade Point'
        verbose_name_plural = 'Trade Points'

    def __str__(self) -> str:
        return textwrap.wrap(self.title, STANDARD_CHAR_FIELD_MAX_LENGTH // 4)[0]


@final
class Visit(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    trade_point = models.ForeignKey(TradePoint, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta(object):
        verbose_name = 'Visit'
        verbose_name_plural = 'Visits'

    def __str__(self) -> str:
        return textwrap.wrap(f'{self.trade_point} {self.datetime}', STANDARD_CHAR_FIELD_MAX_LENGTH // 4)[0]
