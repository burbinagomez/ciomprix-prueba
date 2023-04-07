from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Person
from .serializers import PersonSerializer

# Definimos los datos de prueba
def sample_person(name='John', age=30):
    """Crea y devuelve una persona de prueba"""
    return Person.objects.create(name=name, age=age)

# Definimos la clase de tests
class PersonAPITests(TestCase):
    def setUp(self):
        """Configuración de los tests"""
        self.client = APIClient()

    def test_create_person(self):
        """Prueba la creación de una nueva persona"""
        url = reverse('persona-created')
        data = {'name': 'Jane', 'age': 25}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        person = Person.objects.get(id=response.data['id'])
        self.assertEqual(person.name, data['name'])
        self.assertEqual(person.age, data['age'])

    def test_list_people(self):
        """Prueba la lista de todas las personas"""
        sample_person()
        sample_person()
        url = reverse('persona-list')
        response = self.client.get(url)

        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_person(self):
        """Prueba la obtención de una persona específica"""
        person = sample_person()
        url = reverse('persona-detail', args=[person.id])
        response = self.client.get(url)

        serializer = PersonSerializer(person)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_person(self):
        """Prueba la actualización de una persona"""
        person = sample_person()
        url = reverse('persona-update', args=[person.id])
        data = {'name': 'Mark', 'age': 40}
        response = self.client.put(url, data)

        person.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(person.name, data['name'])
        self.assertEqual(person.age, data['age'])

    def test_delete_person(self):
        """Prueba la eliminación de una persona"""
        person = sample_person()
        url = reverse('persona-delete', args=[person.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Person.objects.filter(id=person.id).exists())
