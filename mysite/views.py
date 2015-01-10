from django.views.decorators.csrf import csrf_exempt
from mysite.models import Content, RContent, Center, JoinMe, Activities, User
from django.shortcuts import render_to_response
from django.template import loader
# Create your views here.


def my_homepage_view(request):
 
    contents = Content.objects.filter(status=1)
    rcontents = RContent.objects.filter(status=1)
    center = Center.objects.filter(status=1)
    return render_to_response('index.html', {'contents': contents, 'rcontents': rcontents, 'center': center})


@csrf_exempt
def join(request):
    JoinMe.objects.create(fullname=request.POST['fullname'], email=request.POST['email'], myclass=request.POST['myclass'],
                         project=request.POST['project'], describe=request.POST['describe'], status='1')
    return render_to_response('thanks.html')


@csrf_exempt
def joinform(request):
    ac = Activities.objects.filter(status=1)
    return render_to_response('signup.html', {'ac': ac})


def registerform(request):
    return render_to_response('register.html')


def loginform(request):
    return render_to_response('login.html')


def homeform(request):
    return render_to_response('home.html')


@csrf_exempt
def register(request):
    User.objects.create(fullname=request.POST['fullname'], username=request.POST['username'], password=request.POST['password'],
                         num=request.POST['num'], describe=request.POST['describe'], myactivities_id='1')
    return render_to_response('register1.html')


@csrf_exempt
def login(request):
    u = User.objects.get(username=request.POST['username'])
    if u.password == request.POST['password']:
        ac = Activities.objects.filter(status=1)
        jm = JoinMe.objects.filter(fullname=u.fullname)
        return render_to_response('home.html', {'u': u, 'ac': ac, 'jm': jm})
    else:
        return render_to_response('login.html')


def index(request):
    return render_to_response('index.html')


def joindetail(request):
    j = JoinMe.objects.filter(status=1)
    return render_to_response('joindetail.html', {'j': j})


@csrf_exempt
def contactus(request):
    if request.method == 'POST':
        message = request.POST['fromemail'] + "  " + request.POST['content']
        send_mail(request.POST['subject'], message, '654543782@qq.com', ['shuilikexie@163.com'], fail_silently=False)
        return render_to_response('sendfeedback.html')
    else:
        return render_to_response('contactus.html')