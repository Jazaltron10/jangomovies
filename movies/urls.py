from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "auth/", include("rest_framework.urls")
    ),  # DRF's browsable API login/logout
    # path('api/users/', include('users.urls')),  # Users routes (ViewSet)
    path('', include('reviews.urls')),  # Reviews routes (ViewSet)
    # path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
]
