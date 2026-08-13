import random
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serialazer import SendOTPSerializer,VerifyOTPSerializer,ResetPasswordSerializer
from accounts.models import OTPCode
from django.utils import timezone
from datetime import timedelta



User = get_user_model()

otp_storage = {}
class SendOTPCodeView(APIView):
    def post(self, request):
        serializer = SendOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']

        OTPCode.objects.filter(email=email).delete()

        code = str(random.randint(100000, 999999))

        OTPCode.objects.create(
            email=email,
            code=code,
            expired_at=timezone.now() + timedelta(minutes=5)
        )

        send_mail(
            subject='Ваш код подтверждения APARTAMENT',
            message=f'Ваш код: {code}',
            from_email='hhabibullaevfirdavs@gmail.com',
            recipient_list=[email]
        )

        return Response({"message": "Код отправлен"})


class VerifyOTPView(APIView):
    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
         
    
class VerifyOTPCodeView(APIView):
    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        otp_code = serializer.validated_data['otp_code']
        stored_otp_code = otp_storage.get(email)

        if stored_otp_code is None:
            return Response({'error': 'No OTP code found for this email.'}, status=status.HTTP_400_BAD_REQUEST)

        if stored_otp_code != otp_code:
            return Response({'error': 'Invalid OTP code.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'OTP verified successfully.'}, status=status.HTTP_200_OK)
    
    
class ResetPasswordView(APIView):
    def post(self,request):
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        otp_code = serializer.validated_data['otp_code']
        new_password = serializer.validated_data['new_password']

        stored_otp_code = otp_storage.get(email)

        if stored_otp_code is None:
            return Response({'error': 'No OTP code found for this email.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)


        user.set_password(new_password)
        user.save()
        del otp_storage[email]
        return Response({'message': 'Password reset successfully.'}, status=status.HTTP_200_OK)



