from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

app_name = "orders"

urlpatterns = [
    path("create/", views.order_create, name=_("order_create")),
    path(
        "admin/order/<int:order_id>",
        views.admin_order_detail,
        name=_("admin_order_detail"),
    ),
]
