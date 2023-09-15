from rest_framework import serializers

from garpix_blog.models.poll import Poll
# from garpix_blog.serializers import ChoiceSerializer


class PollSerializer(serializers.ModelSerializer):
    # choices = ChoiceSerializer(many=True, source='choice_set', )
    # choices = ChoiceSerializer(many=True, source='choices', )

    class Meta:
        model = Poll
        fields = ['id', 'title', 'choices']
