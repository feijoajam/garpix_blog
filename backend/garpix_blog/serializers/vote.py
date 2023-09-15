from rest_framework import serializers

from garpix_blog.models import Vote


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = ['id', 'user', 'choice']

    def update(self, instance, validated_data):
        new_choice = validated_data.get('choice')
        old_choice = instance.choice
        if new_choice != old_choice:
            new_choice.upvote()
            old_choice.downvote()
        return super().update(instance, validated_data)
