from rest_framework import serializers
from django.apps import apps
from items.serializers import ItemSerializer

class RecipientSerializer(serializers.ModelSerializer):

    class Meta:
        model = apps.get_model('recipients.Recipient')
        fields = '__all__'

class RecipientDetailSerializer(RecipientSerializer):
    items = ItemSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.list = validated_data.get('list', instance.list)
        instance.unique_code = validated_data.get('unique_code', instance.unique_code)
        instance.save()
        return instance