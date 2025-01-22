from rest_framework import serializers
from django.apps import apps

class ItemSerializer(serializers.ModelSerializer):
    recipient = serializers.ReadOnlyField(source='recipients.id')

    class Meta:
        model = apps.get_model('items.Item')
        fields = '__all__'