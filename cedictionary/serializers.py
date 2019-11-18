from rest_framework import serializers
from .models import Entries

class CedictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entries
        fields = ['traditional', 'simplified', 'pinyin', 'english']

