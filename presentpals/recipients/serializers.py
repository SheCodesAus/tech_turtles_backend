from rest_framework import serializers
from django.apps import apps
from items.serializers import ItemSerializer

class RecipientSerializer(serializers.ModelSerializer):

    class Meta:
        model = apps.get_model('recipients.Recipient')
        fields = '__all__'

class RecipientDetailSerializer(RecipientSerializer):
    items = ItemSerializer(many=True, read_only=True)