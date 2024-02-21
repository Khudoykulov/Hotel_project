from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import auth_logout
from django.views.generic import CreateView, TemplateView, View
from .form import USerRegister
from .models import Profile


class RegisterView(View):
    form_class = USerRegister
    template_name = 'account/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = USerRegister(request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save()
            print('...........................................................................')
            if request.FILES:
                Profile.objects.create(user_id=user.id, picture=request.FILES.get('image'))
                messages.success(request, 'Successfully registered')
        return redirect('account:login')


class LoginView(TemplateView):
    template_name = 'account/login.html'


class LogoutView(View):
    template_name = 'account/log_out.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        auth_logout(request)
        messages.success(request, 'Successfully logged out')
        return redirect('/')

