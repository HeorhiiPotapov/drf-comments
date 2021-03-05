from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    ListCreateAPIView
)
from rest_framework.permissions import AllowAny
from django.db.models import Q
from .models import Thread, Comment
from .serializers import (
    ThreadSerializer,
    CommentSerializer,
    CommentCreateSerializer
)
from .pagination import CommentsPagination, ThreadPagination
from .ip import get_client_ip, get_useragent


class ThreadListView(ListCreateAPIView):
    serializer_class = ThreadSerializer
    queryset = Thread.objects.all()
    permission_classes = [AllowAny, ]
    pagination_class = ThreadPagination


class CommentListView(ListAPIView):
    serializer_class = CommentSerializer
    pagination_class = CommentsPagination

    def get_queryset(self):
        queryset = Comment.objects.filter(
            thread=self.kwargs['pk']).order_by('-created')

        query = self.request.query_params
        by_time = ['reverse', ]
        by_user = ['username', 'email']

        if len(query.keys()) > 0:
            for key in query.keys():
                if query[key] in by_time:
                    queryset = queryset.order_by('created')
                elif key in by_user:
                    queryset = queryset.filter(
                        Q(username=query[key]) | Q(email=query[key])
                    )
        return queryset


class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [AllowAny, ]

    def perform_create(self, serializer):
        ip = get_client_ip(self.request)
        useragent = get_useragent(self.request)
        serializer.save(user_ip=ip, useragent=useragent)
