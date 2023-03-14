import math

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory, APISimpleTestCase, APITestCase, force_authenticate

from todoapp.models import Project, ToDo
from todoapp.views import ProjectViewSet
from userapp.models import User


class TestProjectViewSet(TestCase):
    def setUp(self) -> None:
        self.name = "admin2"
        self.password = "123456789"
        self.email = "admin_123456789@mail.ru"

        self.data = {
            "name": "Александр",
            "users": "Пушкин",
            "repository": "https://github.com/Nikolos123/drf_1294_1187_1186/",
        }
        self.data_put = {"first_name": "Николай", "last_name": "Пушкин", "birthday_year": 1990}
        self.url = "/api/projects/"
        self.admin = User.objects.create_superuser(self.name, self.email, self.password)

    # APIRequestFactory force_authenticate
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        view = ProjectViewSet.as_view({"get": "list"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.data, format="json")
        view = ProjectViewSet.as_view({"post": "create"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.data, format="json")
        force_authenticate(request, self.admin)
        view = ProjectViewSet.as_view({"post": "create"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # APIClient
    def test_get_detail(self):
        client = APIClient()
        author = ToDo.objects.create(**self.data)
        response = client.get(f"{self.url}{author.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_guest(self):
        client = APIClient()
        author = Project.objects.create(**self.data)
        response = client.put(f"{self.url}{author.id}/", self.data_put)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_admin(self):
        client = APIClient()
        author = Project.objects.create(**self.data)
        client.login(username=self.name, password=self.password)
        response = client.put(f"{self.url}{author.id}/", self.data_put)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # APISimpleTestCase


class TestMath(APISimpleTestCase):
    def test_sqrt(self):
        self.assertEqual(math.sqrt(4), 2)


# APITestCase
class TestBiography(APITestCase):
    def setUp(self) -> None:
        self.name = "admin2"
        self.password = "123456789"
        self.email = "admin_123456789@mail.ru"

        self.data = {
            "name": "Александр",
            "users": "Пушкин",
            "repository": "https://github.com/Nikolos123/drf_1294_1187_1186/",
        }
        self.data_put = {"first_name": "Николай", "last_name": "Пушкин", "birthday_year": 1990}
        self.url = "/api/projects/"
        self.admin = User.objects.create_superuser(self.name, self.email, self.password)

    def test_get_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_admin(self):
        author = Project.objects.create(**self.data)
        bio = ToDo.objects.create(text="test", author=author)
        self.client.login(username=self.name, password=self.password)
        response = self.client.put(f"{self.url}{bio.id}/", {"text": "Biography", "author": bio.author.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
