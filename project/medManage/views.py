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

"""
PatientMedication
Handles API calls related to editing a patient's medications
Supports GET, POST, and DELETE
"""

class PatientMedication(viewsets.ViewSet):

    serializer_class = MedicationSerializer

    def list(self, request, *args, **kwargs):
        if('patient_id_pk' in kwargs):
            patient_id = kwargs['patient_id_pk']
            patient = get_object_or_404(Patient, pk=patient_id)
            serializer = self.serializer_class(patient.medications.all(), many=True)
            return Response(serializer.data)
        else:
            return Response(status=400)

    def create(self, request, *args, **kwargs):

        if('patient_id_pk' in kwargs and 'ids' in request.data):
            patient_id = kwargs['patient_id_pk']
            patient = get_object_or_404(Patient, pk=patient_id)
            meds = request.data['ids']
            for med_id in meds:
                med_add = get_object_or_404(Medication, pk=med_id)
                patient.medications.add(med_add)
            return Response(status=204)
        else:
            return Response(status=400)

    def destroy(self, request, *args, **kwargs):

        if('patient_id_pk' in kwargs):
            med_id = kwargs['pk']
            med_delete = get_object_or_404(Medication, pk=med_id)
            patient_id = kwargs['patient_id_pk']
            patient = get_object_or_404(Patient, pk=patient_id)
            patient.medications.remove(med_delete)
            return Response(status=204)
        else:
            return Response(status=400)
