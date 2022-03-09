from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from employee.api import EmployeeApi, EmployeeCreateApi

urlpatterns = [
    path('admin/', admin.site.urls),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('employee/create',EmployeeCreateApi.as_view()),
    path('employee/list',EmployeeApi.as_view()),

   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)