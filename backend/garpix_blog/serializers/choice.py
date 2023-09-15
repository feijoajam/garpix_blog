from rest_framework import serializers

from garpix_blog.models import Choice


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ['id', 'title', 'poll', 'cnt_votes', 'percent']


class ChoiceCreateSerializer(serializers.ModelSerializer):
    percent = serializers.SerializerMethodField()

    class Meta:
        model = Choice
        fields = ['id', 'title', 'question', 'cnt_votes', 'percent']
