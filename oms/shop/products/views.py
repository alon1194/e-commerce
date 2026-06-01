from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Category



# Existing product view 

class ProductListView(View):
    def get(self, request):
        products = [
            {"name": '24" Monitor', "price": 129.90, "available": True},
            {"name": "Mechanical Keyboard", "price": 89.50, "available": False},
            {"name": "Wireless Mouse", "price": 29.99, "available": True},
        ]
        return render(request, "products/list.html", {"products": products})



# New Category Backoffice views

class CategoryAdminListView(ListView):
    model = Category
    template_name = "products/admin/admin_list.html"
    context_object_name = "categories"


class CategoryAdminCreateView(CreateView):
    model = Category
    fields = ["name", "description", "is_active"]
    template_name = "products/admin/admin_form.html"
    success_url = reverse_lazy("shop:products:admin_categories_list")


class CategoryAdminUpdateView(UpdateView):
    model = Category
    fields = ["name", "description" "is_active"]
    template_name = "products/admin/admin_form.html"
    success_url = reverse_lazy("shop:products:admin_categories_list")


class CategoryAdminDeleteView(DeleteView):
    model = Category
    template_name = "products/admin/admin_confirm_delete.html"
    success_url = reverse_lazy("shop:products:admin_categories_list")