from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.http import Http404
from .models import List
from .serializers import ListSerializer, ListDetailSerializer, RecipientSerializer
from .permissions import IsOwnerOrReadOnly

class ListList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        lists = List.objects.all()
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
        IsOwnerOrReadOnly
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