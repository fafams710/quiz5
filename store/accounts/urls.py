from django.urls import path
from .views import GetUsers, GetUser, UserProfile
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('users/', GetUsers.as_view(), name='user-list'),
    path('users/<int:pk>/', GetUser.as_view(), name='user-detail'),
    path('me/', UserProfile.as_view(), name='user-profile'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
