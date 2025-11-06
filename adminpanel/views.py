from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from users.models import CustomUser
from consultation.models import Consultation
from .models import ActivityLog  # Import hanya yang pasti ada

# 🔒 Fungsi pengecekan role admin
def is_admin(user):
    # Cek apakah user superuser atau punya role 'admin'
    return getattr(user, 'is_superuser', False) or getattr(user, 'role', None) == 'admin'


# 🧭 Dashboard Admin
@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    total_users = CustomUser.objects.count()
    total_doctors = CustomUser.objects.filter(role='doctor').count()
    total_patients = CustomUser.objects.filter(role='patient').count()
    total_consultations = Consultation.objects.count()

    context = {
        'total_users': total_users,
        'total_doctors': total_doctors,
        'total_patients': total_patients,
        'total_consultations': total_consultations,
    }
    return render(request, 'adminpanel/dashboard.html', context)


# 🧑‍💻 Kelola Pengguna
@login_required
@user_passes_test(is_admin)
def user_list(request):
    users = CustomUser.objects.all().order_by('-date_joined')
    context = {'users': users}
    return render(request, 'adminpanel/user_list.html', context)


# 🩺 Kelola Dokter
@login_required
@user_passes_test(is_admin)
def doctor_list(request):
    try:
        from users.models import Doctor  # Import di dalam fungsi agar aman
        doctors = Doctor.objects.select_related('user').all().order_by('-user__date_joined')
    except Exception:
        doctors = []
    context = {'doctors': doctors}
    return render(request, 'adminpanel/doctor_list.html', context)


# 💬 Daftar Konsultasi
@login_required
@user_passes_test(is_admin)
def consultation_list(request):
    consultations = Consultation.objects.select_related('doctor', 'patient').all().order_by('-created_at')
    context = {'consultations': consultations}
    return render(request, 'adminpanel/consultation_list.html', context)


# 🕓 Log Aktivitas Dinamis
@login_required
@user_passes_test(is_admin)
def activity_log(request):
    logs = ActivityLog.objects.select_related('user').all().order_by('-timestamp')
    context = {'activity_logs': logs}
    return render(request, 'adminpanel/activity_log.html', context)
