from django.http import JsonResponse
from django.shortcuts import render

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
    
