from django.test import TestCase
from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from blog_app.models import Blog, BlogReaction

# =============================================================================
# MODEL TESTS
# =============================================================================
# These tests check the database models directly — no HTTP involved.
# They verify fields, string representations, computed properties, and
# database-level constraints.
# =============================================================================


class BlogModelTest(TestCase):
    """Tests for the Blog model."""

    def setUp(self):
        """Create a user and a blog used by every test in this class."""
        self.user = User.objects.create_user(username='author', password='pass1234')
        self.blog = Blog.objects.create(
            title='Test Blog',
            content='This is the blog just for testing',
            author=self.user
        )

    # ── Creation & field values ───────────────────────────────────────────────

    def test_blog_created_successfully(self):
        """Blog is saved and retrievable from the database with correct fields."""
        blog = Blog.objects.get(id=self.blog.id)
        self.assertEqual(blog.title, 'Test Blog')
        self.assertEqual(blog.content, 'This is the blog just for testing')
        self.assertEqual(blog.author, self.user)

    def test_blog_auto_timestamps(self):
        """created_at and updated_at are set automatically on creation."""
        self.assertIsNotNone(self.blog.created_at)
        self.assertIsNotNone(self.blog.updated_at)

    def test_blog_str(self):
        """__str__ returns the blog title."""
        self.assertEqual(str(self.blog), 'Test Blog')

    # ── Reaction counters ─────────────────────────────────────────────────────

    def test_likes_count_default_zero(self):
        """A new blog starts with zero likes."""
        self.assertEqual(self.blog.likes_count, 0)

    def test_dislikes_count_default_zero(self):
        """A new blog starts with zero dislikes."""
        self.assertEqual(self.blog.dislikes_count, 0)

    def test_likes_count_increments(self):
        """likes_count reflects the number of Like reactions."""
        reactor = User.objects.create_user(username='reactor', password='pass1234')
        BlogReaction.objects.create(user=reactor, blog=self.blog, reaction='L')
        self.assertEqual(self.blog.likes_count, 1)

    def test_dislikes_count_increments(self):
        """dislikes_count reflects the number of Dislike reactions."""
        reactor = User.objects.create_user(username='reactor', password='pass1234')
        BlogReaction.objects.create(user=reactor, blog=self.blog, reaction='D')
        self.assertEqual(self.blog.dislikes_count, 1)

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
            u = User.objects.create_user(username=f'liker{i}', password='pass1234')
            BlogReaction.objects.create(user=u, blog=self.blog, reaction='L')
        self.assertEqual(self.blog.likes_count, 3)


class BlogReactionModelTest(TestCase):
    """Tests for the BlogReaction model."""

    def setUp(self):
        """Create an author, a reactor, and a blog for reaction tests."""
        self.author = User.objects.create_user(username='author', password='pass1234')
        self.reactor = User.objects.create_user(username='reactor', password='pass1234')
        self.blog = Blog.objects.create(
            title='Test Blog',
            content='Content here',
            author=self.author
        )

    # ── Creation & field values ───────────────────────────────────────────────

    def test_reaction_created_successfully(self):
        """A reaction is saved with the correct user, blog, and type."""
        reaction = BlogReaction.objects.create(
            user=self.reactor, blog=self.blog, reaction='L'
        )
        self.assertEqual(reaction.user, self.reactor)
        self.assertEqual(reaction.blog, self.blog)
        self.assertEqual(reaction.reaction, 'L')

    def test_reaction_auto_timestamp(self):
        """created_at is set automatically on a reaction."""
        reaction = BlogReaction.objects.create(
            user=self.reactor, blog=self.blog, reaction='L'
        )
        self.assertIsNotNone(reaction.created_at)

    def test_reaction_str(self):
        """__str__ returns a readable description of the reaction."""
        reaction = BlogReaction.objects.create(
            user=self.reactor, blog=self.blog, reaction='L'
        )
        self.assertEqual(str(reaction), 'reactor - Like on Test Blog')

    # ── Database constraint ───────────────────────────────────────────────────

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
            title='Another Blog', content='More content', author=self.author
        )
        BlogReaction.objects.create(user=self.reactor, blog=self.blog, reaction='L')
        BlogReaction.objects.create(user=self.reactor, blog=blog2, reaction='D')
        self.assertEqual(BlogReaction.objects.filter(user=self.reactor).count(), 2)


