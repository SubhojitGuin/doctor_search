from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Doctor
from .forms import DoctorForm


# Create your views here.
@login_required
def doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctors.html', {'doctors': doctors})


@login_required
def detail(request, pk):
    doctor = Doctor.objects.get(pk=pk)
    return render(request, 'doctors/detail.html', {'doctor': doctor})

@login_required
def create_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.user = request.user
            doctor.save()
            return redirect('doctors:doctors')
    else:
        form = DoctorForm()
    return render(request, 'doctors/create_doctor.html', {'form': form})


@login_required
def edit_doctor(request, pk):
    doctor = Doctor.objects.get(pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            doctor = form.save()
            return redirect('doctors:doctors')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctors/create_doctor.html', {'form': form})


@login_required
def delete_doctor(request, pk):
    Doctor.objects.get(pk=pk).delete()
    return redirect('doctors:doctors')


@login_required
def search_doctors(request):
    query = request.GET.get('q')
    if query:
        doctors = Doctor.objects.filter(name__icontains=query)
    else:
        doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'doctors/search_results.html', context)
