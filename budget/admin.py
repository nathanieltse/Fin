from django.contrib import admin

from .models import *
# Register your models here.


class user_list(admin.ModelAdmin):
    list_display = ("id","username")

class account(admin.ModelAdmin):
    listin_display = ("id","user","number","amount")

class spending(admin.ModelAdmin):
    listin_display = ("id","user","item","item_price","timestamp", "category")

class category(admin.ModelAdmin):
    list_display = ("id", "category")
    

class transfer(admin.ModelAdmin):
    listin_display = ("id","sender","recipient","amount", "recived", "timestamp", "message")

class budget(admin.ModelAdmin):
    listin_display = ("id","user","item","item_price", "category","timestamp")

class user_budget(admin.ModelAdmin):
    listin_display = ("id","user","amount", "category","timestamp")

admin.site.register(User, user_list),
admin.site.register(Account, account),
admin.site.register(Spending, spending),
admin.site.register(Category, category),
admin.site.register(Transfer, transfer),
admin.site.register(Budget, budget),
admin.site.register(User_budget, user_budget),

