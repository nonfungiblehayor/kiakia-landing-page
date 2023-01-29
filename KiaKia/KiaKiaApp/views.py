from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Mail
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def index(request):
    mails = Mail.objects.all()
    if request.method == 'POST':
        email = request.POST['email']

        if email:
            if Mail.objects.filter(email=email).exists():
                messages.error(
                    request, 'This email already exists. \n Choose another to join the waitlist.')
                return redirect('index')
            else:
                new_mail = Mail.objects.create(email=email)
                new_mail.save()
                send_mail(
                    subject='Welcome to KiaKia exchange',
                    message='You have successfully joined the waitlist, we weould inform you when we launch.',
                    from_email='kiakiaexchange@gmail.com',
                    recipient_list=[request.POST['email']],
                    fail_silently=True
                )
                if new_mail:
                    messages.success(
                        request, 'You have successfully joined the waitlist!')
                else:
                    messages.error(
                        request, 'Check your connection and try again.')
                return redirect('index')

    else:
        return render(request, 'index.html', {'mails': mails})


# if 'success' in messages:
