from django.test import TestCase
from django.contrib.auth.models import User
from .models import Student
from quiz.models import Quiz
from school.models import Classe

class StudentModelTestCase(TestCase):

    def setUp(self):
        # Création d'un utilisateur
        self.user = User.objects.create_user(username='teststudent', password='password123')

        # Création d'une classe
        self.classe = Classe.objects.create(
            niveau_id=1,  # Assurez-vous qu'un niveau existe ou créez-en un avant
            numeroClasse=1
        )

        # Création d'un quiz
        self.quiz = Quiz.objects.create(
            name="Quiz Test",
            description="Description du quiz"
        )

        # Création d'un étudiant
        self.student = Student.objects.create(
            user=self.user,
            classe=self.classe,
            ville="Yamoussoukro",
            score=10
        )

    def test_student_instance_creation(self):
        """Test de création d'une instance Student"""
        self.assertEqual(self.student.user.username, "teststudent")
        self.assertEqual(self.student.classe, self.classe)
        self.assertEqual(self.student.ville, "Yamoussoukro")
        self.assertEqual(self.student.score, 10)

    def test_slug_generation(self):
        """Test de la génération automatique du slug"""
        self.assertIsNotNone(self.student.slug)
        self.assertTrue(self.student.slug.startswith("teststudent-"))

    def test_get_u_type(self):
        """Test de la méthode get_u_type"""
        self.assertTrue(self.student.get_u_type)

    def test_get_unanswered_questions(self):
        """Test de la méthode get_unanswered_questions"""
        # Ajouter une question au quiz
        question = self.quiz.questions.create(text="Quelle est la capitale ?", order=1)

        # Vérifier les questions non répondues
        unanswered_questions = self.student.get_unanswered_questions(self.quiz)
        self.assertEqual(unanswered_questions.count(), 1)
        self.assertEqual(unanswered_questions.first(), question)

    def test_get_successful_quizzes_count(self):
        """Test de la méthode get_successful_quizzes_count"""
        # Simuler la réussite d'un quiz
        taken_quiz = self.student.quizzes.through.objects.create(
            student=self.student,
            quiz=self.quiz,
            percentage=80  # Pourcentage de réussite
        )
        successful_quizzes_count = self.student.get_successful_quizzes_count()
        self.assertEqual(successful_quizzes_count, 1)

    def test_default_values(self):
        """Test des valeurs par défaut"""
        self.assertEqual(self.student.bio, "Votre bio")
        self.assertTrue(self.student.status)
        self.assertIsNone(self.student.photo)
        from django.test import TestCase
from django.contrib.auth.models import User
from .models import Student
from quiz.models import Quiz
from school.models import Classe

class StudentModelTestCase(TestCase):

    def setUp(self):
        # Création d'un utilisateur
        self.user = User.objects.create_user(username='teststudent', password='password123')

        # Création d'une classe
        self.classe = Classe.objects.create(
            niveau_id=1,  # Assurez-vous qu'un niveau existe ou créez-en un avant
            numeroClasse=1
        )

        # Création d'un quiz
        self.quiz = Quiz.objects.create(
            name="Quiz Test",
            description="Description du quiz"
        )

        # Création d'un étudiant
        self.student = Student.objects.create(
            user=self.user,
            classe=self.classe,
            ville="Yamoussoukro",
            score=10
        )

    def test_student_instance_creation(self):
        """Test de création d'une instance Student"""
        self.assertEqual(self.student.user.username, "teststudent")
        self.assertEqual(self.student.classe, self.classe)
        self.assertEqual(self.student.ville, "Yamoussoukro")
        self.assertEqual(self.student.score, 10)

    def test_slug_generation(self):
        """Test de la génération automatique du slug"""
        self.assertIsNotNone(self.student.slug)
        self.assertTrue(self.student.slug.startswith("teststudent-"))

    def test_get_u_type(self):
        """Test de la méthode get_u_type"""
        self.assertTrue(self.student.get_u_type)

    def test_get_unanswered_questions(self):
        """Test de la méthode get_unanswered_questions"""
        # Ajouter une question au quiz
        question = self.quiz.questions.create(text="Quelle est la capitale ?", order=1)

        # Vérifier les questions non répondues
        unanswered_questions = self.student.get_unanswered_questions(self.quiz)
        self.assertEqual(unanswered_questions.count(), 1)
        self.assertEqual(unanswered_questions.first(), question)

    def test_get_successful_quizzes_count(self):
        """Test de la méthode get_successful_quizzes_count"""
        # Simuler la réussite d'un quiz
        taken_quiz = self.student.quizzes.through.objects.create(
            student=self.student,
            quiz=self.quiz,
            percentage=80  # Pourcentage de réussite
        )
        successful_quizzes_count = self.student.get_successful_quizzes_count()
        self.assertEqual(successful_quizzes_count, 1)

    def test_default_values(self):
        """Test des valeurs par défaut"""
        self.assertEqual(self.student.bio, "Votre bio")
        self.assertTrue(self.student.status)
        self.assertIsNone(self.student.photo)

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Student
from quiz.models import Quiz
from school.models import Classe

class StudentModelTestCase(TestCase):

    def setUp(self):
        # Création d'un utilisateur
        self.user = User.objects.create_user(username='teststudent', password='password123')

        # Création d'une classe
        self.classe = Classe.objects.create(
            niveau_id=1,  # Assurez-vous qu'un niveau existe ou créez-en un avant
            numeroClasse=1
        )

        # Création d'un quiz
        self.quiz = Quiz.objects.create(
            name="Quiz Test",
            description="Description du quiz"
        )

        # Création d'un étudiant
        self.student = Student.objects.create(
            user=self.user,
            classe=self.classe,
            ville="Yamoussoukro",
            score=10
        )

    def test_student_instance_creation(self):
        """Test de création d'une instance Student"""
        self.assertEqual(self.student.user.username, "teststudent")
        self.assertEqual(self.student.classe, self.classe)
        self.assertEqual(self.student.ville, "Yamoussoukro")
        self.assertEqual(self.student.score, 10)

    def test_slug_generation(self):
        """Test de la génération automatique du slug"""
        self.assertIsNotNone(self.student.slug)
        self.assertTrue(self.student.slug.startswith("teststudent-"))

    def test_get_u_type(self):
        """Test de la méthode get_u_type"""
        self.assertTrue(self.student.get_u_type)

    def test_get_unanswered_questions(self):
        """Test de la méthode get_unanswered_questions"""
        # Ajouter une question au quiz
        question = self.quiz.questions.create(text="Quelle est la capitale ?", order=1)

        # Vérifier les questions non répondues
        unanswered_questions = self.student.get_unanswered_questions(self.quiz)
        self.assertEqual(unanswered_questions.count(), 1)
        self.assertEqual(unanswered_questions.first(), question)

    def test_get_successful_quizzes_count(self):
        """Test de la méthode get_successful_quizzes_count"""
        # Simuler la réussite d'un quiz
        taken_quiz = self.student.quizzes.through.objects.create(
            student=self.student,
            quiz=self.quiz,
            percentage=80  # Pourcentage de réussite
        )
        successful_quizzes_count = self.student.get_successful_quizzes_count()
        self.assertEqual(successful_quizzes_count, 1)

    def test_default_values(self):
        """Test des valeurs par défaut"""
        self.assertEqual(self.student.bio, "Votre bio")
        self.assertTrue(self.student.status)
        self.assertIsNone(self.student.photo)

