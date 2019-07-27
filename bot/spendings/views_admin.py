from django.db.models import Sum
from django.contrib.admin.views.main import ChangeList as BaseChangeList


class SpendingsChangeList(BaseChangeList):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.total_spendings_by_currency = self.queryset \
            .values('currency') \
            .annotate(Sum('amount')) \
            .order_by('-amount__sum')
