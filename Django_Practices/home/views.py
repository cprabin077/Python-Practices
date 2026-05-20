from django.http import JsonResponse
from django.shortcuts import redirect, render

from home.forms import UserForm
from home.models import User

# Create your views here.
def home_json(request):
    data = {
        'name':'Prabin Chaudhary',
        'address':'Dhangadhi',
        'phone': 9809120928
    }

    return JsonResponse(data)


def home_page(request):
    return render(request, 'dashboard/home.html')

def login_page(request):
    return render(request, 'login/login.html')

def user_list(request):
    user = User.objects.all()
    # context = {
    #     'users':user
    # }

    # return render(request, 'user_info/users.html', context)
    return render(request, 'user_info/users.html', {'users':user})

def user_create(request):
    print(request.method)
    if request.method == "POST":
        print("This is post metthod")
        data = request.POST
        User.objects.create(
            full_name = data['full_name'],
            email = data['email'],
            phone = data['phone'],
            city = data['city']
        )
        return redirect("/home/user")
    return render(request, 'user_info/create.html')


def user_create2(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/user')
        else:
            print(form.errors)

    context = {
        "form": form
    }
    return render(request, 'user_info/create2.html', context)



