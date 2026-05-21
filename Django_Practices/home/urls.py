from django.urls import path
from home.views import home_json, home_page, login_page, user_create, user_create2, user_delete, user_list, user_update


urlpatterns = [
    path('json/', home_json, name='json-data'),
    path('home_page/',home_page, name = 'home'),
    path('login_page/',login_page, name = 'login'),
    path('user/', user_list, name='user' ),
    path('user_create/', user_create, name='create'),
    path('user_create2/', user_create2, name='create2'),
    path('user_update/<int:id>/', user_update, name='update'),
    path('user_delete/<int:id>/', user_delete, name='delete'),
]