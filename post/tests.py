from django.test import TestCase, Client
from doctest import REPORT_CDIFF
from django.urls import reverse, reverse_lazy
from users import views
from urllib import request, response
from django.contrib.auth.models import User
from .views import PostListView, PostEditView, PostDeleteView, PostDetailView, CommentDeleteView
from .models import Post, Comment
from django.utils import timezone
from django.db import models

# Create your tests here.
class UserNotLoginTestCase(TestCase):
    def test_user_not_login(self):
            """ user not login """
            c = Client()
            response = c.get(reverse('post:index'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'users/login.html')

class PostListViewTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('test_user', password='test_pass')

    def test_post_list_view_status_code(self):
        """ post list view's status code is ok """
        c = Client()
        c.login(username='test_user', password='test_pass')
        response = c.get(reverse('post:post-list'))
        self.assertEqual(response.status_code, 200)

    def test_can_create_post(self):
        """ user can create post """

        c = Client()
        c.login(username='test_user', password='test_pass')
        response = c.post(reverse('post:post-list'), {'body': 'test post'})
        self.assertEqual(response.status_code, 200)

class PostDetailViewTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('test_user', password='test_pass')
        post = Post.objects.create(body='test', id=1, author=user)

    def test_post_detail_view_status_code(self):
        """ post detail view's status code is ok """

        c = Client()
        postTest = Post.objects.first()
        c.login(username='test_user', password='test_pass')
        response = c.get(reverse('post:post-detail', args=(postTest.id,)))
        self.assertEqual(response.status_code, 200)

    def test_can_create_comment(self):
        """ user can create comment """

        c = Client()
        postTest = Post.objects.first()
        c.login(username='test_user', password='test_pass')
        response = c.post(reverse('post:post-detail', args=(postTest.id, )), {'comment': 'test comment'})
        self.assertEqual(response.status_code, 200)

class PostEditViewTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('test_user', password='test_pass')
        post = Post.objects.create(body='test', id=1, author=user)

    def test_can_edit_post(self):
        """ user can edit your post """

        c = Client()
        postTest = Post.objects.first()
        c.login(username='test_user', password='test_pass')
        c.post(reverse('post:post-edit', args=(postTest.id,)), {'body': 'test body'})
        response = c.get(reverse('post:post-detail', args=(postTest.id,)))
        self.assertContains(response, 'test body')

class PostDeleteViewTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('test_user', password='test_pass')
        post = Post.objects.create(body='test', id=1, author=user)

    def test_can_delete_post(self):
        """ user can delete your post """

        c = Client()
        postTest = Post.objects.first()
        c.login(username='test_user', password='test_pass')
        c.post(reverse('post:post-delete', args=(postTest.id,)))
        response = c.get(reverse('post:post-list'))
        self.assertNotContains(response, 'test')
        

class CommentDeleteViewTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('test_user', password='test_pass')
        post = Post.objects.create(body='test', id=1, author=user)
        postTest = Post.objects.first()
        comment = Comment.objects.create(comment='test comment', post=postTest, author=user)

    def test_can_delete_comment(self):
        c = Client()
        postTest = Post.objects.first()
        commentTest = Post.objects.first()
        c.login(username='test_user', password='test_pass')
        c.post(reverse('post:comment-delete', args=(commentTest.id, postTest.id)))
        response = c.get(reverse('post:post-detail', args=(postTest.id,)))
        self.assertNotContains(response, 'test comment')
        