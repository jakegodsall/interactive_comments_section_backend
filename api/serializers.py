from rest_framework.serializers import ModelSerializer

from api.models import ProfileImage, Profile, Message


class ProfileImageSerializer(ModelSerializer):
    model = ProfileImage
    fields = '__all__'


class ProfileSerializer(ModelSerializer):
    model = Profile
    fields = '__all__'


class MessageSerializer(ModelSerializer):
    model = Message
    fields = '__all__'
