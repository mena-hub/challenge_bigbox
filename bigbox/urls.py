from django.urls import path
from bigbox import views

bigbox_patterns = ([
    path('', views.boxes, name="boxes"),
    path('<int:box_id>/', views.information, name="information"),
    path('<int:box_id>/activity/', views.activities, name="activities"),
    path('<int:box_id>/activity/<int:activity_id>', views.relation, name="relation"),
    path('<slug:box_slug>/', views.label, name="label"),
], 'bigbox')