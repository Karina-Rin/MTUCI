from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

app_name = "cart"

urlpatterns = [
    path("", views.cart_detail, name=_("cart_detail")),
    path("add/<int:product_id>/", views.cart_add, name=_("cart_add")),
    path("remove/<int:product_id>/", views.cart_remove, name=_("cart_remove")),
]
