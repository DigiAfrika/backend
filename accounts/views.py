from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

User = get_user_model()

class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
    
    def get_serializer(self, *args, **kwargs):
        from .serializers import UserSerializer
        return UserSerializer(*args, **kwargs)