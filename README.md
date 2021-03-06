# Fin
> Fin is a mobile responsive fintech web application for the user to track their spendings and manage their money.

&nbsp;

![budget page](https://github.com/nathanieltse/Fin/blob/main/budget/asset/budget%20page.png?raw=true)

&nbsp;
# Stack
This application is built on Python Django framework with SQLite as back end and Javascript as front end with bootstrap library.

&nbsp;
# Understanding
In the source code is a Django project called `Fin` that contain a single app called `budget`.

&nbsp;

Inside `budget`, `models.py` has 7 database models : 
* `User` for user account data

* `Account` for user's money records

* `Spending` for user's transaction records

* `Category` for system's category options

* `Transfer` for transfering records

* `Budget` for user's self tracking spending records

* `User_budget` for user's spending record from all sources

&nbsp;

`admin.py` takes in all 7 models database and displays them in lists in the back end site for site admin.

&nbsp;

`urls.py` has 9 paths for all functions like :
* landing page

* logging in

* logging out

* registering

* transfering

* accepting money transfers

* welcome page

* account transaction page

* budget planning page

&nbsp;

`url.py` also has two API calls for posting transfering records and letting user add their spending records.

&nbsp;

`views.py` contains functions that are associated with each route. 

* The `greeting` view renders the greeting page for user who are not logged it.

* The `index` view renders the landing page once user are logged in, and if user doesn't have a spending account they would be presented with option to open one. The `index` view checks if user has transfer from other people and notify user to accept transfer, the `index` view also calculates user's total spending of the month and renders on the `index` page.

* The `login_view` view renders the login page for user log in.

* The `logout_view` view return user to landing page when logged out.

* The `register` view let user registers an account and ensure they meet account information requirements.

* The `transfer` view renders the transfer page. The function checks if user has a spending account and present them option to open one. The function also checks if user has transfers from other people and notify user to accept transfer.

* The `accept` view is a function to let user accepts any incoming transfer and checks to make sure it's the intended recipient accepting the transfer and transfer has never been recieved before user does.

* The `transfer_function` view is an API call function to let user transfers money out.It checks to make sure recipient exsists, user has enough fund in account and the form is filled out with required informations for user to transfer money to other account. 

* The `spending_view` view renders the spending account's transaction records.

* The `budget_view` view renders the budget page that shows user each of the category spending for the month and it's total individually. It also renders all records of the month and splits it into spending account records and user's self tracking records.

* The `spending_function` view is an API call function that takes user's request to track their spendings from the budget page. It ensures the form is properly filled out to be able to post the data to the databases.

&nbsp;

For static file, it hosts custom CSS file for styling and two Javascript files for different pages.

`fin.js` has an eventlistner for submitting form for user to tansfer money to the `transfer_function` API.

`budget.js` is specfically for the budget page. 

* When user clicks the Add item button it calls the `add_item` function and displays a form in the browser for user to fill out. The `add_item` function checks to make sure form is not empty otherwise the submit button would be disabled and display a message for user that all fields need to be filled out

* When user clicks the submit button it calls the `add_btn` function and calls the API to post all the input to the databases.

* The `show(button)` function takes in each category box(button) as argument and is called when user click on one of the category boxes. The function would remove all irrelavent spending records and only shows records that matches the category that user picked. It also presents a returning route when category boxes are clicked for user to display all records again.

&nbsp;

# Webpage template
> Greeting page prompt for user who are not logged in

&nbsp;

![Greeting page](https://github.com/nathanieltse/Fin/blob/main/budget/asset/greeting%20page.png?raw=true)

&nbsp;

> landing page after users are logged in with options to open a spending account.

&nbsp;

![landing page](https://github.com/nathanieltse/Fin/blob/main/budget/asset/newuser%20landing%20page.png?raw=true)

&nbsp;

> landing page after user opens a spending account and able to access all functions and shows user their monthly spending total and account balance.

&nbsp;

![landing page2](https://github.com/nathanieltse/Fin/blob/main/budget/asset/landing%20page.png?raw=true)

&nbsp;

>landing page when user has an incoming transfer notification and option to accept.

&nbsp;

![landing page3](https://github.com/nathanieltse/Fin/blob/main/budget/asset/landing%20page.%20new%20transfer.png?raw=true)

&nbsp;

>account page that shows all transaction records 

&nbsp;

![account page](https://github.com/nathanieltse/Fin/blob/main/budget/asset/transaction%20page.png?raw=true)

&nbsp;

>budget page that shows user their monthly total spendings and each category's breakdown. Add item button for adding spendings for tracking and all this month's spending records and transaction records from spending account

&nbsp;

![budget page](https://github.com/nathanieltse/Fin/blob/main/budget/asset/budget%20page.png?raw=true)

&nbsp;

>When category button is selected the browser will only display selected category's spending and present a Show All button to show all records again.

&nbsp;

![budget page2](https://github.com/nathanieltse/Fin/blob/main/budget/asset/category%20filter.png?raw=true)

&nbsp;

>When add item button is clicked, brower would render a form for user to track their spendings, submit button is disabled until all fields are filled out with a message reminder.

&nbsp;

![budget page3](https://github.com/nathanieltse/Fin/blob/main/budget/asset/add%20budget%20form.png?raw=true)

&nbsp;

>Transfer page for user to fill out transfer request and records of all past history.

&nbsp;

![transfer page](https://github.com/nathanieltse/Fin/blob/main/budget/asset/transfer%20page.png?raw=true)

&nbsp;

>When user recieves an incoming transfer, notification would pop up for user to accept the transfer.

&nbsp;

![transfer page2](https://github.com/nathanieltse/Fin/blob/main/budget/asset/transfer%20page.%20new%20transfer.png?raw=true)
