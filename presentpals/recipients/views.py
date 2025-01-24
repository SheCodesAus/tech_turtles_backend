from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Recipient
from .serializers import RecipientSerializer, RecipientDetailSerializer

class RecipientList(APIView):

    def get(self, request):
        recipients = Recipient.objects.all()
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
    def get_object(self, pk):
        try:
            recipient = Recipient.objects.get(pk=pk)
            return recipient
        except Recipient.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        recipient = self.get_object(pk)
        serializer = RecipientDetailSerializer(recipient)
        return Response(serializer.data)