from django.urls import path, include
from rest_framework import routers

from server.apps.main.views import TradePointViewSet
from server.apps.main.views import VisitViewSet

app_name = 'main'

router = routers.DefaultRouter()
router.register(r'trade_point', TradePointViewSet)
router.register(r'trade_point/visit', VisitViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
