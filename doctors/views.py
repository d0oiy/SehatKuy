from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Doctor
from .forms import DoctorForm

# 🧩 Fungsi pengecekan role admin
def is_admin(user):
    return user.is_superuser or getattr(user, 'role', None) == 'admin'


# 🩺 Dashboard Dokter
@login_required
def dashboard(request):
    return render(request, 'doctors/dashboard.html')


# 📋 Daftar Dokter (hanya bisa diakses oleh admin)
@login_required
@user_passes_test(is_admin)
def doctor_list(request):
    print("✅ Masuk ke doctor_list view")
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctor_list.html', {'doctors': doctors})


# ➕ Tambah Dokter
@login_required
@user_passes_test(is_admin)
def doctor_add(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'doctors/doctor_form.html', {
        'form': form,
        'title': 'Tambah Dokter'
    })


# ✏️ Edit Dokter
@login_required
@user_passes_test(is_admin)
def doctor_edit(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctors/doctor_form.html', {
        'form': form,
        'title': 'Edit Dokter'
    })


# ❌ Hapus Dokter
@login_required
@user_passes_test(is_admin)
def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'doctors/doctor_confirm_delete.html', {
        'doctor': doctor
    })


# 💬 (Opsional) Halaman konsultasi dokter untuk dashboard
@login_required
def consultations(request):
    """
    View dummy untuk menghindari error 'NoReverseMatch: doctor_consultations'
    Nanti bisa diisi data konsultasi sebenarnya.
    """
    return render(request, 'doctors/consultations.html')
