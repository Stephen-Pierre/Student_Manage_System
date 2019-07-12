from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^show_classes/', views.show_classes),
    url(r'^add_grade/', views.add_grade),
    url(r'^add_grade_01/', views.add_grade_01),
    url(r'^alter_grade/', views.alter_grade),
    url(r'^alter_grade_01/', views.alter_grade_01),
    url(r'^delete_grade/', views.delete_grade),
    url(r'^show_students/', views.show_students),
    url(r'^add_student/', views.add_student),
    url(r'^delete_student/', views.delete_student),
    url(r'^alter_student/', views.alter_student),
]