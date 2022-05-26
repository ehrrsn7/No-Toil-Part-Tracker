from django.urls import path

from . import views

urlpatterns = [
    path('Filters', views.filters, name='Filters'),

    # stations
    path('Stations',        views.stations, name='Stations'),
    path('Stations/Stamp',  views.stamp,    name='Stations/Stamp'),
    path('Stations/Check',  views.check,    name='Stations/Check'),
    path('Stations/Spray',  views.spray,    name='Stations/Spray'),
    path('Stations/Oil',    views.oil,      name='Stations/Oil'),
    path('Stations/Bag',    views.bag,      name='Stations/Bag'),

    # misc pages (all point to index idk)
    path('SiteMap',     views.index, name='SiteMap'),
    path('SitePlan',    views.index, name='SitePlan'),
    path('Todo',        views.index, name='Todo'),

    # home page
    path('', views.stations, name=''),

    # actions
    path('add', views.add, name='add'),
    path('show_new_parts_list_range', 
        views.show_new_parts_list_range, 
        name='show_new_parts_list_range'),
]