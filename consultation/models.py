from django.db import models
from django.conf import settings

class Consultation(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=100)
    date = models.DateField()
    complaint = models.TextField()
    status = models.CharField(max_length=20, default='Menunggu')
    

    def __str__(self):
        return f"{self.patient.username} - {self.doctor_name}"

class MedicalRecord(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    consultation = models.ForeignKey('Consultation', on_delete=models.CASCADE, null=True, blank=True)
    diagnosis = models.TextField()
    treatment = models.TextField(blank=True, null=True)
    prescription = models.TextField(blank=True, null=True)
    doctor_note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rekam Medis {self.patient.username} - {self.created_at.strftime('%d %b %Y')}"
