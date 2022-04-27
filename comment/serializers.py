from fluent_comments.models import FluentComment
from rest_framework import serializers
from .models import Poll


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(
            value,
            context=self.context)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = FluentComment
        fields = (
            'comment',
            'id',
            'children',
        )


class PollSerializer(serializers.Serializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Poll
        fields = ('name', 'details', 'comments')

    def get_comments(self, obj):
        poll_comment = FluentComment.objects.filter(object_pk=obj.id, parent_id=None)
        serializer = CommentSerializer(poll_comment, many=True)
        return serializer.data