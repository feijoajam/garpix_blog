from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet
from garpix_blog.models.poll import Poll

from garpix_blog.serializers.poll import PollSerializer


class PollViewSet(ModelViewSet):
    queryset = Poll.active_objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['updated_at', ]

    def get_serializer_class(self):
        return PollSerializer

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     d = instance.update_percents()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)
