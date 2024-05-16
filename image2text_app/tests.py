from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Image, Style, GeneratedText
from django.core.files.uploadedfile import SimpleUploadedFile
from unittest.mock import patch

class Image2TextAppTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        self.client.login(username='testuser', password='testpassword123')

    def test_upload_image_view(self):
        # Test uploading an image with a description
        image_data = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        response = self.client.post(reverse('upload_image'), {'image_file': image_data, 'description': 'Test Image'})
        self.assertEqual(response.status_code, 302)  # Redirect after successful upload
        self.assertTrue(Image.objects.filter(description='Test Image').exists())
        self.assertIn('Upload successful', response.content.decode())  # Check response content

    def test_select_style_view(self):
        # Test selecting a style
        style = Style.objects.create(type='Expository', tone='Informative', voice='Shakespeare', length=1000)
        response = self.client.post(reverse('style_selection', args=[style.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Style selected successfully')

    def test_upload_image_view_no_file(self):
        # Test uploading an image without providing a file
        response = self.client.post(reverse('upload_image'), {'description': 'Test Image'})
        self.assertEqual(response.status_code, 400)  # Bad request due to missing file
        self.assertFalse(Image.objects.filter(description='Test Image').exists())

    def test_select_style_view_invalid(self):
        # Test selecting an invalid style
        response = self.client.post(reverse('style_selection', args=[999]))
        self.assertEqual(response.status_code, 404)  # Not found due to invalid style ID

    def test_upload_image_view_unauthenticated(self):
        # Test uploading an image when the user is not authenticated
        self.client.logout()
        image_data = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        response = self.client.post(reverse('upload_image'), {'image_file': image_data, 'description': 'Test Image'})
        self.assertEqual(response.status_code, 302)  # Redirects to login page for unauthenticated users

    @patch('image2text_app.views.openai.Completion.create')
    def test_generate_text_view(self, mock_create):
        # Mock the OpenAI API call
        mock_create.return_value = {'choices': [{'text': 'Generated text'}]}
        image = Image.objects.create(user=self.user, description='Test Image')
        style = Style.objects.create(type='Expository', tone='Informative', voice='Shakespeare', length=1000)
        response = self.client.post(reverse('generate_text', args=[image.id, style.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after successful text generation
        self.assertTrue(GeneratedText.objects.filter(image=image, style=style).exists())

    def test_generate_text_view_invalid_image(self):
        # Test generating text for an invalid image
        response = self.client.post(reverse('generate_text', args=[999, 1]))
        self.assertEqual(response.status_code, 404)  # Not found due to invalid image ID

    def test_generate_text_view_invalid_style(self):
        # Test generating text with an invalid style
        image = Image.objects.create(user=self.user, description='Test Image')
        response = self.client.post(reverse('generate_text', args=[image.id, 999]))
        self.assertEqual(response.status_code, 404)  # Not found due to invalid style ID

    def tearDown(self):
        # Clean up any files created during the tests
        for image in Image.objects.all():
            image.image_file.delete()

    # Add more tests as needed for other views and scenarios
