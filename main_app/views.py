from rest_framework import generics, permissions

from main_app.models import Question, Questionnaire, Profile
from main_app.serializers import QuestionSerializer, QuestionnaireSerializer, ProfileSerializer
from main_app.permissions import IsHrStaff


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated, IsHrStaff]


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated, IsHrStaff]


class QuestionnaireList(generics.ListCreateAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    permission_classes = [permissions.IsAuthenticated, IsHrStaff]


class QuestionnaireDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    permission_classes = [permissions.IsAuthenticated, IsHrStaff]


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.filter(is_hr_staff=False)
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsHrStaff]


class ProfileDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
