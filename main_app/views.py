from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from django.db.models import F

from main_app.models import Question, Questionnaire, Profile, User, QuestionStats, PollResults, \
    QuestionInPollStats
from main_app.serializers import QuestionSerializer, QuestionnaireSerializer, ProfileSerializer, \
    QuestionStatsSerializer, PollResultsSerializer, QuestionInPollStatsSerializer, UserSerializer
from main_app.permissions import IsHrStaff


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsHrStaff]


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated, IsHrStaff]


class QuestionnaireList(generics.ListCreateAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionnaireDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    permission_classes = [permissions.IsAuthenticated]


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


class QuestionStatsList(generics.ListAPIView):
    queryset = QuestionStats.objects.all()
    serializer_class = QuestionStatsSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionStatsDetail(generics.RetrieveUpdateAPIView):
    queryset = QuestionStats.objects.all()
    serializer_class = QuestionStatsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = QuestionStatsSerializer(queryset, many=True)
        question_stats, _ = QuestionStats.objects.get_or_create(
            question=Question.objects.get(pk=request.data['question']))
        question_stats.total_replies = F('total_replies') + 1
        question_stats.correct = F('correct') + request.data['correct']
        question_stats.var_1_repl = F('var_1_repl') + request.data['var_1_repl']
        question_stats.var_2_repl = F('var_2_repl') + request.data['var_2_repl']
        question_stats.var_3_repl = F('var_3_repl') + request.data['var_3_repl']
        question_stats.var_4_repl = F('var_4_repl') + request.data['var_4_repl']
        question_stats.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class PollResultsList(generics.ListCreateAPIView):
    queryset = PollResults.objects.all()
    serializer_class = PollResultsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        user = User.objects.get(pk=request.data['user'])
        questionnaire = Questionnaire.objects.get(pk=request.data['questionnaire'])

        results = PollResults.objects.create(
            user=user,
            questionnaire=questionnaire,
            answers=request.data['answers'],
            results=request.data['results'])
        results.save()

        serializer = PollResultsSerializer(results)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PollsResultsDetail(generics.RetrieveAPIView):
    queryset = PollResults.objects.all()
    serializer_class = PollResultsSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionInPollStatsList(generics.ListAPIView):
    queryset = QuestionInPollStats.objects.all()
    serializer_class = QuestionInPollStatsSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionInPollStatsDetail(generics.RetrieveUpdateAPIView):
    queryset = QuestionInPollStats.objects.all()
    serializer_class = QuestionInPollStatsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = QuestionInPollStatsSerializer(queryset, many=True)
        question_stats, _ = QuestionInPollStats.objects.get_or_create(
            question=Question.objects.get(pk=request.data['question']),
            poll=Questionnaire.objects.get(pk=request.data['poll']))
        question_stats.total_replies = F('total_replies') + 1
        question_stats.correct = F('correct') + request.data['correct']
        question_stats.var_1_repl = F('var_1_repl') + request.data['var_1_repl']
        question_stats.var_2_repl = F('var_2_repl') + request.data['var_2_repl']
        question_stats.var_3_repl = F('var_3_repl') + request.data['var_3_repl']
        question_stats.var_4_repl = F('var_4_repl') + request.data['var_4_repl']
        question_stats.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view()
@permission_classes([permissions.IsAuthenticated])
def pollResultsListByUserId(request, pk):
    user = User.objects.get(pk=pk)
    queryset = PollResults.objects.filter(user=user)
    serializer = PollResultsSerializer(queryset, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
