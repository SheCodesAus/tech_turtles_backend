from rest_framework import serializers
from django.apps import apps
from recipients.serializers import RecipientSerializer
from decimal import Decimal

class ListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    total_cost = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    
    class Meta:
        model = apps.get_model('lists.List')
        fields = '__all__'

class ListDetailSerializer(ListSerializer):
    recipients = RecipientSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.budget = validated_data.get('budget', instance.budget)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance