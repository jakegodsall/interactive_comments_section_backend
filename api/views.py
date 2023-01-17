from rest_framework.viewsets import ModelViewSet

from api.models import ProfileImage, Profile, Message
from api.serializers import ProfileImageSerializer, ProfileSerializer, MessageSerializer


class ProfileImageViewSet(ModelViewSet):
    queryset = ProfileImage.objects.all()
    serializer_class = ProfileImageSerializer


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
