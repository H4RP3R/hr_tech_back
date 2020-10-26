import json

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework import status

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from main_app.models import Question
from main_app.serializers import QuestionSerializer


class AuthorizedTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='test_staff', password='uL0eiZohmeif8boo')
        user = User.objects.get(username='test_staff')
        user.profile.is_hr_staff = True
        user.profile.save()
        token = Token.objects.get(user=user)
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)


class GetAllQuestionsTest(AuthorizedTestCase):

    def setUp(self):
        super().setUp()

        Question.objects.create(
            text='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor...',
            answer1='answer1',
            answer2='answer2',
            answer3='answer3',
            answer4='answer4',
            has_correct_answer=True,
            correct_answers='1,2',
            score=5,
        )
        Question.objects.create(
            text='Common tunny dartfish eulachon, California flyingfish harelip sucker four-eyed.',
            answer1='answer1',
            answer2='answer2',
            answer3='answer3',
            answer4='answer4',
            has_correct_answer=False,
            correct_answers='',
            score=0,
        )

    def test_get_all_questions(self):
        response = self.client.get(reverse('question_list'))
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleQuestion(AuthorizedTestCase):

    def setUp(self):
        super().setUp()

        self.question_1 = Question.objects.create(
            text='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor...',
            answer1='answer1',
            answer2='answer2',
            answer3='answer3',
            answer4='answer4',
            has_correct_answer=True,
            correct_answers='1,2',
            score=5,
        )
        self.question_2 = Question.objects.create(
            text='Common tunny dartfish eulachon, California flyingfish harelip sucker four-eyed.',
            answer1='answer1',
            answer2='answer2',
            answer3='answer3',
            answer4='answer4',
            has_correct_answer=False,
            correct_answers='',
            score=0,
        )

    def test_get_valid_single_question(self):
        response = self.client.get(
            reverse('question_detail', kwargs={'pk': self.question_2.pk}))
        question = Question.objects.get(pk=self.question_2.pk)
        serializer = QuestionSerializer(question)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_question(self):
        response = self.client.get(reverse('questionnaire_detail', kwargs={'pk': 666}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
