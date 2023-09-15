from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet
from garpix_blog.models import Choice
from garpix_blog.serializers import ChoiceSerializer


class ChoiceViewSet(ModelViewSet):
    queryset = Choice.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['updated_at', ]

    def get_serializer_class(self):
        return ChoiceSerializer
