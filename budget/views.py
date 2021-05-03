from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from django.db.models import Sum
import json
import random
import datetime
import calendar
from datetime import date, timedelta
from django.views.decorators.csrf import csrf_exempt


from .models import *

#greeting page
def greeting (request):
    return render(request, "budget/greeting.html")
    
def index(request):
    if request.user.is_authenticated:
        new_transfer = Transfer.objects.filter(
            recipient=request.user, received = False
        )
        spending = Spending.objects.filter(
            user=request.user
        )
        budget = Budget.objects.filter(
            user=request.user
        )
        exclude = Transfer.objects.filter(
            recipient=request.user
        )
        #try to see if user has a spending account
        if request.method == "GET":
            try:
                account = Account.objects.get(
                    user = request.user
                )
                #total of budget and spending
                total_budget = budget.aggregate(total_budget=Sum("item_price")).get('total_budget')
                total_spending = spending.aggregate(total_spending=Sum("item_price")).get('total_spending')
                total_exclude = exclude.aggregate(total_exclude=Sum("amount")).get('total_exclude')
                #set day range
                startdate = date.today().replace(day=1)
                days_in_month = calendar.monthrange(startdate.year, startdate.month)[1]
                #set to only show day range's data (summary)
                budget = budget.filter(timestamp__range=[startdate, startdate + timedelta(days=days_in_month)])
                spending = spending.filter(timestamp__range=[startdate, startdate + timedelta(days=days_in_month)])
                exclude = exclude.filter(timestamp__range=[startdate, startdate + timedelta(days=days_in_month)])
                #total of budget and spending
                total_budget = budget.aggregate(total_budget=Sum("item_price")).get('total_budget')
                total_spending = spending.aggregate(total_spending=Sum("item_price")).get('total_spending')
                total_exclude = exclude.aggregate(total_exclude=Sum("amount")).get('total_exclude')
                #if there's no transaction
                if total_exclude != None:
                    total_exclude = total_exclude
                else:
                    total_exclude = 0
                if total_budget != None:
                    
                    total_budget = total_budget
                else:
                    total_budget = 0
                if total_spending !=None:
                
                    total_spending = total_spending - total_exclude
                else:
                    total_spending = 0

                total = total_budget + total_spending 
                
            except Account.DoesNotExist:
                return render(request, "budget/index.html")
        #opening spending account
        if request.method == "POST":
            user = request.user
            number = random.randint(0000000000,9999999999)
            amount = 200
            new_account = Account(
                user = user,
                number = number,
                amount = amount
            )
            new_account.save()
            return HttpResponseRedirect(reverse("index"))
        return render(request, "budget/index.html",{
            "account":account,
            "transfers":new_transfer,
            "total":'{:0.2f}'.format(total),
        })
    else:
        return HttpResponseRedirect(reverse("greeting"))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "budget/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "budget/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "budget/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "budget/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "budget/register.html")

#transfer page
@login_required
def transfer(request):
    transfer_history = Transfer.objects.order_by('-id').filter(
        sender=request.user
    )
    new_transfer = Transfer.objects.filter(
        recipient=request.user, received = False
    )
    #check if user has an spending account to do transfer
    if request.method == "GET":
        try:
            account = Account.objects.get(
                user = request.user
            )
        except Account.DoesNotExist:
            return render(request, "budget/transfer.html")
    #opening spending account function
    if request.method == "POST":
        user = request.user
        number = random.randint(0000000000,9999999999)
        amount = 200
        new_account = Account(
            user = user,
            number = number,
            amount = amount
        )
        new_account.save()
        return HttpResponseRedirect(reverse("index"))
    return render(request, "budget/transfer.html",{
        "historys":transfer_history,
        "transfers":new_transfer,
        "account":account
    })

#accepting transfer function
@login_required
def accept(request, id):
    if request.method == "POST":
        account = Account.objects.get(user=request.user)
        transfer = Transfer.objects.get(pk=id)
        #check if recipient is user
        if transfer.recipient == request.user:
            #check if transfer has been recived
            if transfer.received == False:
                account.amount += int(transfer.amount)
                transfer.received = True
                spending = Spending(
                    user = request.user,
                    item = "Money Transfer In",
                    item_price = int(transfer.amount),
                    category = Category.objects.get(id=1)
                )
                account.save()
                transfer.save()
                spending.save()
    return HttpResponseRedirect(reverse("transfer"))

