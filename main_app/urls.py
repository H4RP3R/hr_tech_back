from django.urls import path

from main_app.views import QuestionList, QuestionDetail, QuestionnaireList, QuestionnaireDetail, \
    ProfileList, ProfileDetail, current_user_data, QuestionStatsList, QuestionStatsDetail, \
    PollResultsList, PollsResultsDetail, QuestionInPollStatsList, QuestionInPollStatsDetail, \
    UserList, pollResultsListByUserId, PublishedQuestionnaireList

urlpatterns = [
    path('api/questions/', QuestionList.as_view(), name='question_list'),
    path('api/questions/<int:pk>', QuestionDetail.as_view(), name='question_detail'),

    path('api/questionnaire/', QuestionnaireList.as_view(), name='questionnaire_list'),
    path('api/questionnaire/<int:pk>', QuestionnaireDetail.as_view(), name='questionnaire_detail'),
    path('api/published_questionnaire/',
         PublishedQuestionnaireList.as_view(), name='published_questionnaire'),

    path('api/profiles/', ProfileList.as_view(), name='profile_list'),
    path('api/profiles/<int:pk>/', ProfileDetail.as_view(), name='profile_detail'),

    path('api/current_user_data/', current_user_data, name='current_user_data'),
    path('api/user_list/', UserList.as_view(), name='user_list'),

    # _____________________________ Stats _______________________________________
    path('api/question_stats/', QuestionStatsList.as_view(), name='question_stats'),
    path('api/question_stats/<int:pk>', QuestionStatsDetail.as_view(), name='question_stats_detail'),
    path('api/poll_results/', PollResultsList.as_view(), name='poll_results_list'),
    path('api/poll_results/<int:pk>', PollsResultsDetail.as_view(), name='poll_results_detail'),
    path('api/question_in_poll_stats/', QuestionInPollStatsList.as_view(),
         name='question_in_poll_stats'),
    path('api/question_in_poll_stats/<int:pk>', QuestionInPollStatsDetail.as_view(),
         name='question_in_poll_detail'),
    path('api/poll_results_for_user/<int:pk>', pollResultsListByUserId, name='poll_results_by_id')
]
