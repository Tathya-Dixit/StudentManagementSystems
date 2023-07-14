from django.urls import path
from pages import views
urlpatterns = [
    path('',views.profilepage,name="profilepage"),
    path('assignments',views.assignmentspage,name="assignmentspage"),
    path('result',views.resultspage,name="resultpage"),
    path('labrecords',views.labrecpage,name="labrecpage"),
    path('performance',views.performancepage,name="performancepage"),
]