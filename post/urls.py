from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListView, PostDetailView, PostEditView, PostDeleteView, CommentDeleteView, index
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', PostListView.as_view(), name='post-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('<int:post_pk>/comment_delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
]
