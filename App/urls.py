from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^index/',views.index,name='lele'),
    url(r'^addstu/',views.add_student,name='lele'),
    url(r'^getstu/',views.get_student,name='lele'),



]