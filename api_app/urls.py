from django.conf.urls import url
from api_app import views

urlpatterns = [
    url(r'^api/student$', views.student_list),
    url(r'^api/student/(?P<pk>[0-9]+)$', views.student_detail),
    url(r'^api/attendance$', views.attendance),

]