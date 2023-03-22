from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import UserView, UserCreateView, UserConnectView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenRefreshView.as_view(), name='token_verify'),
    path('user/', UserView.as_view(), name='user'),
    path('user/connect/', UserConnectView.as_view(), name='connection'),
    path('user/create/', UserCreateView.as_view(), name='registration'),
]