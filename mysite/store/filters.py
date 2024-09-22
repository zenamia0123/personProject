from django_filters import FilterSet
from .models import *

class TaskFilter(FilterSet):
    class Meta:
        model = Task
        fields = {'created': ['gt', 'lt'],
                  'completed': ['exact'],
                  }