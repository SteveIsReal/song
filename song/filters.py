import django_filters as filters
from song.models import Author

class AuthorFilter(filters.FilterSet):
    n = filters.CharFilter(lookup_expr='istartswith', field_name="name")
    sn = filters.CharFilter(lookup_expr='icontains', field_name="song__name")

    p_gte = filters.NumberFilter(method='filter_price')
    m_gte = filters.DateFilter(method='filter_month' )

    def filter_price(self, queryset, name, value):
        return queryset.filter(song__price__gte=value)

    def filter_month(self, queryset, name, value):
        return queryset.filter(birth_date__gte = value)

    class Meta:
        model = Author
        fields = []
