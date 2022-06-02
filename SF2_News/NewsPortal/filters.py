import django
from django_filters import FilterSet, DateFilter
from django.forms import DateInput
from .models import Post


class PostFilter(FilterSet):
    date_added = DateFilter(
        lookup_expr='gt',
        widget=DateInput(
            attrs={
                'type': 'date'
            }
        )
    )
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'author': ['exact'],
            'category': ['exact'],

        }