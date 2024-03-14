from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment, TemporaryUser
from .forms import AppointmentForm, TemporaryUserForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
# from django.contrib.auth.tokens import account_activation_token
from django.contrib.auth.tokens import default_token_generator as account_activation_token


# Create your views here.
@login_required
def appointments(request):
    appointments = Appointment.objects.filter(patient=request.user)
    return render(request, 'appointments.html', {'appointments': appointments})


@login_required
def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.save()
            return redirect('appointments:appointments')
    else:
        form = AppointmentForm()
    return render(request, 'create_appointment.html', {'form': form})


@login_required
def create_temporary_user(request):
    if request.method == 'POST':
        form = TemporaryUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # Send a confirmation email to the user
            current_site = get_current_site(request)
            subject = 'Activate Your Account'
            message = 'Please go to this link to activate your account: ' + current_site.domain + '/activate/' + account_activation_token.make_token(
                user)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            send_mail(subject, message, email_from, recipient_list)

            # Redirect the user to a confirmation page
            return redirect('confirmation')
    else:
        form = TemporaryUserForm()
    return render(request, 'create_temporary_user.html', {'form': form})
