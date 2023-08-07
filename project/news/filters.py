from django_filters import FilterSet, DateTimeFilter
from .models import Post, PostCategory
from django.forms import DateTimeInput
import django_filters
from django import forms



POSITIONS = [
        ('article','статьи'),
        ('news','новости')
    ]
class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Поиск по названию')

    type = django_filters.ChoiceFilter(choices=POSITIONS, label='поиск по категории')

    dateCreation = django_filters.IsoDateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label='Поиск по дате',
        widget=DateTimeInput(
            format='%Y-%m-%dT',
            attrs={'type': 'date'},
        )
    )
    class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
        model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
        fields = {'title','dateCreation','type'}


