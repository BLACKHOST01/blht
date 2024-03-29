from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, DeleteView, ListView
from core.models import product, profile, category
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from .forms import LoginForm
from django.contrib.auth.decorators import login_required




def log_out(request):
    logout(request)
    return redirect('core:home')


def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('core:dashboard')
        else:
            return redirect('core:login')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(
#                 request, username=cd['username'], password =cd['password']
#             )
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('/')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#     return render(request, 'auth/login.html', {'form': form})





def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'auth/signup.html', {'form': form})








class productList(ListView):
    model = product
    context_object_name = 't'
    template_name='product_list.html'



class productCreateView(CreateView):
    model = product
    fields =  "__all__"
    template_name = "product_form.html"
    
    success_url = reverse_lazy('core:home')

    
    







class home_view(TemplateView):
    template_name = "c_templates/home.html"



class exchangeView(TemplateView):
    template_name = "c_templates/exchange.html"
    
    
    
# class signupView(TemplateView):
#     template_name = "auth/signup.html"

@login_required
def dashboard(request):
    profiles = profile.objects.all()
    
  
    return render (request, 'c_templates/dashboard.html', {'profile': profile})
class profileCreateView(CreateView):
    model = profile
    fields = [ 'photo', 'country', 'balance']
    template_name = "profile/profile_create.html"
    success_url = reverse_lazy('core:dashboard')