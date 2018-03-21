from .models import answer
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = answer
        fields = ['user_name', ]