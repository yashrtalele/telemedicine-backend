from django.urls import path
from .views import DoctorsView, GetDoctor, CreateDoctor, UpdateDoctor, DeleteDoctor

urlpatterns = [
    path('', DoctorsView.as_view(), name="doctors"),
    path('<id>', GetDoctor.as_view(), name="doctor"),
    path('create/', CreateDoctor.as_view(), name="create_doctor"),
    path('update/', UpdateDoctor.as_view(), name="update_doctor"),
    path('delete/', DeleteDoctor.as_view(), name="delete_doctor")
]