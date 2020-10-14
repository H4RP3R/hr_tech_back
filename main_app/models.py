from django.db import models
from django.core.validators import validate_comma_separated_integer_list
from django.contrib.auth.models import User
from django.db.utils import OperationalError


class QuestionFOurAnswers(models.Model):
    '''
    Basic set of answer options
    '''
    answer1 = models.CharField(max_length=250, blank=False, default='')
    answer2 = models.CharField(max_length=250, blank=False, default='')
    answer3 = models.CharField(max_length=250, blank=False, default='')
    answer4 = models.CharField(max_length=250, blank=False, default='')
    has_correct_answer = models.BooleanField()
    correct_answers = models.CharField(
        validators=[validate_comma_separated_integer_list], max_length=100)

    class Meta:
        abstract = True


class Question(QuestionFOurAnswers):
    text = models.TextField()
    score = models.IntegerField(default=0)

    def __str__(self):
        return f'Question id: {self.id} | text: {self.text[:20]}'


class Questionnaire(models.Model):
    try:
        all_questions = Question.objects.all()
        QUESTION_CHOICES = [(q, q.id) for q in all_questions]
    except:
        QUESTION_CHOICES = []

    title = models.CharField(max_length=250, unique=True)
    questions = models.ManyToManyField(Question, choices=QUESTION_CHOICES, blank=True)

    def __str__(self):
        return f'Questionnaire id: {self.id} | questions: {len(self.questions)}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_hr_staff = models.BooleanField(default=False)

    def __str__(self):
        status = 'Staff' if self.is_hr_staff else 'User'
        return f'{status} {self.user.username} <id:{self.user.id}>'
