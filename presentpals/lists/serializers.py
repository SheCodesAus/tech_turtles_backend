from rest_framework import serializers
from django.apps import apps
from recipients.serializers import RecipientSerializer

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('lists.List')
        fields = '__all__'

class ListDetailSerializer(ListSerializer):
    recipients = RecipientSerializer(many=True, read_only=True)