# -*- coding: utf-8 -*-
import random, string
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View, ListView, DeleteView
from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.contrib import messages
from .forms import LoginForm, ChangePasswordForm
from .models import UserProfile
from .functions import SecurityUtils
from WebBoxFashion.apps.general_functions import send_email
from WebBoxFashion.core.json_settings import get_settings
from WebBoxFashion.apps import response_messages
from django.contrib.auth import authenticate
from django.views.generic import TemplateView
from django.template.response import TemplateResponse


settings = get_settings()


class Login(View):
    template_name = "login.html"
    form = LoginForm

    def get(self, request):
        if request.GET.get('tenant_name', False) and schema_exists(request.GET.get('tenant_name')):
            protocol = "https" if settings['USE_SSL'] else "http"
            url_redirect = "{0}://{1}.{2}{3}".format(
                protocol,
                request.GET.get('tenant_name'),
                request.META['HTTP_HOST'],
                reverse_lazy('security:login')
            )
            return HttpResponseRedirect(url_redirect)
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('fluxo:dashboard'))
        else:
            ctx = {'form': self.form}
            if 'next' in request.GET:
                ctx['next'] = request.GET['next']
            return TemplateResponse(request, self.template_name, ctx)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            login(request, form.my_user)
            messages.success(request, _("Bem vindo {0}!".format(form.my_user.first_name)))
            if 'next' in request.POST:
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse_lazy('fluxo:dashboard'))
        else:
            ctx = {'form': form}
            return render(request, self.template_name, ctx)


class Logout(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('security:login'))


class SenhaMudarView(View):
    template_name = "mudarsenha.html"

    def get(self, request):
        return TemplateResponse(request, self.template_name)

    def post(self, request):
        email = request.POST['email'] if 'email' in request.POST else None
        password_one = request.POST['password_one'] if 'password_one' in request.POST else None
        password_two = request.POST['password_two'] if 'password_two' in request.POST else None
        userAuth = authenticate(username=email, password=password_one)
        if userAuth is not None:
            if password_one != password_two:
                user = User.objects.get(username=email)
                user.set_password(password_two)
                user.save()
                return HttpResponseRedirect(reverse_lazy('security:login'))
            else:
                messages.error(request, _("As senhas sao iguais"))
        else:
            messages.error(request, _("Usuario nao identificado"))
        return self.get(request)


class UserProfileData(LoginRequiredMixin, View):
    template_name = "form_create_perfil.html"

    def get(self, request):
        return TemplateResponse(request, self.template_name)

    def post(self, request):
        userprofile = request.user.userprofile
        image_profile = request.FILES['image_profile'] if 'image_profile' in request.FILES else None
        if image_profile:
            userprofile.image_profile = image_profile
            userprofile.save()
        request.user.username = request.POST['email']
        request.user.first_name = request.POST['first_name']
        request.user.last_name = request.POST['last_name']
        request.user.email = request.POST['email']
        request.user.save()
        return HttpResponseRedirect(reverse_lazy('fluxo:dashboard'))


class ChangePassword(LoginRequiredMixin, View):
    template_name = "change_password.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        password_one = request.POST['password_one'] if 'password_one' in request.POST else None
        password_two = request.POST['password_two'] if 'password_two' in request.POST else None
        if password_one and password_two:
            if password_one == password_two:
                request.user.set_password(password_one)
                request.user.save()
                logout(request)
                return HttpResponseRedirect(reverse_lazy('security:login'))
            else:
                messages.error(request, _("as senhas nao coincidem"))
        else:
            messages.error(request, _("Error nos dados recebidos"))
        return self.get(request)


class UserList(LoginRequiredMixin, ListView):
    template_name = "user_list.html"
    model = UserProfile
    paginate_by = 10


class UserNew(LoginRequiredMixin, View):
    template_name = "user_new.html"
    model = UserProfile
    paginate_by = 10
    fields = ['username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff', 'is_active']
    success_url = reverse_lazy('security:user-new')
    utils = SecurityUtils()

    def send_welcome_mail(self, request, new_user, new_user_password):
        protocol = "https" if settings['USE_SSL'] else "http"
        url_server = "{0}://{1}.{2}{3}".format(
            protocol,
            request.tenant.schema_name,
            settings['BASE_URL'],
            reverse_lazy("security:login")
            )
        ctx = {'user': request.user, 'new_user': new_user, 'new_user_password': new_user_password, 'URL_SERVER': url_server}
        html_content = render_to_string('mailing/welcome_user.html', ctx)
        subject = _("Bem vindo ao Portal Gera/ Convite de Novo Usuario")
        send_email(subject, to_email=new_user.email, html_content=html_content)

    def get(self, request):
        ctx = {'random_password': self.utils.random_password()}
        return TemplateResponse(request, self.template_name, ctx)

    def post(self, request):
        try:
            user_exist = User.objects.get(email=request.POST['email'])
        except:
            user_exist = None
        if user_exist:
            messages.error(request, _("Email {0} encontra se registrado no sistema do portal gera".format(request.POST['email'])))
            ctx = {'random_password': self.utils.random_password(), 'first_name': request.POST['first_name'],
                   'last_name': request.POST['last_name'], 'email': request.POST['email']}
            return TemplateResponse(request, self.template_name, ctx)
        else:
            new_user = User.objects.create_user(request.POST['email'],
                                                request.POST['email'],
                                                request.POST['password'])
            new_user.first_name = request.POST['first_name']
            new_user.last_name = request.POST['last_name']
            new_user.is_active = True  # Activamos al usuario
            new_user.save()
            # Enviamos un email de bemvinda
            self.send_welcome_mail(request, new_user, request.POST['password'])
            messages.success(request, response_messages.SAVE_SUCCESSFULL)
            return HttpResponseRedirect(reverse_lazy('security:user-list'))


class UserDelete(LoginRequiredMixin, DeleteView):
    template_name = "user_delete.html"
    model = UserProfile
    success_url = reverse_lazy('security:user-list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, response_messages.DELETE_SUCCESSFULL)
        return super(UserDelete, self).delete(request, *args, **kwargs)


class ActiveInactiveUser(LoginRequiredMixin, View):
    """
    Ativamos / Desativamos usuarios.
    """

    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            user.is_active = not user.is_active
            user.save()
            messages.success(request, response_messages.UPDATE_SUCCESSFULL)
        except User.DoesNotExist:
            messages.error(request, _("Usuario nao encontrado"))
        return HttpResponseRedirect(reverse_lazy('security:user-list'))


class PreLoginView(View):
    template_name = "pre_login.html"
    active_menu = "login"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return request(request, self.template_name)