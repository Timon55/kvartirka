from fluent_comments.models import FluentComment
from rest_framework import serializers
from .models import Poll


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(
            value,
            context=self.context)
        return serializer.data


class CommentSerializerWithoutChildren(serializers.ModelSerializer):
    #children = RecursiveField(many=True)

    class Meta:
        model = FluentComment
        fields = (
            'tree_path',
            'object_pk',
            'comment',
            'id',
        )


class CommentSerializerFull(serializers.ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = FluentComment
        fields = (
            'tree_path',
            'object_pk',
            'comment',
            'id',
            'children'
        )


class PollSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Poll
        fields = ('id', 'name', 'details', 'comments')

    @staticmethod
    def get_comments(obj):
        poll_comment = FluentComment.objects.filter(object_pk=obj.id, tree_path__regex="^.{10}$|^.{21}$|^.{32}$")
        serializer = CommentSerializerWithoutChildren(poll_comment, many=True)
        data = serializer.data
        return data


class CommentThreeAndMoreLevel(serializers.ModelSerializer):

    comments = serializers.SerializerMethodField()

    class Meta:
        model = FluentComment
        fields = (
            'tree_path',
            'object_pk',
            'comment',
            'id',
            'parent',
            'comments',
        )

    @staticmethod
    def get_comments(obj):
        nested_comment = FluentComment.objects.filter(parent_id=obj.id)
        serializer = CommentSerializerWithoutChildren(nested_comment, many=True)
        data = serializer.data
        return data
