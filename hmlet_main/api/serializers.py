from django.forms import widgets
from rest_framework import serializers
from scrape.models import Estate, Question


class EstateListSerializer(serializers.HyperlinkedModelSerializer):
    question_asked = serializers.CharField(read_only=True, source='question.question')
    
    class Meta:
        model = Estate
        view_name = 'estate-detail'
        fields = (
            'url',
            'question',
            'question_asked',
            'location',
            )
        

class EstateSerializer(serializers.HyperlinkedModelSerializer):
    question_asked = serializers.CharField(read_only=True, source='question.question')
    
    class Meta:
        model = Estate
        view_name = 'estate-detail'
        fields = (
            'url',
            'question',
            'question_asked',
            'rent',
            'area',
            'raw_text',
            'link',
            'ask_date',
            'source',
            'location',
            )
        

class QuestionListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        view_name = 'question-detail'
        fields = (
            'question',
            'url',
            'ask_date',
            )
        

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    # estate_set = serializers.HyperlinkedRelatedField(many=True,
    #                                                 read_only=True,
    #                                                 view_name='estate-detail')
    estate_set = EstateListSerializer(many=True)
    
    class Meta:
        model = Question
        view_name = 'question-detail'
        fields = ('question', 'estate_set',)
        
