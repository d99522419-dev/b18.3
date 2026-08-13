from rest_framework.response import Response
from rest_framework.decorators import permission_classes, api_view
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import  IsAuthenticated, AllowAny


from accounts.models import User
from .serialazer import  LoginSerializer,RegisterSerializer

@api_view(["POST"])
@permission_classes(([AllowAny]))
def custom_login(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    return Response(serializer.validated_data, status=status.HTTP_201_CREATED)



@api_view(["POST"])
@permission_classes(([AllowAny]))
def custom_register(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


@api_view(['GET',"PUT","PATCH"])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    if request.method == 'GET':
        serializer = RegisterSerializer(user)
        return Response(serializer.data)
    
    elif request.method in ['PUT', 'PATCH']:
        serializer = RegisterSerializer(user, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_out(request):
    Token.objects.filter(user=request.user).delete

    return Response({"messages": "vi vishli iz servera"}, status=status.HTTP_200_OK)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deactivate_account(request):
    
    Token.objects.filter(user=request.user).delete
    request.user.is_active = False
    request.user.save()
    return Response({"messages": "vi dezactirovali accaunt"}, status=status.HTTP_200_OK)