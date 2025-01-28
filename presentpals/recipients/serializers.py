from rest_framework import serializers
from django.apps import apps
from items.serializers import ItemSerializer

class RecipientSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = apps.get_model('recipients.Recipient')
        fields = '__all__'

class RecipientDetailSerializer(RecipientSerializer):

    def validate(self, data):
        recipient_list = data.get('list')
        request_user = self.context['request'].user

        # Ensure the list's owner matches the authenticated user
        if recipient_list.owner != request_user:
            raise serializers.ValidationError("You do not own this list id.")

        return data

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.list = validated_data.get('list', instance.list)
        instance.unique_code = validated_data.get('unique_code', instance.unique_code)
        instance.save()
        return instance