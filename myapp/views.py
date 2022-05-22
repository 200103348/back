from django.shortcuts import redirect, render, get_object_or_404
from .forms import *
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import admin_only, unauthenticated_user, allowed_users
from django.core.mail import send_mail
from django.views.decorators.csrf import *
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# Create your views here.

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def index(request):
    if request.method == "POST":
        form = MvideoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video-upload')
    else:
        form = MvideoForm()

    var = {'form': form}
    return render(request, 'myapp/index.html', var)



@login_required(login_url='login')
@admin_only
def newproject(request):
    var = MenPrize.objects.all()
    return render(request, 'myapp/newproject.html', {'var': var})



@unauthenticated_user
def loginPage(request):
	if request.user.is_authenticated:
		return redirect('project')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('project')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'myapp/login.html', context)



def logoutUser(request):
    logout(request)
    return redirect('login')



def test(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'],
                             '200103348@stu.sdu.edu.kz', ['200103348@stu.sdu.edu.kz'], fail_silently=True)
            if mail:
                messages.success(request, 'Email is send!')
                return redirect('test')
            else:
                messages.error(request,'Sending error!')
        else:
            messages.error(request, 'Register error!')
    else:
        form=ContactForm()
    return render(request, 'myapp/test.html', {'form':form})



def userPage(request):
    context={}
    return render(request, 'myapp/user.html', context)



def managerPage(request):
    return render(request, 'myapp/manager.html')


@unauthenticated_user
def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')

			messages.success(request, 'Account was created for ' + user)

			return redirect('login')

	context = {'form': form}
	return render(request, 'myapp/register.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['manager'])
def news_home(request):
    error = ' '
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sportnews')
        else:
            error = 'Form was uncorrect'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'myapp/news_home.html', data)



@allowed_users(allowed_roles=['manager'])
def form(request):
    post = Articles.objects.all()
    return render(request, 'myapp/form.html', {'post': post})



class NewsDetailView(DetailView):
    model = Articles
    template_name = 'myapp/details_view.html'
    context_object_name = 'article'



class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'myapp/news_home.html'

    form_class = ArticlesForm



def delete(request, id):
    al = Articles.objects.get(id=id)
    al.delete()
    return redirect("sportnews")



def forupload(request):
    video = Myvideo.objects.all()

    return render(request, 'myapp/forupload.html', {'video' : video})



@login_required(login_url='login')
def tokyo(request):
    return render(request, 'myapp/tokyo.html')



@login_required(login_url='login')
def olympics(request):
    summ = Summer.objects.all()
    win = Winter.objects.all()
    context = {'summ': summ, 'win': win}
    return render(request, 'myapp/olympics.html', context=context)


def show_post(request, post_id):
    post = get_object_or_404(Post, slug=post_id)
    context = {'post': post}
    return render(request, 'myapp/oop.html', context=context)


