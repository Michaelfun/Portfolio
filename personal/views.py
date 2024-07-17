from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .models import *

# Create your views here.


def home(request):
    my_info = Me.objects.all()
    interest = Interest.objects.all()
    services = Service.objects.all()
    testimonial = Testimonial.objects.all()

    data = {
        'my_info': my_info,
        'interest': interest,
        'services': services,
        'testimonial': testimonial,
    }
    return render(request, 'index.html', data)


def portfolio(request):
    return render(request, 'pages/portfolio-details.html')


def send_mail(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        body = request.POST.get('message')

        print(body)

        body = (name +'\n' +'from:'+ ' '+ email+ '\n' + body)

        receiver_email = "funganoti.work@gmail.com"
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        # Authentication
        s.login("funganoti@gmail.com", "yfde vwii lhwa pcsu ")

        # message to be sent
        message = MIMEMultipart()
        message["From"] = email
        message["To"] = receiver_email
        message["Subject"] = subject
        # sending the mail
        message.attach(MIMEText(body, "plain"))
        s.sendmail(email, receiver_email, message.as_string())
        # terminating the session
        s.quit()
        messages.info(request, 'Email sent successfully')
        return redirect('home')
