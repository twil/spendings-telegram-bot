from django.conf import settings
from django.db import models


class Spending(models.Model):
    """
    Captures who spent money. When he did it. And especially how many.
    """

    CURRENCY_RUB = 'rub'
    CURRENCY_USD = 'usd'
    CURRENCY_EUR = 'eur'
    CURRENCY_CHOICES = (
        (CURRENCY_RUB, CURRENCY_RUB),
        (CURRENCY_USD, CURRENCY_USD),
        (CURRENCY_EUR, CURRENCY_EUR),
    )

    amount = models.DecimalField(max_digits=11, decimal_places=2)
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        default=CURRENCY_RUB,
    )
    labels = models.ManyToManyField('Label', blank=True)
    # who spent money
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
    )
    datetime = models.DateTimeField()

    class Meta:
        ordering = ('-datetime',)

    def __str__(self):
        return '{owner}: {amount} {currency}'.format(
            owner=self.owner.get_full_name() if self.owner else '???',
            amount=self.amount,
            currency=self.currency,
        )


class Label(models.Model):
    """
    Labels a spending. There might be synonyms.

    Only the parent should be used.
    """

    name = models.CharField(max_length=255, blank=True, default='')
    synonym_of = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name='+',
        blank=True,
    )

    def __str__(self):
        return self.name
