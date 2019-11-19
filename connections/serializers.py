from rest_framework import serializers
from .models import Connection, Word, Language, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'location', 'birth_date']

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('english_name', 'iso_639_1_code', 'iso_639_2_code')


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = (
            'language', 
            'text', 
            'is_word', 
            'number_of_syllables', 
            'english_transcription_system', 
            'transcription', 
            'international_phonetic_alphabet',
        )

class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = (
            'user', 
            'query', 
            'result', 
            'phonetic_relationship', 
            'semantic_relationship', 
        )




