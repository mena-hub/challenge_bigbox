from django.urls import path
from bigbox import views

urlpatterns = [
    path('', views.home, name="home"),
    path('box/', views.boxes, name="boxes"),
    path('box/<int:box_id>/', views.information, name="information"),
    path('box/<int:box_id>/activity/', views.activities, name="activities"),
    path('box/<int:box_id>/activity/<int:activity_id>', views.relation, name="relation"),
    path('box/<slug:slug>/', views.label, name="label"),
]