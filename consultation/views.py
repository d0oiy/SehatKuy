from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Consultation
from .forms import ConsultationForm
from django.contrib import messages

@login_required
def consultation_list(request):
    consultations = Consultation.objects.filter(patient=request.user)
    return render(request, 'consultation/list.html', {'consultations': consultations})

@login_required
def consultation_create(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            consultation = form.save(commit=False)
            consultation.patient = request.user
            consultation.save()
            messages.success(request, "Konsultasi berhasil dikirim! Tunggu konfirmasi dari dokter.")
            return redirect('consultation_list')
    else:
        form = ConsultationForm()
    return render(request, 'consultation/create.html', {'form': form})

@login_required
def medical_record_list(request):
    records = MedicalRecord.objects.filter(patient=request.user).order_by('-created_at')
    return render(request, 'medical_record/list.html', {'records': records})
