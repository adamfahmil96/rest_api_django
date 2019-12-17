from rest_framework import serializers
from .models import Language

# Serializer digunakan untuk penanganan REST API secara 'shortcut'
class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'url', 'name', 'paradigm')