from rest_framework import serializers
from main_app.models import Question, Questionnaire, Profile, User, QuestionStats, PollResults, \
    QuestionInPollStats


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ['id', 'title', 'questions']

    def to_representation(self, instance):
        questions = [QuestionSerializer(q).data for q in instance.questions.all()]
        return {
            'id': instance.id,
            'title': instance.title,
            'questions': questions,
        }

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.questions.set(validated_data.get('questions', instance.questions))
        instance.save()
        return instance


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        extra_kwargs = {'password': {'write_only': True}}
        fields = '__all__'


class QuestionStatsSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True)

    class Meta:
        model = QuestionStats
        fields = '__all__'


class PollResultsSerializer(serializers.ModelSerializer):
    questionnaire = QuestionnaireSerializer()
    user = UserSerializer()

    class Meta:
        model = PollResults
        fields = ['questionnaire', 'user']


class QuestionInPollStatsSerializer(serializers.ModelSerializer):
    poll = QuestionnaireSerializer(read_only=True)
    question = QuestionSerializer(read_only=True)

    class Meta:
        model = QuestionInPollStats
        fields = '__all__'
