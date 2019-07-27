from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Spending, Label


@admin.register(Spending)
class SpendingAdmin(admin.ModelAdmin):
    list_display = ('amount', 'currency', 'labels_list', 'datetime', 'owner',)
    list_filter = ('owner', 'datetime', 'labels',)

    def labels_list(self, obj):
        labels = []
        for l in obj.labels.all().order_by('name'):
            labels.append(l.name)

        return mark_safe('<br>'.join(labels))


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    pass
