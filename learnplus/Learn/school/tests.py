from django.test import TestCase
from .models import Matiere

class MatiereModelTestCase(TestCase):
    def setUp(self):
        self.matiere = Matiere.objects.create(
            nom="Histoire",
            description="Description d'un cours d'histoire"
        )

    def test_instance_creation(self):
        self.assertEqual(self.matiere.nom, "Histoire")
        self.assertEqual(self.matiere.description, "Description d'un cours d'histoire")
        self.assertIsNotNone(self.matiere.slug)

    def test_default_values(self):
        self.assertTrue(self.matiere.status)
        self.assertIsNone(self.matiere.image)

    def test_slug_generation(self):
        self.assertTrue(self.matiere.slug.startswith("histoire"))
