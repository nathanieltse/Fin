document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#add-item').addEventListener('click', add_item);
    document.querySelectorAll('#category-box').forEach((button) => {
        button.addEventListener('click',() => {
            show(button)
            
        })
    });
});

//adding box appear
function add_item() {
    //disable add botton
    document.querySelector('#add-item').disabled = true;

    const form = document.createElement('form');
    const date = document.createElement('input');
    const item = document.createElement('input');
    const item_price = document.createElement('input');
    const category = document.createElement('select');
    const opt1 = document.createElement('option');
    const opt2 = document.createElement('option');
    const opt3 = document.createElement('option');
    const opt4 = document.createElement('option');
    const opt5 = document.createElement('option');
    const opt6 = document.createElement('option');
    const opt7 = document.createElement('option');
    const opt8 = document.createElement('option');
    const opt9 = document.createElement('option');
    const subcontainer1 = document.createElement('div');
    const subcontainer2 = document.createElement('div');
    const subcontainer3 = document.createElement('div');
    const subcontainer4 = document.createElement('div');
    const submit = document.createElement('input');
    const message = document.createElement('p');

    //all placeholder
    date.placeholder= "Date YYYY-MM-DD";
    item.placeholder= "What was the spending?";
    item_price.placeholder= "Price";
    submit.type="submit";
    submit.value="Add";


    //all selection for category
    opt1.attributes= "selected disabled"
    opt1.innerHTML="Pick a category";
    opt1.value="";
    opt2.innerHTML="Resutaurant";
    opt2.value="2";
    opt3.innerHTML="Transportation";
    opt3.value="3";
    opt4.innerHTML="Shopping";
    opt4.value="4";
    opt5.innerHTML="Services";
    opt5.value="5";
    opt6.innerHTML="Leisure";
    opt6.value="6";
    opt7.innerHTML="Health & beauty";
    opt7.value="7";
    opt8.innerHTML="Grocery";
    opt8.value="8";
    opt9.innerHTML="Utility";
    opt9.value="9";

    // putting all elements together
    subcontainer1.append(date);
    subcontainer2.append(item);
    subcontainer3.append(item_price);
    category.append(opt1,opt2,opt3,opt4,opt5,opt6,opt7,opt8,opt9)
    subcontainer4.append(category);
    form.append(subcontainer1, subcontainer2, subcontainer3, subcontainer4, submit, message);
    document.querySelector('#add_item').append(form);

    //class and id
    form.classList.add(
        "border",
        "rounded",
        "px-5",
        "py-5",
        "mb-3"
    )
    subcontainer1.classList.add(
        "form-group",
    );
    subcontainer2.classList.add(
        "form-group",
    );
    subcontainer3.classList.add(
        "form-group",
    );
    subcontainer4.classList.add(
        "form-group",
    );
    date.classList.add(
        "form-control",
    )
    item.classList.add(
        "form-control",
    )
    item_price.classList.add(
        "form-control",
    )
    category.classList.add(
        "form-control",
    )
    submit.classList.add(
        "btn",
        "primary-color-btn",
    )
    message.classList.add(
        "message"
    )
    form.id = "add_item_form";
    date.id = "date";
    item.id = "item";
    item_price.id = "price";
    category.id = "category";
    message.id = "message";
    submit.id = "submit-btn"
    
    //check empty field
    if (document.querySelector('#date').value == "" || document.querySelector('#item').value == "" || document.querySelector('#price').value == "" || document.querySelector('#category').value == "" ){
        document.querySelector('#message').innerHTML = "Field can't be empty"
        document.querySelector('#submit-btn').disabled = true ;
    } 

    document.querySelector('#add_item_form').addEventListener("change", () => {
    if (document.querySelector('#date').value == "" || document.querySelector('#item').value == "" || document.querySelector('#price').value == ""|| document.querySelector('#category').value == ""){
        document.querySelector('#message').innerHTML = "Field can't be empty"
        document.querySelector('#submit-btn').disabled = true ;
    } else {   
        document.querySelector('#submit-btn').disabled = false ;
        document.querySelector('#message').innerHTML = ""
    }})
    //submit function
    document.querySelector('#add_item_form').addEventListener('submit', add_btn)
}

//API call to call to budget
function add_btn() {
    
        fetch('/spendingfunc',{
            method:'POST',
            body:JSON.stringify({
                time:document.querySelector('#date').value,
                item:document.querySelector('#item').value,
                item_price:document.querySelector('#price').value,
                category:document.querySelector('#category').value,
            })
        })    

}

//category filtering function
function show(button) {
    const all = document.querySelectorAll('#category-box');
    const allbudget = document.querySelectorAll('#budget-box, #spending-box');
    const total = document.querySelectorAll('#subsummary');
    //reset all buttons
    all.forEach((button)=>{ 
        button.setAttribute("class","category-box px-3 py-2 pb-0 my-2 mx-4");
    });
    allbudget.forEach((box)=>{ 
        box.setAttribute("class","d-flex flex-row justify-content-between py-4 px-5 my-3 border rounded");
    });
    
    //hide total
    total.forEach((box)=>{
        box.setAttribute('class','')
        box.style.display="none"; 
    })
    //button change color
    button.setAttribute("class","category-box-active px-3 py-2 pb-0 my-2 mx-4");

    //category filter transaction boxes
    const category = button.getAttribute("data-cat");
    const budget = document.querySelectorAll('#budget-box');
    const spending = document.querySelectorAll('#spending-box');

    budget.forEach((box)=>{
        if (box.getAttribute("data-cat") != category) {
            box.setAttribute('class','')
            box.style.display="none";
            
        } else {
            
            box.style.display="block";
        }
    });
    spending.forEach((box)=>{
        if (box.getAttribute("data-cat") != category) {
            box.setAttribute('class','')
            box.style.display="none"; 
        } else {

            box.style.display="block";
            
        }
    });
    //add return route
    if (document.querySelector('#return') != null) {

    } else {
        const back = document.createElement('div');
        const text = document.createElement('p');

        text.innerHTML = "Show all";

        back.append(text)
        document.querySelector('#summary').append(back)

        //all class
        back.classList.add(
            "category-box",
            "py-2",
            "my-4", 
            "mx-auto"
            
        )
        text.classList.add(
            "category-text",
            "my-0",
            "text-center"
        )
        back.id = "return"
    }
    //back button function
    const backButton = document.querySelector('#return');
    
    backButton.onclick = () => {
        location.reload();
    };
}

