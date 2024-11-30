from django.urls import path
from django.views.decorators.cache import cache_page
from spam.apps import SpamConfig


app_name = SpamConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path("create_product/", ProductCreateView.as_view(), name="product_create"),
    path("<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("create_category/", CategoryCreateView.as_view(), name="category_create"),
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("contacts/", contacts, name="contacts"),
]