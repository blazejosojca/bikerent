from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.template.response import TemplateResponse
from django.views.generic import (
    ListView,
    View,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView
)
from django.contrib.auth import authenticate, login
from .forms import UserAddForm, ClientForm
from .models import Client
from bike.models import Renting


class CreateClient(View):
    model = Client
    form_class = ClientForm
    template_name = 'client/client_form.html'


class UpdateClient(UpdateView):
        model = Client
        form_class = ClientForm
        template_name = 'client/client_form.html'


class ClientDetails(DetailView):

    model = Client

    def get_context_data(self, **kwargs):
        context = super(ClientDetails, self).get_context_data(**kwargs)
        return context


class ClientList(ListView):
    template_name = "client/client_list.html"
    ctx = "client_list"

    def get_queryset(self):
        return Client.objects.all()


class ClientListRenting(View):
    template_name = "client/client_rentings.html"

    def get(self, request, pk):
        client = Client.objects.get(pk=pk)
        return render(request, self.template_name, {'client': client,
                                                    'renting_list': Renting.objects.filter(related_client=pk)})


class DeleteClient(DetailView):
    model = Client
    success_url = "client/client_list.html"


"""

class LoginView(FormView):
    model = User
    form_class = UserAddForm
    fields = '__all__'
    success_url = '/'
    template_name = 'client/form_template.html'

    def form_valid(self, form):
        login(self.request, form.user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('client_list')


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect("/")


class UserAddView(CreateView):

    template_name = 'client/form_template.html'
    form_class = UserAddForm

    def get_success_url(self):
        return reverse('list-users')


    def form_valid(self, form):
        user = get_user_model()
        user.objects.create_user(**form.cleaned_data)
        return redirect(self.get_success_url())

"""
