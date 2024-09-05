from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("user",views.user,name='user'),
    path("userview",views.userview,name='userview'),
    path("delete_user/<str:userid>/", views.delete_user, name='delete_user'),
    path("insertuser/",views.insertuser,name='insertuser'),
    path("edit_user/<str:userid>/", views.edit_user, name='edit_user'),
   
   

    path("client",views.client,name='client'),
    path("insertclient/",views.insertclient,name='insertclient'),
    path("clientview",views.clientview,name='clientview'),
    path("delete_client/<str:clientid>/", views.delete_client, name='delete_client'),
    path("edit_client/<str:clientid>/", views.edit_client, name='edit_client'),
   

    path("project",views.project,name='project'),
    path("insertproject/",views.insertproject,name='insertproject'),
    path("projectview",views.projectview,name='projectview'),
    path("delete_project/<str:projectid>/", views.delete_project, name='delete_project'), 
    path("edit_project/<str:projectid>/", views.edit_project, name='edit_project'),
    


]
