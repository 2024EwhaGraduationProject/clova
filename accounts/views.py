from django.shortcuts import render
from django.core.mail import EmailMessage
from rest_framework import views, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import UserLoginSerializer, UserSerializer

# Create your views here.
class LoginView(views.APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            return Response({"message":'로그인 성공',"data":serializer.validated_data}, status=status.HTTP_200_OK)
        return Response({"message":'로그인 실패',"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class SignupView(APIView):
    serializer = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message":'회원가입 성공',"data":serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message":'회원가입 실패',"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

import random

def genCode(length=4):
    return ''.join(random.choices('0123456789', k=length))

class SignupCodeView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data['email']+"@ewha.ac.kr"

        if email=="@ewha.ac.kr":
            return Response({'error': '이메일이 입력되지 않았습니다.'}, status=400)
        
        verificationCode = genCode()

        subject = "[c.lova] 인증코드를 안내해드립니다."
        to = [email]
        message = f"""
        안녕하세요,
        c.lova입니다.

        회원가입을 위한 인증코드를 안내해드립니다.

        "
        {verificationCode}
        "

        인증코드를 요청하지 않았다면 2024clova@gmail.com로 문의 부탁드립니다.
        c.lova와 함께해주셔서 감사합니다.


        < 클로바 드림 >
        2024clova@gmail.com
        """

        EmailMessage(subject=subject, body=message, to=to).send()
        return Response({'verificationCode': verificationCode}, status=201)