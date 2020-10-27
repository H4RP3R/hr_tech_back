from django.db import models
from django.core.validators import validate_comma_separated_integer_list
from django.contrib.auth.models import User
from django.db.utils import OperationalError


class QuestionFOurAnswers(models.Model):
    '''
    Basic set of answer options
    '''
    answer1 = models.CharField(max_length=250, blank=False)
    answer2 = models.CharField(max_length=250, blank=False)
    answer3 = models.CharField(max_length=250, blank=False)
    answer4 = models.CharField(max_length=250, blank=False)
    has_correct_answer = models.BooleanField()
    correct_answers = models.CharField(
        validators=[validate_comma_separated_integer_list], max_length=100, blank=True)

    class Meta:
        abstract = True


class Question(QuestionFOurAnswers):
    text = models.TextField()
    score = models.IntegerField(default=0)

    def __str__(self):
        return f'Question id: {self.id} | text: {self.text[:20]}'


class Questionnaire(models.Model):
    title = models.CharField(max_length=250, unique=True)
    questions = models.ManyToManyField(Question, blank=True)

    def __str__(self):
        return f'Questionnaire id: {self.id} | title: {self.title}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    is_hr_staff = models.BooleanField(default=False)

    def __str__(self):
        status = 'Staff' if self.is_hr_staff else 'User'
        return f'{status} {self.user.username} <id:{self.user.id}>'


class QuestionStats(models.Model):
    question = models.OneToOneField('Question', primary_key=True, on_delete=models.DO_NOTHING)
    total_replies = models.PositiveIntegerField(default=0)
    correct = models.PositiveIntegerField(default=0)
    var_1_repl = models.PositiveIntegerField(default=0)
    var_2_repl = models.PositiveIntegerField(default=0)
    var_3_repl = models.PositiveIntegerField(default=0)
    var_4_repl = models.PositiveIntegerField(default=0)


class QuestionInPollStats(models.Model):
    poll = models.ForeignKey('Questionnaire', on_delete=models.DO_NOTHING)
    question = models.ForeignKey('Question', on_delete=models.DO_NOTHING)
    total_replies = models.PositiveIntegerField(default=0)
    correct = models.PositiveIntegerField(default=0)
    var_1_repl = models.PositiveIntegerField(default=0)
    var_2_repl = models.PositiveIntegerField(default=0)
    var_3_repl = models.PositiveIntegerField(default=0)
    var_4_repl = models.PositiveIntegerField(default=0)


class PollResults(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.DO_NOTHING)
    answers = models.JSONField()
    results = models.JSONField()

    class Meta:
        unique_together = ('user', 'questionnaire')


class TotalPollStats(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.DO_NOTHING)
    total_replies = models.PositiveIntegerField(default=0)