# =============================================================================
# API TESTS — BLOGS
# =============================================================================
# These tests hit the REST API endpoints and check HTTP status codes,
# response bodies, and permission rules.
#
# Permission matrix for blogs:
#   Guest       → read only (GET)
#   Regular user → read only (GET)
#   Admin (is_staff) → full CRUD
# =============================================================================


class BlogAPITest(APITestCase):
    """Tests for /api/blogs/ endpoints."""

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

    # ── GET /api/blogs/ — list ────────────────────────────────────────────────

    def test_guest_can_list_blogs(self):
        """Unauthenticated users can read the blog list."""
        response = self.client.get('/api/blogs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_returns_all_blogs(self):
        """Blog list contains all blogs in the database."""
        Blog.objects.create(title='Second Blog', content='Content', author=self.admin)
        response = self.client.get('/api/blogs/')
        self.assertEqual(len(response.data), 2)

    def test_list_response_contains_required_fields(self):
        """Each blog in the list includes all expected fields."""
        response = self.client.get('/api/blogs/')
        blog_data = response.data[0]
        for field in ['id', 'title', 'content', 'author', 'likes_count', 'dislikes_count', 'created_at']:
            self.assertIn(field, blog_data)

    def test_blogs_ordered_newest_first(self):
        """Blog list is ordered by created_at descending (newest first)."""
        newer = Blog.objects.create(
            title='Newer Blog', content='Content', author=self.admin
        )
        response = self.client.get('/api/blogs/')
        # The first item in the list should be the most recently created
        self.assertEqual(response.data[0]['id'], newer.id)

    # ── GET /api/blogs/{id}/ — retrieve ──────────────────────────────────────

    def test_guest_can_retrieve_single_blog(self):
        """Unauthenticated users can read a single blog by ID."""
        response = self.client.get(f'/api/blogs/{self.blog.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Existing Blog')

    def test_retrieve_nonexistent_blog_returns_404(self):
        """Requesting a blog with a non-existent ID returns 404."""
        response = self.client.get('/api/blogs/99999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_retrieve_response_contains_likes_and_dislikes(self):
        """Single blog response includes likes_count and dislikes_count."""
        response = self.client.get(f'/api/blogs/{self.blog.id}/')
        self.assertIn('likes_count', response.data)
        self.assertIn('dislikes_count', response.data)

    # ── POST /api/blogs/ — create ─────────────────────────────────────────────

    def test_admin_can_create_blog(self):
        """Admin (is_staff=True) can create a blog and gets 201."""
        self.client.force_authenticate(user=self.admin)
        response = self.client.post('/api/blogs/', {
            'title': 'New Blog',
            'content': 'New content'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Blog')

    def test_create_blog_author_is_set_automatically(self):
        """The author field is set to the logged-in admin, not sent by the client."""
        self.client.force_authenticate(user=self.admin)
        response = self.client.post('/api/blogs/', {
            'title': 'Auto Author Blog',
            'content': 'Content'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['author']['username'], 'admin')

    def test_create_blog_saves_to_database(self):
        """After a successful POST, the blog exists in the database."""
        self.client.force_authenticate(user=self.admin)
        self.client.post('/api/blogs/', {'title': 'DB Check', 'content': 'Content'})
        self.assertTrue(Blog.objects.filter(title='DB Check').exists())

    def test_regular_user_cannot_create_blog(self):
        """Regular user (is_staff=False) gets 403 on blog create."""
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.post('/api/blogs/', {
            'title': 'Sneaky Blog',
            'content': 'Should not work'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_guest_cannot_create_blog(self):
        """Unauthenticated request to create a blog gets 403."""
        response = self.client.post('/api/blogs/', {
            'title': 'Guest Blog',
            'content': 'Should not work'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_blog_without_title_fails(self):
        """Creating a blog without a title returns 400."""
        self.client.force_authenticate(user=self.admin)
        response = self.client.post('/api/blogs/', {'content': 'No title here'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_blog_without_content_fails(self):
        """Creating a blog without content returns 400."""
        self.client.force_authenticate(user=self.admin)
        response = self.client.post('/api/blogs/', {'title': 'No Content Blog'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_blog_with_title_too_long_fails(self):
        """Creating a blog with a title longer than 50 characters returns 400."""
        self.client.force_authenticate(user=self.admin)
        response = self.client.post('/api/blogs/', {
            'title': 'A' * 51,   # max_length is 50
            'content': 'Some content'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # ── PATCH /api/blogs/{id}/ — partial update ───────────────────────────────

    def test_admin_can_partial_update_blog(self):
        """Admin can PATCH (partially update) a blog."""
        self.client.force_authenticate(user=self.admin)
        response = self.client.patch(f'/api/blogs/{self.blog.id}/', {
            'title': 'Updated Title'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Title')

    def test_regular_user_cannot_partial_update_blog(self):
        """Regular user cannot PATCH a blog and gets 403."""
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.patch(f'/api/blogs/{self.blog.id}/', {
            'title': 'Hacked Title'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_guest_cannot_partial_update_blog(self):
        """Unauthenticated PATCH request gets 403."""
        response = self.client.patch(f'/api/blogs/{self.blog.id}/', {
            'title': 'Hacked Title'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ── PUT /api/blogs/{id}/ — full update ────────────────────────────────────

    def test_admin_can_full_update_blog(self):
        """Admin can PUT (fully replace) a blog."""
        self.client.force_authenticate(user=self.admin)
        response = self.client.put(f'/api/blogs/{self.blog.id}/', {
            'title': 'Fully Replaced Title',
            'content': 'Fully replaced content'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Fully Replaced Title')
        self.assertEqual(response.data['content'], 'Fully replaced content')

    def test_regular_user_cannot_full_update_blog(self):
        """Regular user cannot PUT a blog and gets 403."""
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.put(f'/api/blogs/{self.blog.id}/', {
            'title': 'Unauthorized Replace',
            'content': 'Should fail'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ── DELETE /api/blogs/{id}/ ───────────────────────────────────────────────

    def test_admin_can_delete_blog(self):
        """Admin can delete a blog and gets 204."""
        self.client.force_authenticate(user=self.admin)
        response = self.client.delete(f'/api/blogs/{self.blog.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_removes_blog_from_database(self):
        """After a successful DELETE, the blog no longer exists in the database."""
        self.client.force_authenticate(user=self.admin)
        blog_id = self.blog.id
        self.client.delete(f'/api/blogs/{blog_id}/')
        self.assertFalse(Blog.objects.filter(id=blog_id).exists())

    def test_regular_user_cannot_delete_blog(self):
        """Regular user cannot delete a blog and gets 403."""
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.delete(f'/api/blogs/{self.blog.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_guest_cannot_delete_blog(self):
        """Unauthenticated DELETE request gets 403."""
        response = self.client.delete(f'/api/blogs/{self.blog.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_nonexistent_blog_returns_404(self):
        """Deleting a blog with a non-existent ID returns 404."""
        self.client.force_authenticate(user=self.admin)
        response = self.client.delete('/api/blogs/99999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


# =============================================================================
# API TESTS — REACTIONS
# =============================================================================
# Permission matrix for reactions:
#   Guest            → read only (GET)
#   Admin (is_staff) → read only (GET) — blocked from write
#   Regular user     → full CRUD
# =============================================================================


class BlogReactionAPITest(APITestCase):
    """Tests for /api/reactions/ endpoints."""

    def setUp(self):
        """Create an admin, a regular user, a blog, and a second regular user."""
        self.client = APIClient()

        self.admin = User.objects.create_user(
            username='admin', password='admin1234', is_staff=True
        )
        self.regular_user = User.objects.create_user(
            username='regular', password='pass1234'
        )
        self.another_user = User.objects.create_user(
            username='another', password='pass1234'
        )
        self.blog = Blog.objects.create(
            title='Test Blog',
            content='Content here',
            author=self.admin
        )

    # ── GET /api/reactions/ — list ────────────────────────────────────────────

    def test_guest_can_list_reactions(self):
        """Unauthenticated users can view the reactions list."""
        response = self.client.get('/api/reactions/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_regular_user_can_list_reactions(self):
        """Authenticated regular user can view the reactions list."""
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.get('/api/reactions/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # ── GET /api/reactions/{id}/ — retrieve ──────────────────────────────────

    def test_guest_can_retrieve_single_reaction(self):
        """Unauthenticated users can read a single reaction by ID."""
        reaction = BlogReaction.objects.create(
            user=self.regular_user, blog=self.blog, reaction='L'
        )
        response = self.client.get(f'/api/reactions/{reaction.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['reaction'], 'L')

    def test_retrieve_nonexistent_reaction_returns_404(self):
        """Requesting a reaction with a non-existent ID returns 404."""
        response = self.client.get('/api/reactions/99999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # ── POST /api/reactions/ — create ─────────────────────────────────────────

    def test_regular_user_can_like(self):
        """Regular user can post a Like reaction and gets 201."""
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.post('/api/reactions/', {
            'blog': self.blog.id,
            'reaction': 'L'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['reaction'], 'L')

    def test_regular_user_can_dislike(self):
        """Regular user can post a Dislike reaction and gets 201."""
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.post('/api/reactions/', {
            'blog': self.blog.id,
            'reaction': 'D'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['reaction'], 'D')

    def test_reaction_user_is_set_automatically(self):
        """The user field on a reaction is set to the logged-in user automatically."""
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.post('/api/reactions/', {
            'blog': self.blog.id,
            'reaction': 'L'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # user is a StringRelatedField so it returns the username string
        self.assertEqual(response.data['user'], 'regular')

    def test_admin_cannot_react(self):
        """Admin (is_staff=True) is blocked from creating a reaction."""
        self.client.force_authenticate(user=self.admin)
        response = self.client.post('/api/reactions/', {
            'blog': self.blog.id,
            'reaction': 'L'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_guest_cannot_react(self):
        """Unauthenticated users cannot create a reaction."""
        response = self.client.post('/api/reactions/', {
            'blog': self.blog.id,
            'reaction': 'L'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_invalid_reaction_choice_rejected(self):
        """A reaction value other than 'L' or 'D' returns 400."""
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.post('/api/reactions/', {
            'blog': self.blog.id,
            'reaction': 'X'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_reaction_without_blog_field_fails(self):
        """Posting a reaction without specifying a blog returns 400."""
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.post('/api/reactions/', {'reaction': 'L'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_reaction_to_nonexistent_blog_fails(self):
        """Posting a reaction for a blog that doesn't exist returns 400."""
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.post('/api/reactions/', {
            'blog': 99999,
            'reaction': 'L'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_can_change_reaction(self):
        """
        A user can POST a second reaction to the same blog to switch from
        Like to Dislike. The serializer uses update_or_create, so the
        existing record is updated instead of creating a duplicate.
        """
        self.client.force_authenticate(user=self.regular_user)
        # First reaction: Like
        self.client.post('/api/reactions/', {'blog': self.blog.id, 'reaction': 'L'})
        # Second POST: switch to Dislike
        self.client.post('/api/reactions/', {'blog': self.blog.id, 'reaction': 'D'})

        # Only one reaction record should exist for this user/blog
        self.assertEqual(
            BlogReaction.objects.filter(user=self.regular_user, blog=self.blog).count(), 1
        )
        # And the stored value should be the latest one
        reaction = BlogReaction.objects.get(user=self.regular_user, blog=self.blog)
        self.assertEqual(reaction.reaction, 'D')

    # ── Blog counts after reactions ───────────────────────────────────────────

    def test_likes_count_updates_after_like(self):
        """Blog likes_count increases to 1 after a Like reaction."""
        self.client.force_authenticate(user=self.regular_user)
        self.client.post('/api/reactions/', {'blog': self.blog.id, 'reaction': 'L'})

        response = self.client.get(f'/api/blogs/{self.blog.id}/')
        self.assertEqual(response.data['likes_count'], 1)
        self.assertEqual(response.data['dislikes_count'], 0)

    def test_dislikes_count_updates_after_dislike(self):
        """Blog dislikes_count increases to 1 after a Dislike reaction."""
        self.client.force_authenticate(user=self.regular_user)
        self.client.post('/api/reactions/', {'blog': self.blog.id, 'reaction': 'D'})

        response = self.client.get(f'/api/blogs/{self.blog.id}/')
        self.assertEqual(response.data['dislikes_count'], 1)
        self.assertEqual(response.data['likes_count'], 0)

    def test_counts_reflect_multiple_users(self):
        """likes_count correctly reflects reactions from multiple users."""
        self.client.force_authenticate(user=self.regular_user)
        self.client.post('/api/reactions/', {'blog': self.blog.id, 'reaction': 'L'})

        self.client.force_authenticate(user=self.another_user)
        self.client.post('/api/reactions/', {'blog': self.blog.id, 'reaction': 'L'})

        response = self.client.get(f'/api/blogs/{self.blog.id}/')
        self.assertEqual(response.data['likes_count'], 2)

    def test_counts_update_when_reaction_is_changed(self):
        """
        When a user switches from Like to Dislike, likes_count drops to 0
        and dislikes_count rises to 1 (no double-counting).
        """
        self.client.force_authenticate(user=self.regular_user)
        self.client.post('/api/reactions/', {'blog': self.blog.id, 'reaction': 'L'})
        self.client.post('/api/reactions/', {'blog': self.blog.id, 'reaction': 'D'})

        response = self.client.get(f'/api/blogs/{self.blog.id}/')
        self.assertEqual(response.data['likes_count'], 0)
        self.assertEqual(response.data['dislikes_count'], 1)

    # ── DELETE /api/reactions/{id}/ ───────────────────────────────────────────

    def test_regular_user_can_delete_own_reaction(self):
        """Regular user can delete their own reaction and gets 204."""
        self.client.force_authenticate(user=self.regular_user)
        post_resp = self.client.post('/api/reactions/', {
            'blog': self.blog.id,
            'reaction': 'L'
        })
        reaction_id = post_resp.data['id']
        delete_resp = self.client.delete(f'/api/reactions/{reaction_id}/')
        self.assertEqual(delete_resp.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_reaction_removes_it_from_database(self):
        """After deleting a reaction, it no longer exists in the database."""
        self.client.force_authenticate(user=self.regular_user)
        post_resp = self.client.post('/api/reactions/', {
            'blog': self.blog.id,
            'reaction': 'L'
        })
        reaction_id = post_resp.data['id']
        self.client.delete(f'/api/reactions/{reaction_id}/')
        self.assertFalse(BlogReaction.objects.filter(id=reaction_id).exists())

    def test_admin_cannot_delete_reaction(self):
        """Admin is blocked from deleting a reaction."""
        # Create the reaction as a regular user first
        reaction = BlogReaction.objects.create(
            user=self.regular_user, blog=self.blog, reaction='L'
        )
        self.client.force_authenticate(user=self.admin)
        response = self.client.delete(f'/api/reactions/{reaction.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_guest_cannot_delete_reaction(self):
        """Unauthenticated users cannot delete a reaction."""
        reaction = BlogReaction.objects.create(
            user=self.regular_user, blog=self.blog, reaction='L'
        )
        response = self.client.delete(f'/api/reactions/{reaction.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ── PATCH /api/reactions/{id}/ — partial update ───────────────────────────

    def test_regular_user_can_patch_own_reaction(self):
        """Regular user can PATCH their own reaction to change its value."""
        reaction = BlogReaction.objects.create(
            user=self.regular_user, blog=self.blog, reaction='L'
        )
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.patch(f'/api/reactions/{reaction.id}/', {
            'reaction': 'D'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['reaction'], 'D')

    def test_admin_cannot_patch_reaction(self):
        """Admin is blocked from PATCHing a reaction."""
        reaction = BlogReaction.objects.create(
            user=self.regular_user, blog=self.blog, reaction='L'
        )
        self.client.force_authenticate(user=self.admin)
        response = self.client.patch(f'/api/reactions/{reaction.id}/', {
            'reaction': 'D'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
