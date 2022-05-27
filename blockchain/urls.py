from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import CreateFileHashBlockchain, UploadView

urlpatterns = [
    path('create/', CreateFileHashBlockchain.as_view(), name="create_file_hash"),
    path('upload/', UploadView.as_view(), name="file_upload")
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    