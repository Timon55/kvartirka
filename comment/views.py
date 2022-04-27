from rest_framework import viewsets
from fluent_comments.models import FluentComment
from .serializers import CommentSerializer, PollSerializer
from .models import Poll
from django.contrib.contenttypes.models import ContentType
from rest_framework.response import Response
from datetime import datetime
from Kvartirka import settings



class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def retrieve(self, request, pk=None):
        poll = self.get_object(pk)
        serializer = self.serializer_class(poll, context={'request': request})
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = FluentComment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            data = self.request.data
            comment = data['comment']
            poll = data['Poll']
            if 'parent' in data:
                parent = data['parent']
            else:
                parent = None
            submit_date = datetime.now()
            content = ContentType.objects.get(model="Poll").pk
            comment = FluentComment.objects.create(object_pk=poll, comment=comment, submit_date=submit_date,
                                                   content_type_id=content, user_id=self.request.user.id,
                                                   site_id=settings.SITE_ID, parent_id=parent)
            serializer = CommentSerializer(comment, context={'request': request})
            return Response(serializer.data)
