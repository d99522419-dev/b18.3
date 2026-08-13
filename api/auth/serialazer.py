from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password



from rest_framework import serializers
from rest_framework.authtoken.models import Token

from phonenumber_field.serializerfields import PhoneNumberField
from accounts.models import User


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, attrs):
        print(attrs)
        user = authenticate(email=attrs.get('email'), password=attrs.get('password'))       
        if not user:
            raise serializers.ValidationError("Invalid email or password.")
        
        token,_ = Token.objects.get_or_create(user=user)
        return {"token": token.key,"email": user.email}



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,validators=[validate_password])
    password2 = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('email','first_name','avatar','last_name','phone_number','date_of_birth', 'password', 'password2')
    
    def validate(self, attrs):
        if not attrs['password'] == attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create(**validated_data)
        Token.objects.create(user=user)
        return validated_data

class ProfileSeriaalizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "phone_number","first_name","last_name","avatar","date_of_birth")
        readonly_fields = ("email")

class SendOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()

class VerifyOTPSerializer(serializers.Serializer):
        email = serializers.EmailField()
        code = serializers.CharField(max_length=6, min_length=6)

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp_code = serializers.CharField(max_length=6, min_length=6)
    new_password = serializers.CharField(min_length=8)
