from rest_framework import serializers
from django.apps import apps

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = apps.get_model('items.Item')
        fields = '__all__'

class ItemDetailSerializer(ItemSerializer):

    def validate(self, data):
        recipient_id = data.get('recipient')
        recipient_list_id = recipient_id.list
        request_user = self.context['request'].user

        # Ensure the list's owner matches the authenticated user
        if recipient_list_id.owner != request_user:
            raise serializers.ValidationError("You do not own this list associated with this recipient id.")

        return data

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