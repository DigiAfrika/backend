from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'password', 'is_client', 'is_freelancer')

    def create(self, validated_data):
        is_client = validated_data.pop('is_client', False)
        is_freelancer = validated_data.pop('is_freelancer', False)
        user = super().create(validated_data)
        user.is_client = is_client
        user.is_freelancer = is_freelancer
        user.save()
        return user

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = User
        fields = ('id', 'email', 'is_client', 'is_freelancer') 