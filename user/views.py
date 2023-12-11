from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User,PasswordReset
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime,random,string
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from rest_framework import exceptions
# from rest_framework.exceptions import APIException

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PasswordReset, User
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
import jwt
import datetime
import random
import string
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from rest_framework import exceptions
from rest_framework.exceptions import NotFound
class Register(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        
        verification_token = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12))

        
        PasswordReset.objects.create(email=request.data['email'], token=verification_token)

        
        send_mail(
            subject="Verify your email",
            message=f'Click the following link to verify your email: http://localhost:3000/login/{verification_token}',
            from_email='yasnapolyanaa123@gmail.com', 
            recipient_list=[request.data['email']]
        )

        return Response({
            'message': 'User registered. Please check your email for verification.'
        })


class EmailVerification(APIView):
    def get(self, request, token):
        
        password_reset = get_object_or_404(PasswordReset, token=token)

        
        user = User.objects.filter(email=password_reset.email).first()
        if user:
            user.email_verified = True  
            user.save()

            
            password_reset.delete()

            return Response({'message': 'Email verified successfully.'}, status=status.HTTP_200_OK)
        else:
            raise NotFound("User not found")
class Login(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed("User not found")

        if not user.email_verified:
            raise AuthenticationFailed("Email not verified. Please verify your email.")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password")

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=720),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response_data = {
            'jwt': token
        }

        return Response(response_data)

class UserView(APIView):
    def get(self, request):
        auth_header = request.headers.get('Authorization')

        if not auth_header or not auth_header.startswith('Bearer '):
            raise AuthenticationFailed("Invalid Authorization header")

        token = auth_header.split(' ')[1]

        if not token:
            raise AuthenticationFailed("Unauthenticated")

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated")

        user = User.objects.filter(id=payload['id']).first()

        if not user:
            raise AuthenticationFailed("User not found")

        serializer = UserSerializer(user)
        return Response(serializer.data)
class Logout(APIView):
    def delete(self, request):
        auth_header = request.headers.get('Authorization')

        if not auth_header or not auth_header.startswith('Bearer '):
            raise AuthenticationFailed("Invalid Authorization header")

        token = auth_header.split(' ')[1]

        if not token:
            raise AuthenticationFailed("Invalid token in Authorization header")

        response = Response(data={'message': 'success'}, status=status.HTTP_200_OK)
        response.delete_cookie('jwt')  
        response.data = {
            'message': 'success'
        }
        return response

class ForgotPassword(APIView):
    def post(self,request):
        from_email = 'yasnapolyanaa123@gmail.com'
        email=request.data['email']
        token=''.join(random.choice(string.ascii_uppercase + string.digits)for _ in range(12))
        PasswordReset.objects.create(email=email,token=token)
        send_mail(
            subject="Reset your password",
            message='Clik <a href="http://localhost:3000/pswrd-reset/'+ token + '"> here</a> to reset your password or click <a href="https://steady-tapioca-8e39f4.netlify.app/pswrd-reset/'+ token + '"> here</a> ',
            from_email=from_email,
            recipient_list=[email]
        )
        
        return Response({
            'message':'Please, check your email'
        })

class ResetPassword(APIView):
    def put(self,request):
        data=request.data

        if data['password'] != data['password_confirm']:
            raise exceptions.APIException('Passwords do not match')
        
        passwordReset=PasswordReset.objects.filter(token=data['token']).first()
        user=User.objects.filter(email=passwordReset.email).first()
        if not user:
            raise exceptions.NotFound("User not found")
        user.set_password(data['password'])
        user.save()

        return Response({
            "message":"success"
        })
