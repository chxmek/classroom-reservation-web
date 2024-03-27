from datetime import datetime
from django.contrib import messages
from django.shortcuts import render
from decimal import Decimal

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Room, Book
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from decimal import Decimal


def home(request):
    if request.user.is_authenticated:
        return render(request, 'myapp/home.html')
    else:
        return render(request, 'myapp/signin.html')


@login_required(login_url='signin')
def findclassroom(request):
    context = {}
    if request.method == 'POST':
        building_r = request.POST.get('building')
        floor_r = request.POST.get('floor')
        date_r = request.POST.get('date')
        date_r = datetime.strptime(date_r,"%Y-%m-%d").date()
        year = date_r.strftime("%Y")
        month = date_r.strftime("%m")
        day = date_r.strftime("%d")
        classroom_list = Room.objects.filter(building=building_r, floor=floor_r, date__year=year, date__month=month, date__day=day)
        if classroom_list:
            return render(request, 'myapp/list.html', locals())
        else:
            context['data'] = request.POST
            context["error"] = "No available classroom schedule for entered."
            return render(request, 'myapp/findclassroom.html', context)
    else:
        return render(request, 'myapp/findclassroom.html')


@login_required(login_url='signin')
def bookings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('classroom_id')
        seats_r = int(request.POST.get('no_seats'))
        classroom = Room.objects.get(id=id_r)
        time_r_r = request.POST.get('time')  # Get the selected time from the form

        if classroom:
            if classroom.remain >= int(seats_r):
                name_r = classroom.room_name
                building_r = classroom.building
                floor_r = classroom.floor
                total_r = Decimal(classroom.total)
                image_r = classroom.image
                date_r = classroom.date
                time_r = classroom.time_create
                time_period_r = time_r_r  # Update the time with the selected time
                username_r = request.user.username
                email_r = request.user.email
                userid_r = request.user.id
                remain_r = classroom.remain - seats_r
                Room.objects.filter(id=id_r).update(remain=remain_r)
                book = Book.objects.create(name=username_r, email=email_r, userid=userid_r, room_name=name_r,
                                           building=building_r, uid=id_r,
                                           floor=floor_r, total=seats_r, date=date_r, time_create=time_r, time_period=time_period_r, image=image_r,
                                           status='BOOKED')
                print('------------book id-----------', book.id)
                # book.save()
                return render(request, 'myapp/bookings.html', locals())
            else:
                # context["error"] = "Sorry select fewer number of seats"
                context["error"] = "Sorry, this classroom is already booked."
                return render(request, 'myapp/findclassroom.html', context)

    else:
        return render(request, 'myapp/findclassroom.html')


@login_required(login_url='signin')
def cancellings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('classroom_id')
        #seats_r = int(request.POST.get('no_seats'))

        try:
            book = Book.objects.get(id=id_r)
            classroom = Room.objects.get(id=book.uid)
            remain_r = classroom.remain + book.total
            Room.objects.filter(id=book.uid).update(remain=remain_r)
            #total_r = book.total - seats_r
            Book.objects.filter(id=id_r).update(status='CANCELLED')
            Book.objects.filter(id=id_r).update(total=0)
            messages.success(request, "Booked Rooms has been cancelled successfully.")
            return redirect(seebookings)
        except Book.DoesNotExist:
            context["error"] = "Sorry You have not booked that room"
            return render(request, 'myapp/error.html', context)
    else:
        return render(request, 'myapp/findclassroom.html')


@login_required(login_url='signin')
def seebookings(request,new={}):
    context = {}
    id_r = request.user.id
    book_list = Book.objects.filter(userid=id_r)
    if book_list:
        return render(request, 'myapp/booklist.html', locals())
    else:
        context["error"] = "Sorry no rooms booked"
        return render(request, 'myapp/findclassroom.html', context)


def signup(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        email_r = request.POST.get('email')
        password_r = request.POST.get('password')
        user = User.objects.create_user(name_r, email_r, password_r, )
        if user:
            login(request, user)
            return render(request, 'myapp/thank.html')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'myapp/signup.html', context)
    else:
        return render(request, 'myapp/signup.html', context)


def signin(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        password_r = request.POST.get('password')
        user = authenticate(request, username=name_r, password=password_r)
        if user:
            login(request, user)
            # username = request.session['username']
            context["user"] = name_r
            context["id"] = request.user.id
            return render(request, 'myapp/success.html', context)
            # return HttpResponseRedirect('success')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'myapp/signin.html', context)
    else:
        context["error"] = "You are not logged in"
        return render(request, 'myapp/signin.html', context)


def signout(request):
    context = {}
    logout(request)
    context['error'] = "You have been logged out"
    return render(request, 'myapp/signin.html', context)


def success(request):
    context = {}
    context['user'] = request.user
    return render(request, 'myapp/success.html', context)
