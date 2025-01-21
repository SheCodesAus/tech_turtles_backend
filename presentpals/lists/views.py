from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import List
from .serializers import ListSerializer, ListDetailSerializer, RecipientSerializer

class ListList(APIView):
    def get(self, request):
        lists = List.objects.all()
        serializer = ListSerializer(lists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ListSerializer(data=request.data)
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

class ListDetail(APIView):
    def get_object(self, pk):
        try:
            list = List.objects.get(pk=pk)
            return list
        except List.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        list = self.get_object(pk)
        serializer = ListDetailSerializer(list)
        return Response(serializer.data)