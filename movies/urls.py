from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),  # DRF's browsable API login/logout
    path('', include('reviews.urls')),  # Reviews routes (ViewSet)
    path('auth/', TokenObtainPairView.as_view(), name='auth'),    
]
