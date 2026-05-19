from django.urls import path
from home.views import home_json, home_page, login_page, user_list


urlpatterns = [
    path('json/', home_json, name='json-data'),
    path('home_page/',home_page, name = 'home'),
    path('login_page/',login_page, name = 'login'),
    path('user/', user_list, name='user' ),
]