from django.urls import path, include
from django.contrib import admin  # Add this import
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),  # Add this line
    path('api-auth/', include('rest_framework.urls')),
    path('api/tasks/', include('todo.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenObtainPairView.as_view(), name='token_refresh'),
]