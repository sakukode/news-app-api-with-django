from django_filters import rest_framework as filters

from .models import News


class NewsFilter(filters.FilterSet):
    # custom filter news berdasarkan nama kategori
    categories = filters.CharFilter(field_name="categories__name", lookup_expr='exact')
    # custom filter tanggal publish news/berita 
    # berdasarkan range tanggal dari parameter published_after & published_before
    published = filters.DateFromToRangeFilter(field_name="published_at")

    class Meta:
        model = News
        fields = ['title', 'categories', 'published']