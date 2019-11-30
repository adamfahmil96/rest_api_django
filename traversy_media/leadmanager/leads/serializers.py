from rest_framework import serializers
from leads.models import Lead

# Lead Serializers
# Serializers digunakan untuk mapping data yang akan dikeluarkan pada saat pemanggilan API

class LeadSerializer(serializers.ModelSerializer):
    # yang di-overwrite adalah Meta, yang di-set adalah modelnya, dan field yang dikeluarkan adalah semua
    class Meta:
        model  = Lead
        fields = '__all__'