from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import RegisterUserForm, LoginUserForm
from .models import *


class ProductFilter():
    def get_category(self):
        return Category.objects.all()

    def get_years(self):
        return Product.objects.filter(draft=False).values('year').distinct()

    def get_memory(self):
        return Memory.objects.all()

    def get_manufacture(self):
        return Manufacture.objects.all()


class StoreView(ListView):
    model = Product
    queryset = Product.objects.filter(draft=False)
    template_name = 'store/store.html'


class ProductView(ProductFilter, ListView):
    model = Product
    queryset = Product.objects.filter(draft=False)
    paginate_by = 3


class ProductDetailView(ProductFilter, DetailView):
    model = Product
    slug_field = 'slug'


class Search(ProductFilter, ListView):
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.filter(title__icontains=self.request.GET.get('search'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = f'search={self.request.GET.get("search")}&'
        return context


class FilterProductView(ProductFilter, ListView):
    paginate_by = 3

    def get_queryset(self):
        if 'year' in self.request.GET and 'manufacture' in self.request.GET:
            queryset = Product.objects.filter(
                Q(year__in=self.request.GET.getlist("year")),
                Q(manufacture__in=self.request.GET.getlist("manufacture"))
            ).distinct()
        else:
            queryset = Product.objects.filter(
                Q(year__in=self.request.GET.getlist("year")) | Q(category__in=self.request.GET.getlist("category")) |
                Q(manufacture__in=self.request.GET.getlist("manufacture")) |
                Q(memory__in=self.request.GET.getlist("memory"))
            ).distinct()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['year'] = ''.join([f'year={x}&' for x in self.request.GET.getlist('year')])
        context['manufacture'] = ''.join([f'manufacture={x}&' for x in self.request.GET.getlist('manufacture')])
        context['category'] = ''.join([f'category={x}&' for x in self.request.GET.getlist('category')])
        context['memory'] = ''.join([f'memory={x}&' for x in self.request.GET.getlist('memory')])
        return context


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'store/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('store_view')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'store/login.html'

    def get_success_url(self):
        return reverse_lazy('product_view')


def logout_user(request):
    logout(request)
    return redirect('store_view')