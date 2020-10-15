from django.urls import path

from main_app.views import QuestionList, QuestionDetail, QuestionnaireList, QuestionnaireDetail, \
    ProfileList, ProfileDetail


urlpatterns = [
    path('questions/', QuestionList.as_view(), name='question_list'),
    path('question/<int:pk>', QuestionList.as_view(), name='question_detail'),
    path('questionnaire/', QuestionnaireList.as_view(), name='questionnaire_list'),
    path('questionnaire/<int:pk>', QuestionnaireDetail.as_view(), name='questionnaire_detail'),
    path('profiles/', ProfileList.as_view(), name='profile_list'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile_detail'),
]
