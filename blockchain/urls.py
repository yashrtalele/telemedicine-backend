from django.urls import path
from .views import CreateFileHashBlockchain

urlpatterns = [
    path('create/', CreateFileHashBlockchain.as_view(), name="create_file_hash"),
]