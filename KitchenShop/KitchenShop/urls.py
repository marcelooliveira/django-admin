from django.contrib import admin
from django.urls import path
from urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('custom/', include('custom.urls'))
]
