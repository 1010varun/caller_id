from authapp.models import *
from authapp.serializers import *
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken



class MarkSpam(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response({'error': 'Phone number is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the phone number belongs to a registered user
        user, created = User.objects.get_or_create(phone_number=phone_number, defaults={'username': 'Unknown'})

        user.mark_as_spam()

        return Response({'message': 'Number marked as spam'}, status=status.HTTP_200_OK)
    
class SearchByName(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, name):
        # Search registered users
        registered_users = User.objects.filter(username__icontains=name)

        results = []
        for user in registered_users:
            results.append({
                'name': user.username,
                'phone_number': user.phone_number,
                'is_spam': user.is_spam,
                'registered': user.is_registered
            })

        return Response(results, status=status.HTTP_200_OK)
    

class SearchByPhoneNumber(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, phone_number):
        try:
            user = User.objects.get(phone_number=phone_number)
            result = {
                'name': user.username,
                'phone_number': user.phone_number,
                'is_spam': user.is_spam,
            }
            return Response(result, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response([], status=status.HTTP_404_NOT_FOUND)
