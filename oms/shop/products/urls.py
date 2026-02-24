
from django.urls import path



from .views import (
    
    ProductListView,
    CategoryAdminListView,
    CategoryAdminCreateView,
    CategoryAdminUpdateView,
    CategoryAdminDeleteView,
)

app_name = "products"

urlpatterns = [
  
    # Public product listing
    
    path("", ProductListView.as_view(), name="product_list"),

  
    # Backoffice Category CRUD
  
    path(
        "admin/categories/",
        CategoryAdminListView.as_view(),
        name="admin_categories_list",
    ),
    path(
        "admin/categories/create/",
        CategoryAdminCreateView.as_view(),
        name="admin_categories_create",
    ),
    path(
        "admin/categories/<int:pk>/edit/",
        CategoryAdminUpdateView.as_view(),
        name="admin_categories_edit",
    ),
    path(
        "admin/categories/<int:pk>/delete/",
        CategoryAdminDeleteView.as_view(),
        name="admin_categories_delete",
    ),
]