from rest_framework.routers import DefaultRouter

from api.views import ProfileImageViewSet, ProfileViewSet, MessageViewSet

router = DefaultRouter()
router.register('profile-images', ProfileImageViewSet, basename='profileimage')
router.register('profile', ProfileViewSet, basename='profile')
router.register('message', MessageViewSet, basename='message')

urlpatterns = router.urls
