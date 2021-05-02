# Fin
> Fin is a mobile responsive fintech web application for the user to track their spendings and manage their money.

&nbsp;

![budget page](https://lh3.googleusercontent.com/JQ1FgCEjYzy50i-ls6hnIorzlaPwkrgI1rntteDmnfQ9r7_omIen7zJv05Go84ghAJfW7uoSIkLyednbpvx5-TZgNkTlV5o7phHwqZySe5je9a7fTmnm8XDgAqDwbrkNZO7Vonxc5_KFeRmTCYC9RRkBgGZlFD0Sc3nk4rhpQrT9FOE75zUsXvqlrnMs5HQa9wkL93lp9LBz2ugSxRwhDLRe9okR4oBrf6rFwH0f_faML7EZM3Cr6jNLOxzDOTA3C7Rb5c5UIFcwXUf3MG3g2j2ZlCaL-HzbF4X5y_gcTxMPxTtMGiQMNjDH2YC6w8b9PizsfbyOwbddpcbhxd9lKOWcdr0BacOxNbV7AXDECPR07OMIJQBz3txy4tpmn1CJdxa34bgzL-9KTUOXfzSCHF8d9-Ux8RevpW8vaZVRpEyTRPVXoA8Jb9Bz4jZK8XGFyTZOZTaLnMvWTdCdGRMt7BJdhzMUvh71BXUbtuX5r1Hd1P6zYCP0T27FFCzsY8tjOnqqGfr8UxfKk0d1iM4KWIjh3_z4vKZ5ag_ppU8w7AiCb2DKF0F-S_-9oALLDrArWRDUtD0qN9iteH8g3PcFL0ghSdd4DYHpqScchHgi_2boZpxKUym9MJ0KeiCKeRUaNyksPZVIQ0M1-brDzOo-m8TCDtikqltW-sOEGmz5YChKsuyXcLsAJyoEqz-kwzUM_Sg9GxN8YQsKA83xFd_46sJD=w3148-h2100-no?authuser=0)

&nbsp;
# Stack
This application is built on Python Django framework with SQLite as back end and Javascript as front end with bootstrap library.

&nbsp;
# Understanding
In the source code is a Django project called `capstone` that contain a single app called `budget`.

&nbsp;

Inside `budget`, `models.py` has 7 database models : 
* `User` for user account data

* `Account` for user's money record

* `Spending` for user's transaction record

* `Category` for system's category options

* `Transfer` for transfering record

* `Budget` for user's self tracking spending record

* `User_budget` for user's spending record from all sources

&nbsp;

`admin.py` takes in all 7 models database and displays them in lists in the back end admin site for siteadmin.

&nbsp;

`urls.py` has 9 path for all functions like :
* landing page

* logging in

* logging out

* registering

* transfering

* accepting moeny transfers

* welcome page

* account transaction page

* budget planning page

&nbsp;

`url.py` also has two API call route for posting transfering record and letting user add their spending record.

&nbsp;

`views.py` contains functions that are associated with each route. 

* The `greeting` view renders the greeting page for user who are not logged it.

* The `index` view renders the landing page once user are logged in, and if user doesn't have a spending account they would be presented with option to open one. The `index` view checks if user has transfer from other people and notify user to accept transfer, the `index` view also calculate user's total spending of the month and renders on the `index` page.

* The `login_view` view renders the login page for user log in.

* The `logout_view` view return user to landing page when logged out.

* The `register` view let user registers an account and ensure they meet account information requirements.

* The `transfer` view renders the transfer page. The function checks if user has a spending account and present them option to open one. The function also checks if user has transfer from other people and notify user to accept transfer.

* The `accept` view is a function to let user accept any incoming transfer and checks to make sure it's the intend recipient accepting the transfer and transfer has never been recieved before user does.

* The `transfer_function` view is an API call function to let user transfers money out.It checks to make sure recipient exsists, user has enough fund in account and the form is filled out with required information for user to transfer money to other account. 

* The `spending_view` view renders the spending account's transaction record.

* The `budget_view` view renders the budget page that shows user each of the category spending for the month and it's total individually. It also renders all records of the month and split it into spending account record and user's self tracking record.

* The `spending_function` view is an API call function that takes user's request  to track their spending from the budget page. It ensures the form is properly filled out to be able to post the data to the database.

&nbsp;

For static file, it hosts custom CSS file for styling and two Javascript file for different pages.

`fin.js` has an eventlistner for submitting form for user to tansfer money to the `transfer_function` API.

`budget.js` is specfically for the budget page. 

* When user click the Add item button it calls the `add_item` function and display a form in the browser for user to file out. The `add_item` function check to make sure form is not empty otherwise the submit button would be disabledand display a message for user that all fields need to be filled out

* When user click the submit button it calls the `add_btn` function and call the API to post all the input to the database.

* The `show(button)` function take in each category box(button) as argument and is called when user click on one of the category boxes. The function would remove all irrelavent spending records and only shows records that matches the category that user picked. It also presents a returning route when category boxes are clicked for user to display all records again.

&nbsp;

# Webpage template
> Greeting page prompt for user who are not logged in

&nbsp;

![Greeting page](https://lh3.googleusercontent.com/pasgQ3w05Sf9IC8faVnZx-CVEEZtg5knq1_5S7uwlEHqNbe9276RGGLvb20mu1X08YdXfHDJf2qgZwr6gijhabwwCiKlgNvKzNa7Enq_MqX_vbgn_XeNNYVT235IgEckpJO6TDhTABxqUjBIbV33cQxXbiNihRAvVqUrTYPL9LM9aLvkkUXnfmzarpxiMXH2cMVQzEfafZwg1b8o0qVyO7W9P-o62PAwL2s6zfKhkpk_PfNKZ1ZXMALCQeiFSlB6v6IiP9mmOBRiMhHm5IHN6gpR35kWa7UBp9s-302YArepj3uQVW0hrWImpUEtC4XpZK8hkJHSyLNLOa4Rs3Xa3muCBzH7pTxJoWPOdOZ6h--DBFYrr3NC4g_JgNxF0_7mIcFW4vNG3JdFor5MUAuJ4Ov8yt9RO5KQ5zsbWQfBrs_STmj29R49KDY_Iw0ugaYnKwt6kQqQgzEyltgwUc91DKIH78Tkk0rD-_v0TEUITnfg6gS-Za-4gb3H2fwiY9DRuYElkcUdDPam1iSheBZdkVt9AQ2HwLxe40myIHQw7g2njzHGAq7v9dT-e5T0x1CKXgjirrGk1K17_l2QwiGkmjT3VkOtFXDcmlRO4qWqx7fHSYAxAIWkVbTKtOHd-HlQpDvL2ksxJfYoyY5IeZF6LEZE3jhZyjTxbkSO9BekCMV9UdxGzdE_tG3sk8_4mlzFotLAXeewph5yKMmnQJvcj8Ty=w3060-h2132-no?authuser=0)

&nbsp;

> landing page after users are logged in with options to open a spending account.

&nbsp;

![landing page](https://lh3.googleusercontent.com/pw/ACtC-3dIDUarkh-4j_IP2M6RL1hTpo80S5iwaKe6kiQMkNagjyleB82MTlO1ZWaeNeN1lerUyw26Jz1BQERW3n7jr1BjsMRrZ7-ufNGatSOs8lMXmwCbDlLIx0a89f_ftTG39Kn3VSv-1FEhzJfABCnJYA81=w3138-h2155-no?authuser=0)

&nbsp;

> landing page after user opens a spending account and able to access all functions and shows user their monthly spending total and account balance.

&nbsp;

![landing page2](https://lh3.googleusercontent.com/pw/ACtC-3fDkRDwH46Syrhhx4Gs-eFE7JXh_hwRRrgRekS2KYF-cPnWll8dA_QIDWYdDORnJdmQbXYnLA8ahj0c4-XLYeaL__AONZLCoTmQ3hfyaweK6oKY2d2lCgTiohx8SgI_1KYM-i4R5LjgCt0j6cYi_5Vz=w3148-h2096-no?authuser=0)

&nbsp;

>landing page when user has a incoming transfer notification and option to accept.

&nbsp;

![landing page3](https://lh3.googleusercontent.com/XnmqKzeH9sPiNlvotnhcKa5Zh9Rs4mDrvmcjSfcZHrX5m008TpRrHsiL_qaHwsZVE7wJm_r7HDxdJb18kklSLggSPaHw0eQH17vc9jPPOy26v9xbYQWnwkPB4gEmhR3MGiyStXPcpnLHi8WjqvbukDyGgXVbxLbePMukOvHHbad_L-ptCwP9YiAgTY0MAz2dxJbW_7TxD99taXOIcNqmvu8J9XgYL5OIK6oCQNSJF4xtUYbipa9qLB3NeRitkChltAq7yvQTy_xgRgaSjSy21_DHAbX_Zyz_sXHiscmeiVYhxQNqw1zktLe-nvuD96WjvWd7dFwdH9naWDks4H1RVpMmBPt5ly3hvyjLmnPpfbhK6s6K6bb4-iWkzPlDHlLWapF4CPH1_hXAmKeWUt8M6J9H-_pGJQ7NM7yhFmT_a_PDo77Gn4iyCN5nHpBQ1ulm2LIxbsjcrN_adelGxXOOJEPNKsEtQ2lWw61RAo_jUhnHqv3Z0Pw6x4LO6CbYXpLEWXdojrTbfCIDPkc4gxUkfrlookdKdyYMI01ZQKGKOzZPANHY_UsJavjBENDv3YEvALSkfhq2e4petdbadLJJyBoLjwESzscJimkkcgKXqsZAbCMoljNchtL9LzAE5MOTthjxTiHDXTzMPb-xEC-bTCcpJTmnp7bNGJ_jd_aykGcHKBKvB22ro0xlBYOHM0wSTtkU3w29H7RUinRGTNno289Q=w3148-h2098-no?authuser=0)

&nbsp;

>account page that shows all transaction records 

&nbsp;

![account page](https://lh3.googleusercontent.com/gvzF8VYj5glUi-maOs46Ah2aoJc2xVWq4LOuzOYUVVspXh_vrqSgm74ThSTi_5mt52jeS5x_1DkgawhzFV77fIpE1hPsNmIXiYqnqqGJEhlFpv1htHSAMKNXlRbev3jlg40933BmXcJaeTrC4oqTuIVxuOszHCpr2yOxZS7rwaNFb9tYiqkjYnhLtWH1rPMxQsZDAt7bZq6HZlZdSDdEt_wV9B8XwAgA0jdho38j_dSj9OHKeyZxbWmBvO6uKL0XeajymNQXXtW7nghImKcHBKUsccYGinRWtXxUwDb2AXXzsU0q9j0eZl6U6BRHqHaz6ChYzg9I11JM9hv8LIgkmfxNLz_iD0Wjo9vEcE4FE1m10pE7icfSqxx-EQj8Y7ss81zRz1ki99oao70NBOFbymSoKpYlv9U6IDhyB7MxjVFs54KgVRVwvc4y_MgLXYbwZtKHPq6CrZivAPZ0VG9vfDZD1frhfWwYLPVlvNMhiHTdJ0obYKgdOHQRkGJR5NI4k0xK_tfRehz_b0Vy1lYN6Xg9TogRn4tTxa0myJTeHzHrAPsQd79ybaX-zQqm6tuqEirBahPD3ydYFboDSRQqjDvH_8cxOzdv6ZusBIr_3WsDIO_TUhfdiOrIwJDabpnN3OlzWY8kfrszqOs4fYHnkjIs48-Eq72DHQaapJAGt0iYb8VreIFujdwZagHrt0nZsU84QGNXw7hrYKEq9iZfPQZY=w3148-h2104-no?authuser=0)

&nbsp;

>budget page that shows user their monthly total spending and each category's breakdown. Add item button for adding spending for tracking and all this month's spending records and transaction records from spending account

&nbsp;

![budget page](https://lh3.googleusercontent.com/JQ1FgCEjYzy50i-ls6hnIorzlaPwkrgI1rntteDmnfQ9r7_omIen7zJv05Go84ghAJfW7uoSIkLyednbpvx5-TZgNkTlV5o7phHwqZySe5je9a7fTmnm8XDgAqDwbrkNZO7Vonxc5_KFeRmTCYC9RRkBgGZlFD0Sc3nk4rhpQrT9FOE75zUsXvqlrnMs5HQa9wkL93lp9LBz2ugSxRwhDLRe9okR4oBrf6rFwH0f_faML7EZM3Cr6jNLOxzDOTA3C7Rb5c5UIFcwXUf3MG3g2j2ZlCaL-HzbF4X5y_gcTxMPxTtMGiQMNjDH2YC6w8b9PizsfbyOwbddpcbhxd9lKOWcdr0BacOxNbV7AXDECPR07OMIJQBz3txy4tpmn1CJdxa34bgzL-9KTUOXfzSCHF8d9-Ux8RevpW8vaZVRpEyTRPVXoA8Jb9Bz4jZK8XGFyTZOZTaLnMvWTdCdGRMt7BJdhzMUvh71BXUbtuX5r1Hd1P6zYCP0T27FFCzsY8tjOnqqGfr8UxfKk0d1iM4KWIjh3_z4vKZ5ag_ppU8w7AiCb2DKF0F-S_-9oALLDrArWRDUtD0qN9iteH8g3PcFL0ghSdd4DYHpqScchHgi_2boZpxKUym9MJ0KeiCKeRUaNyksPZVIQ0M1-brDzOo-m8TCDtikqltW-sOEGmz5YChKsuyXcLsAJyoEqz-kwzUM_Sg9GxN8YQsKA83xFd_46sJD=w3148-h2100-no?authuser=0)

&nbsp;

>When category button are selected the browser will only display selected category's spending and present a show all button to show all records again.

&nbsp;

![budget page2](https://lh3.googleusercontent.com/MInO5bU6uVE5A_4bd9Bd9lkmJ64reKsphg1vx2nWhiwWzV23TRSFyOrEGfyi1m5T4gmta0yUxB8OodemvpjMbVxfh4Ei9APOyGxB_YHQtxMti47qRlbTq_DtSsbkRrYqw36pFB4GOS9GD4gHdUwqj1jlcRttyBrQUnZWGZmQ8cngS2J_40FM96-yFmuezBcy2Wt3Nd39lQaaBXU2vJ-sdH5m0pOBBm73AMTSXOf3_zm2p9aU-I_I77dZfEHx_s_Gn5JN1idFqU9BRQeEDnP82XqpbfuDB1dFx0hK7AxVSECqSZxjlFqCw07sC1iaV6PZLpYg5uxmiy0MSj3FeNTIEV8ubYaloMZOywvPdQub84lvxWqePQ_HE_OyhFb56Ap3qzFrInZqCi971EvaPpOkApTrgntmY3Gu-g5BnYK98PPIIZP4rGCkhlQuDWWC_8_nyo6Ga2zuYYRHn204mKzUYraTSGFlZ1rRzvhFcp7NERlGJcyG0w4h2MaHCq2qy-LEQdB9npHj5V-ogcq7zuIx1WeOqa9js_2fyJ_LTuTLVA_xjyvyxL381dFsnv1TlBCHaYnY_XDrMfB4__hS2PsKhj8b0LjOymxVML8sgnOtdu_m1MKjCQz7TLY8EenQCMYknatCeB9nVnD4nzZma6LPpgtQb2fb3rtjqcwpH6Ejdam-4ZG8h9-_hSf6nvavbMk_cVVH0V11KcEX6Twfg6RILfj9=w3148-h2098-no?authuser=0)

&nbsp;

>When add item button is clicked, brower would render a form for user to track their spending, submit button is disabled until all field is filled out with a message reminder.

&nbsp;

![budget page3](https://lh3.googleusercontent.com/6hY8YP_uCeciLzD1xN_QoqdMrt2EyXwlQrO5NDe4SHP9YzW2eVNNKJQ9qbbVqmzD2Yfp-_TdFg4RSU3ogG7Su2UxZIdv-25ZXNB9jH6mGYZkgNAUU-yQ3ssIUzYCulz6pbMev_wyU2yd2Pt_9PGo2bk-ZO7xaezNMjBqr76WghInYDDIYqZjx-E-EsL2MleCb6VP3HhTpjKI6M6fGG17qoeOuzNSfHh4mm1LFIG7a_1Aj6yLzXHhKlGlW8uSICDvn4PPjhVJjcx0k-H38oCvqfUqnW0N44Yb82uPLKvAHQIXwD5Q2oBL0YPlZp7-2DJQB8QM1furE-fBzhQC8n9fU5Fi-bDAMFD80M0fkgeAZGrtOFSCdjf7_ohpAro2fqixPmOrwmeVVPZyw8PS3l0wEoE_M12jhSVkFW7p9f_gOr62Z1Xqz-mPPGqNfQkXSR9sofsiKLC7oOJsluol-ZIq5vg49tFL_vM8ESB5b8sCgEQF133yIELO0UbjubGE5s5EKdNM1jYNyhPvBhg4uyV7ZEoYwt4D9MrOC_D_LayV0KY8YWdZXnq3BI_kNfCTyQzLr_LCIF5IwMegwCbHv__-O1P3nSYPayDOs1WKUvswT3uRIVF5novS9J-4Ah9m_WC0M4_Ogouz4XZz-UuB5vlUgENAZeoSYWoSb2m-4ad2Q6WnVjsIGqGnp1CA6EbsoY5iS9h92mUixD0n7pyooMUxT_FA=w3148-h2096-no?authuser=0)

&nbsp;

>Transfer page for user to fill out transfer request and records of all past history.

&nbsp;

![transfer page](https://lh3.googleusercontent.com/Wvoy2-wXdLzvEM570VABr3N0sWgxAZNRgnWcx-z-J8L9hfSE_0K2TMyxMm3bavb6SQX4serzJP-Py601du_m1aZw6kJjFaUzSHWlrtmIayFMem0HIEhkDG3oaillxpzhjuXADqOnwt_EyI1HwYi-XNPK3BhbdHEj2BrMjmOJWOeXoWQJnQdDxyRENBmlNorWf9zFa7IlL-J0sDDiTDA8v_4oYiawyownmjsliaQ8lf4hoCpcL_ywIUZmJhIRtdKcHx6_Kxya4JlkBkDORJ_y7rDIbAfENhmJUrRycs2yzri2EDdHmUzGys7UHvvv46W_qfIKfGQBZGTwZXcWvXD7-540R42OS4WUZSiB1V38ju8W83q8dspx5FlmtdJgHiH2nt9Aige3F0k7Q40EjA-zYBGpRh2nylRbcXvRXT9VhqFRV82WDFWdw2-LP824L2KQiILn5G3nZLTjX4ZWjvOtM3pFYxXK8QUIG7gCRFmLQdKsKiqPXw9lPNl_cJ-bHl_3hnLMFZAGgB9O-7q3sZ7xsdM5o4kV9H53h-ciY-IFkmzaj3VJDNAW6FC949zLrsQC82jOfZze6gWRbD4S-6_g3mC58CamnYDRvXRzT5wOXEeyA2DyLqZr13hO6cys5DBxFKuwj5GvxRdgyFqlS7fj3Sndl1gdsbEaWO_USVRYxu39mKk4EFcZH-APQS_r3DvKgYhPln8z9b-1EhzaYJ0WfFbd=w3148-h2092-no?authuser=0)

&nbsp;

>When user recieve an incoming transfer, notification would pop up for user to accept the transfer.

&nbsp;

![transfer page2](https://lh3.googleusercontent.com/aUxOSaxTOcMQOkqUsDi2Pr-Nv70MxyeAEpkXCLoR2ttQYr2KIYS2dhfRUfhXLXzlrzv6bzWSbdOpLF0rVlJVVnBjjeV-fITF0nbavfDn9uUV6sH4XJEFZ7VvNSsN41CaM5Gf5fHRhgF682aQMslzI7qhfMdgC5JYyASeEf6BAubtKh7UlnpXIm80WA_RxR706WlJkt9NhUC2WBX4_hjMI5f7m3AoSzOGKqhvsHilXfQDJSyOvgvPKL2VFE0oOin3jz0VvBbusaSJiu2f-045dQYZaGO8xkbgF8Gm9hsAQZt0IjOiX39azgdfMRZoNbb-QJ5fPw8-CJLMUTB25EyJT65rHHBZY69NLcKKqeaP71MV5ehWsgtzU0hUAvsb-voDUHvsfWDlMbr8oiogf6J2j02a-oYYYozFIlE83yR3Lu7oRjYLw8r0Xe_5eBIjO7KfnYkpUBDyTbA_RCjdmJFht37YQqawZIgDIc0t72yBQfZObNm-sR-1_IzFCN69H6TysjyPzEFe-iJ53dOJHgL_jReDSPsRHybs1BxhOKLMyYXJ6-1q1COou8aLb57S5TuyzEUWmTcsN-GW31AASuMUj5KPee_FbYSzUGZ7PG8sC2EY2h0XfugHjGWqAav7lGAq7SBcL5jqA1YqZfxN3GkApwiwu-dEBr2mAWiD_jbEC4Zv6oyNy9evPaeiblyuRKRj_4IzeqEU7fFhwCjAR5udsYHU=w3148-h2094-no?authuser=0)
