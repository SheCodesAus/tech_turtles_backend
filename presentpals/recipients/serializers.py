from rest_framework import serializers
from django.apps import apps

class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('recipients.Recipient')
        fields = '__all__'