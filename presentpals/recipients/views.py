from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.http import Http404
from .models import Recipient
from .serializers import RecipientSerializer, RecipientDetailSerializer
from items.serializers import ItemSerializer, ItemDetailSerializer
from .permissions import IsCreatorOrSuperuser

class RecipientList(APIView):
    
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsCreatorOrSuperuser
    ]

    def get(self, request):
        if not request.user.is_authenticated:
            return Response(
                {"detail": "Authentication required."}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        if request.user.is_superuser:
            recipients = Recipient.objects.all()
        else: 
            recipients = Recipient.objects.filter(list__owner=request.user)
        
        serializer = RecipientSerializer(recipients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecipientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class RecipientDetail(APIView):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsCreatorOrSuperuser
    ]

    def get_object(self, pk):
        try:
            recipient = Recipient.objects.get(pk=pk)
            self.check_object_permissions(self.request, recipient)
            return recipient
        except Recipient.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        recipient = self.get_object(pk)
        serializer = RecipientDetailSerializer(recipient)
        return Response(serializer.data)

    def put(self, request, pk):
        recipient = self.get_object(pk)
        serializer = RecipientDetailSerializer(
            instance=recipient,
            data=request.data,
            partial=True,
            context={"request": request},
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk, format=None):
        recipient = self.get_object(pk)
        recipient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SharedRecipientDetail(APIView):

    def get_object(self, unique_code):
        try:
            recipient = Recipient.objects.get(unique_code=unique_code)
            self.check_object_permissions(self.request, recipient)
            return recipient
        except Recipient.DoesNotExist:
            raise Http404
    
    def get(self, request, unique_code):
        recipient = self.get_object(unique_code)
        serializer = RecipientDetailSerializer(recipient)
        return Response(serializer.data)

    def post(self, request, unique_code):
        recipient = self.get_object(unique_code)
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(recipient=recipient)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, unique_code, pk):
        recipient = self.get_object(unique_code)
        try:
            item = Item.objects.get(pk=pk, recipient=recipient)  # Ensure the item belongs to the recipient
        except Item.DoesNotExist:
            raise Http404
            
        serializer = ItemDetailSerializer(
            instance=item,
            data=request.data,
            partial=True,
            context={"request": request},
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, unique_code, pk):
        recipient = self.get_object(unique_code)
        try:
            item = Item.objects.get(pk=pk, recipient=recipient)  # Ensure the item belongs to the recipient
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Item.DoesNotExist:
            raise Http404