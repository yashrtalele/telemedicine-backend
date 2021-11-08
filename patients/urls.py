from django.urls import path
from .views import PatientsView, GetPatient, CreatePatient, UpdatePatient, DeletePatient

urlpatterns = [
    path('', PatientsView.as_view(), name="doctors"),
    path('<id>', GetPatient.as_view(), name="doctor"),
    path('create/', CreatePatient.as_view(), name="create_doctor"),
    path('update/', UpdatePatient.as_view(), name="update_doctor"),
    path('delete/', DeletePatient.as_view(), name="delete_doctor")
]