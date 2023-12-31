from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from mainapp.views import TaskViewSet, TaskRetrieveUpdateDeleteView

schema_view = get_schema_view(
   openapi.Info(
      title="Task API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register('task', TaskViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/task/<int:pk>/', TaskRetrieveUpdateDeleteView.as_view(), name='task-retrieve-update-delete'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
