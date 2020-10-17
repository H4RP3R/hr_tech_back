from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from main_app.models import Question, Questionnaire, Profile, User
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


@api_view()
@permission_classes([permissions.IsAuthenticated])
def current_user_data(request):
    user = User.objects.get(id=request.user.id)
    data = {
        'id': user.id,
        'username': user.username,
        'is_hr_staff': user.profile.is_hr_staff,
    }
    return Response(data)
