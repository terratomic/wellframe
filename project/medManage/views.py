# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django import forms
from medManage.models import Medication, Patient
from medManage.serializers import MedicationSerializer, PatientSerializer
from rest_framework import viewsets
from rest_framework.response import Response



class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer



class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientMedication(viewsets.ViewSet):

    serializer_class = MedicationSerializer

    def list(self, request, *args, **kwargs):
        if('patient_id_pk' in kwargs):
            patient_id = kwargs['patient_id_pk']
            # patient = Patient.objects.get(pk=patient_id)
            patient = get_object_or_404(Patient, pk=patient_id)
            serializer = self.serializer_class(patient.medications.all(), many=True)
            return Response(serializer.data)
        else:
            return Response(status=400)

    def create(self, request, *args, **kwargs):

        if('patient_id_pk' in kwargs and 'id' in request.data):
            patient_id = kwargs['patient_id_pk']
            med_id = request.data['id']
            patient = get_object_or_404(Patient, pk=patient_id)
            med_add = get_object_or_404(Medication, id=med_id)
            patient.medications.add(med_add)
            return Response(status=204)
        else:
            return Response(status=400)

    def destroy(self, request, *args, **kwargs):

        if('patient_id_pk' in kwargs):
            patient_id = kwargs['patient_id_pk']
            med_id = kwargs['pk']
            patient = get_object_or_404(Patient, pk=patient_id)
            med_delete = get_object_or_404(Medication, id=med_id)
            patient.medications.remove(med_delete)
            return Response(status=204)
        else:
            return Response(status=400)


#
# class PatientMedication(forms.Form):
#     med = forms.ModelChoiceField(queryset = Medication.objects.all())
#
#     def get_queryset(self):
#         # if('patient_id_pk' in self.kwargs):
#         return Patient.objects.get(id=self.kwargs['patient_id_pk']).medications
#         # return Medication.objects.all()
#
#     def create(self, request,*args, **kwargs):
#         if('patient_id_pk' in self.kwargs):
#
#             if(request.method=='POST'):
#                 form = addPatientMedication(request.POST)
#             med = form.cleaned_data['med']
#
#             if(form.is_valid()):
#                 Patient.objects.get(id=self.kwargs['patient_id_pk']).medications.add(form.cleaned_data['medication'])
#             return Response(status=204)
#         else:
#             return Response(status=500)
#
#     def destroy(self, request, *args, **kwargs):
#
#         if('patient_id_pk' in kwargs):
#             patient_id = self.kwargs['patient_id_pk']
#             med_id = self.kwargs['pk']
#             medications = Patient.objects.get(id=patient_id).medications
#             med_delete = medications.get(id=med_id)
#             medications.remove(med_delete)

# class PatientMedicationViewSet(viewsets.ModelViewSet):
#
#     serializer_class = PatientSerializer

    # def get_queryset(self):
    #     patient_id = self.kwargs['patient_id']
    #     return Patient.objects.filter(pk=patient_id)
    #
    # def update(self):
    #     adding_med = Medication.create("Advil99")
    #     queryset.medications.add(adding_med)
    #
    # def delete(self):
    #     med_id = self.kwargs['med_id']
    #     queryset = get_queryset().medications
    #
    #     for med in queryset:
    #         if med.id == med_id:
    #             med.delete()
    #             return
