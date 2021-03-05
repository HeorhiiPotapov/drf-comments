from django.urls import path
from . import views

urlpatterns = [
    path('', views.ThreadListView.as_view()),
    path('create-comment/', views.CommentCreateView.as_view()),
    path('<int:pk>/', views.CommentListView.as_view()),
]
