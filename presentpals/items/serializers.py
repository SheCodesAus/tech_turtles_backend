from rest_framework import serializers
from django.apps import apps

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = apps.get_model('items.Item')
        fields = '__all__'

    def validate(self, data):
        recipient = data.get('recipient')
        request = self.context.get('request')
        is_shared_view = self.context.get('is_shared_view', False)
        
        # Skip validation for SharedRecipientDetail view
        if is_shared_view:
            return data
        
        if not request or not request.user:
            raise serializers.ValidationError("Authentication required.")
            
        if recipient.list.owner != request.user:
            raise serializers.ValidationError("You can only create items for recipients in lists you own.")
            
        return data

class ItemDetailSerializer(ItemSerializer):

    def validate(self, data):
        recipient = data.get('recipient')
        request_user = self.context['request'].user

        if recipient and recipient.list.owner != request_user:
            raise serializers.ValidationError("You do not own this list associated with this recipient id.")

        return data

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.where_to_buy = validated_data.get('where_to_buy', instance.where_to_buy)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.delivery_status = validated_data.get('delivery_status', instance.delivery_status)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.status = validated_data.get('status', instance.status)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.recipient = validated_data.get('recipient', instance.recipient)
        instance.save()
        return instance