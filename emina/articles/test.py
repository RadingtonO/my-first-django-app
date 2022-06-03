from django.test import TestCase
from django.urls import reverse

from .models import *


class ModelsTestCase(TestCase):

    def test_categories_title(self):
        category = Categories.objects.create(title="My first category")
        category.save()
        self.assertEqual(category.title, "My first category")


class UrlsTemplatesTestCase(TestCase):

    def test_template_name_main(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/index.html')

    def test_templates_name_register(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/register.html')

    def test_templates_name_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/login.html')



