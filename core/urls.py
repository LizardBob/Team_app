from django.contrib import admin
from django.urls import path
from . import views

app_name='core'
urlpatterns = [
    path('druzyna/', views.druzyna, name='druzyna'),
    path('<int:pk>/panel_zawodnika', views.pan_zawodnika, name='pan_zawodnika'),
    path('panel_trenera/', views.pan_trenera, name='pan_trenera'),
    path('zaloguj/', views.our_log, name='our_log'),
    path('choose/', views.choose, name='choose'),
    path('', views.index, name='index'),
    path('thx/', views.thx, name= 'thank'),
    path('<int:user_id>/', views.user_page, name='user_page'),
    path('<int:user_player_id>/player_page', views.player_page, name='player_page'),
    path('<int:team_id>/team_page', views.team_page, name='team_page'),
    path(r'signup/', views.signup, name='signup'),
    path('admin/', admin.site.urls),
]
