from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.http import Http404
from .models import List
from .serializers import ListSerializer, ListDetailSerializer, RecipientSerializer
from .permissions import IsCreatorOrSuperuserOrAdmin

class ListList(APIView):
    
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, 
        IsCreatorOrSuperuserOrAdmin
    ]

    def get(self, request):
        # If the user is not authenticated return 401
        if not request.user.is_authenticated:
            return Response(
                {"detail": "Authentication required."}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        # If the user is authenticated and superuser, return all lists
        if request.user.is_superuser or request.user.is_staff:
            lists = List.objects.all()
        # If the user is authenticated, return all lists they own
        else: 
            lists = List.objects.filter(owner=request.user)

        serializer = ListSerializer(lists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ListDetail(APIView):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsCreatorOrSuperuserOrAdmin
    ]

    def get_object(self, pk):
        try:
            list = List.objects.get(pk=pk)
            self.check_object_permissions(self.request, list)
            return list
        except List.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        list = self.get_object(pk)
        serializer = ListDetailSerializer(list)
        return Response(serializer.data)

    def put(self, request, pk):
        list = self.get_object(pk)
        serializer = ListDetailSerializer(
            instance=list,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def delete(self, request, pk, format=None):
        list = self.get_object(pk)
        list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)