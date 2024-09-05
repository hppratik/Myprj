from django.shortcuts import render,redirect,get_object_or_404
from .models import User
from .models import Client
from .models import Project
from datetime import datetime


# Create your views here.
def index(request):
    return render(request, 'index.html')

def user(request):
    return render(request, 'user.html')

def userview(request):
    user=User.objects.all()
    return render(request, 'userview.html',{'userdata':user})

def delete_user(request, userid):
    user = get_object_or_404(User, userid=userid)
    user.delete()
    return redirect('userview')

def insertuser(request):

    vuid = request.POST['tuid'];
    vunam = request.POST['tuname'];
   
    us=User(userid=vuid, username=vunam);
    us.save();
    return render(request, 'index.html',{})

def edit_user(request, userid):
    user = get_object_or_404(User, userid=userid)

    if request.method == 'POST':
        user.username = request.POST['username']
        user.save()
        return redirect('userview')
    
    return render(request, 'useredit.html', {'user': user})




def client(request):
    return render(request, 'client.html')


def insertclient(request):

    vcid = request.POST['tcid'];
    vcnam = request.POST['tcname'];
    vcby=request.POST['tccreate']; # this should be a u

    
    uss=Client(clientid=vcid, clientname=vcnam, created_by=vcby);
    uss.save();
    return render(request, 'index.html',{})


def clientview(request):
    client=Client.objects.all()
    return render(request, 'clientview.html',{'clientdata':client})

def delete_client(request, clientid):
    client = get_object_or_404(Client, clientid=clientid)
    client.delete()
    return redirect('clientview')


def edit_client(request, clientid):
    client = get_object_or_404(Client, clientid=clientid)

    if request.method == 'POST':
        client.clientname = request.POST.get('clientname')
        client.created_by = request.POST.get('created_by')
        client.save()
        return redirect('clientview')
    
    return render(request, 'clientedit.html', {'client': client})

def project(request):
    return render(request, 'project.html')


def insertproject(request):

    vpid = request.POST['tpid'];
    vpnam = request.POST['tpname'];
    vpcnam = request.POST['tpcname'];
    vpunam = request.POST['tpuname'];
    vpcby=request.POST['tpccreate']; 
    usss=Project(projectid=vpid, projectname=vpnam, clientname=vpcnam, username=vpunam, created_by=vpcby );
    usss.save();
    return render(request, 'index.html',{})


def projectview(request):
    project=Project.objects.all()
    return render(request, 'projectview.html',{'projectdata':project})

def delete_project(request, projectid):
    project = get_object_or_404(Project, projectid=projectid)
    project.delete()
    return redirect('projectview')
def edit_project(request, projectid):
    project = get_object_or_404(Project, projectid=projectid)

    if request.method == 'POST':
        project.projectname = request.POST.get('projectname')
        project.clientname = request.POST.get('clientname')
        project.username = request.POST.get('username')
        project.created_by = request.POST.get('created_by')
        project.save()
        return redirect('projectview')
    
    return render(request, 'projectedit.html', {'project': project})