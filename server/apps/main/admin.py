from django.contrib import admin

from server.apps.main.models import Worker, TradePoint, Visit


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin[Worker]):
    """Admin panel for ``Worker`` model."""
    list_display = ('name', 'phone_number')
    search_fields = ('name', )


@admin.register(TradePoint)
class TradePointAdmin(admin.ModelAdmin[TradePoint]):
    """Admin panel for ``TradePoint`` model."""
    list_display = ('title', 'worker')
    search_fields = ('title', )


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin[Visit]):
    """Admin panel for ``Visit`` model."""
    list_display = ('trade_point', 'datetime', 'latitude', 'longitude')
    search_fields = ('trade_point__title', 'trade_point__worker__name')

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

