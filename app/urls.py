from django.contrib import admin
from django.urls import path, include
# import package yang dibutuhkan untuk dokumentasi API
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# pengaturan untuk dokumentasi API (judul, deskripsi dll)
schema_view = get_schema_view(
    openapi.Info(
        title="News App API",
        default_version='v1',
        description="An api for News App",
        terms_of_service="/terms/",
        contact=openapi.Contact(email="sakukode@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
	# routing untuk Rest API
	path('api/', include('news.urls')),
    # routing untuk Admin
    path('admin/', admin.site.urls),
    # dokumentasi API dengan Swagger
    path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),
    # dokumentasi API dengan Redoc
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
]