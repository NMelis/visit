from rest_framework import mixins
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import GenericViewSet

from server.apps.main.models import TradePoint, Visit
from server.apps.main.serializers import TradePointSerializer
from server.apps.main.serializers import VisitTradePointSerializer


class TradePointViewSet(mixins.ListModelMixin,
                        GenericViewSet):
    queryset = TradePoint.objects.all()
    serializer_class = TradePointSerializer

    def get_queryset(self):
        phone_number = self.request.GET.get('phone_number', None)
        if phone_number is None:
            raise ValidationError({'phone_number': 'query param is required'})
        return self.queryset.filter(worker__phone_number=phone_number).all()


class VisitViewSet(mixins.CreateModelMixin,
                   GenericViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitTradePointSerializer

