from django.urls import path

from main_app.views import QuestionList, QuestionDetail, QuestionnaireList, QuestionnaireDetail, \
    ProfileList, ProfileDetail, current_user_data, QuestionStatsList, QuestionStatsDetail, \
    PollResultsList, PollsResultsDetail, QuestionInPollStatsList, QuestionInPollStatsDetail, \
    UserList, pollResultsListByUserId, PublishedQuestionnaireList

urlpatterns = [
    path('questions/', QuestionList.as_view(), name='question_list'),
    path('questions/<int:pk>', QuestionDetail.as_view(), name='question_detail'),

    path('questionnaire/', QuestionnaireList.as_view(), name='questionnaire_list'),
    path('questionnaire/<int:pk>', QuestionnaireDetail.as_view(), name='questionnaire_detail'),
    path('published_questionnaire/',
         PublishedQuestionnaireList.as_view(), name='published_questionnaire'),

    path('profiles/', ProfileList.as_view(), name='profile_list'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile_detail'),

    path('current_user_data/', current_user_data, name='current_user_data'),
    path('user_list/', UserList.as_view(), name='user_list'),

    # _____________________________ Stats _______________________________________
    path('question_stats/', QuestionStatsList.as_view(), name='question_stats'),
    path('question_stats/<int:pk>', QuestionStatsDetail.as_view(), name='question_stats_detail'),
    path('poll_results/', PollResultsList.as_view(), name='poll_results_list'),
    path('poll_results/<int:pk>', PollsResultsDetail.as_view(), name='poll_results_detail'),
    path('question_in_poll_stats/', QuestionInPollStatsList.as_view(),
         name='question_in_poll_stats'),
    path('question_in_poll_stats/<int:pk>', QuestionInPollStatsDetail.as_view(),
         name='question_in_poll_detail'),
    path('poll_results_for_user/<int:pk>', pollResultsListByUserId, name='poll_results_by_id')
]
