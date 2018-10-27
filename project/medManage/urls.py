from django.urls import path, include
from . import views
from medManage.views import MedicationViewSet, PatientViewSet, PatientMedication
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

# class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
#     pass



router = routers.SimpleRouter(trailing_slash=False)
router.register(r'medications', MedicationViewSet)
router.register(r'patients',PatientViewSet)
# router.register(r'patients/(?P<patient_id>.+)/medications',PatientMedicationViewSet, basename='patients')
# router.register(r'patients/(?P<patient_id>.+)/medications',PatientViewSet)
patients_router = routers.NestedSimpleRouter(router, r'patients',lookup='patient_id')
patients_router.register('medications', PatientMedication, base_name='patients-medications')

urlpatterns = [
    path(r'api/', include(router.urls)),
    path(r'api/', include(patients_router.urls)),
]
