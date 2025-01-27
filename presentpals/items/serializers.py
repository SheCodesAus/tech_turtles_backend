from rest_framework import serializers
from django.apps import apps

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = apps.get_model('items.Item')
        fields = '__all__'

class ItemDetailSerializer(ItemSerializer):

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.where_to_buy = validated_data.get('where_to_buy', instance.where_to_buy)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.status = validated_data.get('status', instance.status)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.recipient = validated_data.get('recipient', instance.recipient )
        instance.save()
        return instance