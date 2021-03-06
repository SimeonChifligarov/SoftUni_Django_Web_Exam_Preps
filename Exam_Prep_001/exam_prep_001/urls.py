from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from exam_prep_001 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('exam_prep_001.web.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
