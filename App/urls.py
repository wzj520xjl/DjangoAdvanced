from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^index/',views.index,name='lele'),
    url(r'^addstu/',views.add_student,name='add_student'),
    url(r'^getstu/',views.get_student,name='get_stundet'),



]