#API call to transfer
@csrf_exempt
@login_required
def transfer_function(request):
    #posting data to server
    if request.method == "POST":
        data=json.loads(request.body)
        transfer = Transfer(
            sender = request.user,
            recipient = User.objects.get(username=data["recipient"]),
            amount = data["amount"],
            message = data["message"],
        )
        #if recipient and amount is empty, bounce back
        if data["recipient"] == "":
            return JsonResponse({
                "error": "At least one recipient required."
            }, status=400)
        if data["amount"] == "":
            return JsonResponse({
                "error": "Transfer amount required."
            }, status=400)
        account = Account.objects.get(user=request.user)
        transfer_amount = int(data["amount"])
        #make sure user has enough money to transfer
        if account.amount >= transfer_amount:
            transfer.save()
            account.amount -= transfer_amount 
            account.save()
            spending = Spending(
                user=request.user,
                item = "Money Transfer Out",
                item_price = transfer_amount,
                category = Category.objects.get(id=1)
                )
            spending.save()
            user_budget = User_budget(
                user=request.user,
                amount = transfer_amount,
                category = Category.objects.get(id=1),
                timestamp= datetime.datetime.now(),
            )
            user_budget.save()
            return JsonResponse({"message": "Transfer sent successfully."}, status=201)
        return JsonResponse({
                "error": "Transfer amount exceed account balance."
            }, status=400)
    else:
        return JsonResponse({
            "error": "POST request required."
        }, status=400)

#spending acount detail page
@login_required
def spending_view(request):
    spending = Spending.objects.filter(
        user=request.user
    )
    return render(request, "budget/spending.html", {
        "spendings":spending,
    })

