from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet
from garpix_blog.models import Vote
from garpix_blog.serializers import VoteSerializer


class VoteViewSet(ModelViewSet):
    queryset = Vote.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['created_at', 'updated_at', ]

    def get_serializer_class(self):
        return VoteSerializer

    def perform_create(self, serializer):
        choice = serializer.validated_data.get('choice', None)
        choice.upvote()
        return serializer.save()

    def perform_destroy(self, instance):
        instance.choice.downvote()
        super().perform_destroy(instance)
