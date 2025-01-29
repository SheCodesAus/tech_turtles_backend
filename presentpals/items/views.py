from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.http import Http404
from .models import Item
from .serializers import ItemSerializer, ItemDetailSerializer
from .permissions import IsCreatorOrSuperuser

class ItemList(APIView):
    
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
            items = Item.objects.all()
        else: 
            items = Item.objects.filter(recipient__list__owner=request.user)
        
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
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

class ItemDetail(APIView):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsCreatorOrSuperuser
    ]

    def get_object(self, pk):
        try:
            item = Item.objects.get(pk=pk)
            self.check_object_permissions(self.request, item)
            return item
        except Item.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        item = self.get_object(pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk):
        item = self.get_object(pk)
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
    
    def delete(self, request, pk, format=None):
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
