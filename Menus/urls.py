from django.urls import path
from .views import home, scraper, register, login, logout, dashboard, display_menu, user_set_preferences, item_set_preferences
# from .views import item_details

app_name = 'Menus'
urlpatterns = [
    path('', home, name='home'),
    path(r'scraper/', scraper, name='scraper'),
    path(r'create-account/', register, name='register'),
    path(r'login/', login, name='login'),
    path(r'logout/', logout, name='logout'),
    path(r'my-dashboard/', dashboard, name='dashboard'),
    path(r'menus/', display_menu, name='display_menu'),
    # path(r'item/<int:item_id>/', item_details, name='item_details'),
    path(r'my-preferences/', user_set_preferences, name='user_set_preferences'),
    path(r'search/', item_set_preferences, name='item_set_preferences'),
]