from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Thread, Comment


class ThreadSerializer(ModelSerializer):

    comments_count = SerializerMethodField()

    class Meta:
        model = Thread
        fields = ['id', 'name', 'comments_count']

    @staticmethod
    def get_comments_count(obj):
        return obj.comments.count()


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'thread', 'parent', 'username', 'email',
                  'text', 'created', 'modified', 'user_ip', 'useragent']


class CommentCreateSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'thread', 'parent', 'username', 'email',
                  'text', 'created', 'modified']
