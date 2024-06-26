from . import views
from django.urls import path

urlpatterns = [
    path('create/', views.create_post, name='create_post'),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('post/<slug:slug>/upvote/', views.upvote_post, name='upvote_post'),
    path('post/<slug:slug>/downvote/',
         views.downvote_post, name='downvote_post'),
]