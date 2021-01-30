from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	# routing untuk Rest API
	path('api/', include('news.urls')),
    # routing untuk Admin
    path('admin/', admin.site.urls),
]