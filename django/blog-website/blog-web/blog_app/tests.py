from django.test import TestCase
from django.contrib.auth.models import User
from django.db import IntegrityError
from blog_app.models import Blog, BlogReaction
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

class BlogModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='author', password='pass1234')
        self.blog = Blog.objects.create(
            title='Test Blog',
            content='This is the blog just for testing',
            author=self.user
        )

    def test_blog_created_successfully(self):
        blog = Blog.objects.get(id=self.blog.id)
        self.assertEqual(blog.title, 'Test Blog')
        self.assertEqual(blog.author, self.user)
        self.assertIsNotNone(blog.created_at)
        """__str__ returns the blog title."""
        self.assertEqual(str(self.blog), 'Test Blog')

        self.assertEqual(self.blog.likes_count, 0)


    def test_likes_count_increments(self):
        reactor = User.objects.create_user(username='reactor', password='pass1234')
        BlogReaction.objects.create(
            user=reactor,
            blog=self.blog,
            reaction='L'
        )
        self.assertEqual(self.blog.likes_count, 1)

    def test_likes_and_dislikes_are_independent(self):
        """Likes and dislikes are counted separately for the same blog."""
        liker = User.objects.create_user(username='liker', password='pass1234')
        disliker = User.objects.create_user(username='disliker', password='pass1234')
        BlogReaction.objects.create(user=liker, blog=self.blog, reaction='L')
        BlogReaction.objects.create(user=disliker, blog=self.blog, reaction='D')
        self.assertEqual(self.blog.likes_count, 1)
        self.assertEqual(self.blog.dislikes_count, 1)

    def test_multiple_users_can_like_same_blog(self):
        """Multiple different users can all like the same blog."""
        for i in range(3):
            u = User.objects.create_user(username=f'author{i}', password=f'password{i}')
            BlogReaction.objects.create(
                user=u, 
                blog=self.blog, 
                reaction='L'
            )
        self.assertEqual(self.blog.likes_count, 3)

class BlogReactionModelTest(TestCase):

    def setUp(self):
        """Create an author, a reactor, and a blog for reaction tests."""
        self.author = User.objects.create_user(username='author', password='pass1234')
        self.reactor = User.objects.create_user(username='reactor', password='pass1234')
        self.blog = Blog.objects.create(
            title='Test Blog',
            content='Content here',
            author=self.author
        )

    def test_reaction_created_successfully(self):
        reaction = BlogReaction.objects.create(
            user=self.reactor, 
            blog=self.blog, 
            reaction='L'
        )
        self.assertEqual(reaction.user, self.reactor)
        self.assertEqual(reaction.blog, self.blog)
        self.assertEqual(reaction.reaction, 'L')
        self.assertIsNotNone(reaction.created_at)

    def test_unique_together_prevents_duplicate_reaction(self):
        """A user cannot react to the same blog twice at the database level."""
        BlogReaction.objects.create(user=self.reactor, blog=self.blog, reaction='L')
        with self.assertRaises(IntegrityError):
            BlogReaction.objects.create(user=self.reactor, blog=self.blog, reaction='D')

    def test_different_users_can_react_to_same_blog(self):
        """Two different users can each react to the same blog."""
        other = User.objects.create_user(username='other', password='pass1234')
        BlogReaction.objects.create(user=self.reactor, blog=self.blog, reaction='L')
        BlogReaction.objects.create(user=other, blog=self.blog, reaction='L')
        self.assertEqual(BlogReaction.objects.filter(blog=self.blog).count(), 2)

    def test_same_user_can_react_to_different_blogs(self):
        """The same user can react to two different blogs."""
        blog2 = Blog.objects.create(
            title='Another Blog', 
            content='More content', 
            author=self.author
        )
        BlogReaction.objects.create(user=self.reactor, blog=self.blog, reaction='L')
        BlogReaction.objects.create(user=self.reactor, blog=blog2, reaction='D')
        self.assertEqual(BlogReaction.objects.filter(user=self.reactor).count(), 2)

class BlogAPITest(APITestCase):
    
    def setUp(self):
        """Create an admin, a regular user, and an existing blog."""
        self.client = APIClient()

        self.admin = User.objects.create_user(
            username='admin', password='admin1234', is_staff=True
        )
        self.regular_user = User.objects.create_user(
            username='regular', password='pass1234'
        )
        self.blog = Blog.objects.create(
            title='Existing Blog',
            content='Some content',
            author=self.admin
        )

    def test_guest_can_list_blogs(self):
        """Unauthenticated users can read the blog list."""
        response = self.client.get('/api/blogs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_returns_all_blogs(self):
        """Blog list contains all blogs in the database."""
        Blog.objects.create(title='Second Blog', content='Content', author=self.admin)
        response = self.client.get('/api/blogs/')
        self.assertEqual(len(response.data), 2)

    