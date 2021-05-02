
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("transfer", views.transfer, name="transfer"),
    path("accept/<int:id>", views.accept, name="accept"),
    path("greeting", views.greeting, name="greeting"),
    path("spending", views.spending_view, name="spending"),
    path("budget", views.budget_view, name="budget"),

    #API
    path("transferfunc", views.transfer_function, name="transfer_function"),
    path("spendingfunc", views.spending_function, name="spending_function"),
]
