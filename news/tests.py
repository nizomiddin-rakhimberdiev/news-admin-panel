from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Mavzu', text = 'yangilik matni', author='Falonchiyev Pistonchi')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_title = f"{post.title}"
        expected_object_text = f'{post.text}'
        expected_object_author = f'{post.author}'
        self.assertEqual(expected_object_title, 'Mavzu')
        self.assertEqual(expected_object_text, 'yangilik matni')
        self.assertEqual(expected_object_author, 'Falonchiyev Pistonchi')


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(title = 'Mavzu 2', text = 'boshqa yangilik', author='boshqa aftor')

    def test_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEquals(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEquals(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')