#budget tool detail page
@login_required
def budget_view(request):
    spending = Spending.objects.filter(
        user=request.user
    )
    budget = Budget.objects.filter(
        user=request.user
    )
    exclude = Transfer.objects.filter(
        recipient=request.user
    )
    user_budget = User_budget.objects.filter(
        user=request.user
    )
    
    #all category
    MoneyTransfer  = User_budget.objects.filter(
        user=request.user, category = 1
    )
    Restaurant = User_budget.objects.filter(
        user=request.user, category = 2
    )
    Transportation = User_budget.objects.filter(
        user=request.user, category = 3
    )
    Shopping = User_budget.objects.filter(
        user=request.user, category = 4
    )
    Services = User_budget.objects.filter(
        user=request.user, category = 5
    )
    Leisure = User_budget.objects.filter(
        user=request.user, category = 6
    )
    Health = User_budget.objects.filter(
        user=request.user, category = 7
    )
    Grocery = User_budget.objects.filter(
        user=request.user, category = 8
    )
    Utility = User_budget.objects.filter(
        user=request.user, category = 9
    )
    

    #total of budget and spending
    total_budget = budget.aggregate(total_budget=Sum("item_price")).get('total_budget')
    total_spending = spending.aggregate(total_spending=Sum("item_price")).get('total_spending')
    total_exclude = exclude.aggregate(total_exclude=Sum("amount")).get('total_exclude')
    #set day range
    startdate = date.today().replace(day=1)
    days_in_month = calendar.monthrange(startdate.year, startdate.month)[1]
    #set to only show day range's data (summary)
    budget = budget.order_by("-id").filter(timestamp__range=[startdate, startdate + timedelta(days=days_in_month)])
    spending = spending.order_by("-id").filter(timestamp__range=[startdate, startdate + timedelta(days=days_in_month)])
    exclude = exclude.filter(timestamp__range=[startdate, startdate + timedelta(days=days_in_month)])
    user_budget = user_budget.filter(timestamp__range=[startdate, startdate + timedelta(days=days_in_month)])
    #set to only show day range's data (category)
    MoneyTransfer = MoneyTransfer.filter(timestamp__range=[startdate, startdate + timedelta(days=days_in_month)])
    Restaurant = Restaurant.filter(timestamp__range=[startdate, startdate + timedelta(days=days_in_month)])
    Transportation = Transportation.filter(timestamp__range=[startdate, startdate + timedelta(days=days_in_month)])
    Shopping = Shopping.filter(timestamp__range=[startdate, startdate + timedelta(days=days_in_month)])
    Services = Services.filter(timestamp__range=[startdate, startdate + timedelta(days=days_in_month)])
    Leisure = Leisure.filter(timestamp__range=[startdate, startdate + timedelta(days=days_in_month)])
    Health = Health.filter(timestamp__range=[startdate, startdate + timedelta(days=days_in_month)])
    Grocery = Grocery.filter(timestamp__range=[startdate, startdate + timedelta(days=days_in_month)])
    Utility = Utility.filter(timestamp__range=[startdate, startdate + timedelta(days=days_in_month)])
    #total of budget and spending
    total_budget = budget.aggregate(total_budget=Sum("item_price")).get('total_budget')
    total_spending = spending.aggregate(total_spending=Sum("item_price")).get('total_spending')
    total_exclude = exclude.aggregate(total_exclude=Sum("amount")).get('total_exclude')
    #if there's no transaction
    if total_exclude != None:
        total_exclude = total_exclude
    else:
        total_exclude = 0
    if total_budget != None:
        
        total_budget = total_budget
    else:
        total_budget = 0
    if total_spending !=None:
    
        total_spending = total_spending - total_exclude
    else:
        total_spending = 0

    total = total_budget + total_spending
    #total of each category
    MoneyTransfer = MoneyTransfer.aggregate(total_exclude=Sum("amount")).get('total_exclude')
    Restaurant = Restaurant.aggregate(total_exclude=Sum("amount")).get('total_exclude')
    Transportation = Transportation.aggregate(total_exclude=Sum("amount")).get('total_exclude')
    Shopping = Shopping.aggregate(total_exclude=Sum("amount")).get('total_exclude')
    Services = Services.aggregate(total_exclude=Sum("amount")).get('total_exclude')
    Leisure = Leisure.aggregate(total_exclude=Sum("amount")).get('total_exclude')
    Health = Health.aggregate(total_exclude=Sum("amount")).get('total_exclude')
    Grocery = Grocery.aggregate(total_exclude=Sum("amount")).get('total_exclude')
    Utility = Utility.aggregate(total_exclude=Sum("amount")).get('total_exclude')

    return render(request, "budget/budget.html", {
        "spendings":spending,
        "budgets":budget,
        "total_budget":'{:0.2f}'.format(total_budget),
        "total_spending":'{:0.2f}'.format(total_spending),
        "total":'{:0.2f}'.format(total),
        "total_moneyTransfer":MoneyTransfer,
        "total_restaurant":Restaurant,
        "total_transportation":Transportation,
        "total_shopping":Shopping,
        "total_services":Services,
        "total_leisure":Leisure,
        "total_health":Health,
        "total_grocery":Grocery,
        "total_utility":Utility,
        
    })

#API call for adding spending function
@csrf_exempt
def spending_function(request):
    #user self posting budget
    if request.method == "POST":
        data=json.loads(request.body)
        budget = Budget(
            user=request.user,
            timestamp=data["time"],
            item=data["item"],
            item_price=data["item_price"],
            category=Category.objects.get(pk=data["category"])
        )
        #make sure all enteries are not empty
        if data["time"] == "":
            return JsonResponse({
                "error": "Time required."
            }, status=400)
        if data["item"] == "":
            return JsonResponse({
                "error": "itme name required."
            }, status=400) 
        if data["item_price"] == "":
            return JsonResponse({
                "error": "price required."
            }, status=400)
        if data["category"] == "":
            return JsonResponse({
                "error": "category required."
            }, status=400)
        budget.save()
        user_budget = User_budget(
            user=request.user,
            amount = data["item_price"],
            category = Category.objects.get(pk=data["category"]),
            timestamp= data["time"],
        )
        user_budget.save()
        category = Category.objects.get(pk=data["category"])
        new = User_budget.objects.get(pk=user_budget.id)
        category.add(new)
        
        return JsonResponse({"message": "Item added"}, status=201)
    return JsonResponse({
        "error": "GET or POST request required."
    }, status=400)