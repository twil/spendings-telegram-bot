# Generated by Django 2.2.3 on 2019-07-26 23:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255)),
                ('synonym_of', models.ManyToManyField(related_name='_label_synonym_of_+', to='spendings.Label')),
            ],
        ),
        migrations.CreateModel(
            name='Spending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('currency', models.CharField(choices=[('rub', 'rub'), ('usd', 'usd'), ('eur', 'eur')], default='rub', max_length=3)),
                ('datetime', models.DateTimeField()),
                ('labels', models.ManyToManyField(to='spendings.Label')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
