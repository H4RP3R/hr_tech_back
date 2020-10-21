from django.urls import path

from main_app.views import QuestionList, QuestionDetail, QuestionnaireList, QuestionnaireDetail, \
    ProfileList, ProfileDetail, current_user_data


urlpatterns = [
    path('questions/', QuestionList.as_view(), name='question_list'),
    path('questions/<int:pk>', QuestionDetail.as_view(), name='question_detail'),
    path('questionnaire/', QuestionnaireList.as_view(), name='questionnaire_list'),
    path('questionnaire/<int:pk>', QuestionnaireDetail.as_view(), name='questionnaire_detail'),
    path('profiles/', ProfileList.as_view(), name='profile_list'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile_detail'),
    path('current_user_data/', current_user_data, name='current_user_data'),
]
