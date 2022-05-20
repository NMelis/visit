from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from server.apps.main.models import TradePoint, Visit


class TradePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradePoint
        fields = ['pk', 'title']


class VisitTradePointSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visit
        fields = ['trade_point', 'latitude', 'longitude', 'id', 'datetime']
        extra_kwargs = {
            'trade_point': {'write_only': True},
            'latitude': {'write_only': True},
            'longitude': {'write_only': True}
        }

    def validate(self, attrs):
        phone_number = self.context['request'].GET.get('phone_number')
        if not TradePoint.objects.filter(worker__phone_number=phone_number, id=attrs['trade_point'].pk).exists():
            raise ValidationError({'phone_number': 'permission denied'})
        return attrs
