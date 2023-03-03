const url = "http://localhost:3030/jsonstore/grocery/"; 
const addProduct = document.getElementById("add-product");
const loadProduct = document.getElementById("load-product");
const updateProduct = document.getElementById("update-product");

const productName = document.getElementById("product");
const productCount = document.getElementById("count");
const priceProduct = document.getElementById("price");

const tableBody = document.getElementById("tbody");

function attachEvents() {
addProduct.addEventListener("click", adding);
loadProduct.addEventListener("click", loading);
// updateProduct.addEventListener("click", updating)

}


function adding(event) {
    // if (event){
    event.preventDefault();
    // }
    let product = productName.value;
    let count = productCount.value;
    let price = priceProduct.value;

    if (product, count, price) {
        data = {
            "product": product,
            "count": count,
            "price": price
        }

        productName.value = "";
        productCount.value = "";
        priceProduct.value = "";

        fetch(url, {
            method: "POST",
            headers: {
                "Content-type": "application/json"
            },
            body: JSON.stringify(data)
        })
        .then(() => loading(event));
        
    }
}

function loading(event) {
    if (event){
        event.preventDefault();
    }

    
    tableBody.innerHTML = "";
    try {
        fetch(url)
        .then(response => response.json())
        .then((data) => {
            Object.values(data)
            .forEach(({ product, count , price, _id }) => {
        
                let tr = document.createElement("tr");

                let tdProduct = document.createElement("td");
                tdProduct.textContent = product;
                tdProduct.setAttribute("class", "name");

                   let tdCountProduct = document.createElement("td");
                tdCountProduct.textContent = count;
                tdCountProduct.setAttribute("class", "count-product");


                let tdProductPrice = document.createElement("td");
                tdProductPrice.textContent = price;
                tdProductPrice.setAttribute("class", "product-price");


                let tdBtns = document.createElement("td");
                tdBtns.setAttribute("class", "btn");

                let updateBtn = document.createElement("button");
                updateBtn.setAttribute("class", "update");
                updateBtn.setAttribute("id", _id);

                updateBtn.textContent = 'Update';

                let deleteBtn = document.createElement("button");
                deleteBtn.setAttribute("class", "delete");
                deleteBtn.setAttribute("id", _id);

                deleteBtn.textContent = 'Delete';

                tdBtns.appendChild(updateBtn);
                tdBtns.appendChild(deleteBtn);
                tr.appendChild(tdProduct);
                tr.appendChild(tdCountProduct);
                tr.appendChild(tdProductPrice);
                tr.appendChild(tdBtns);
                tableBody.appendChild(tr);

                updateBtn.addEventListener("click", updateRow);
                deleteBtn.addEventListener("click", deleteRow);

            })
       
        })
    }
    catch (error) {
        console.error(`Could not get products: ${error}`);
    }
}

function updateRow(e){
    let target = e.target
    let id = target.id;

    let product  = target.parentElement.parentElement.children[0].textContent;
    let count  = target.parentElement.parentElement.children[1].textContent;
    let price  = target.parentElement.parentElement.children[2].textContent;

    productName.value = product;
    productCount.value = count;
    priceProduct.value = price;

    updateProduct.disabled = false;
    addProduct.disabled = true;

    updateProduct.addEventListener("click", function(e) {
        e.preventDefault();
        let product = productName.value
        let count = productCount.value
        let price = priceProduct.value

        if (product, count, price) {

            productName.value = "";
            productCount.value = "";
            priceProduct.value = "";
    
            let updateUrl = `${url}${id}`
    
            data = {
                "product" : product,
                "count" : count,
                "price" : price
            }
    
            fetch(updateUrl, {
                method: "PATCH",
                headers: {
                    "Content-type": "application/json"
                },
                body: JSON.stringify(data)
            })
            .then(() => loading())
            
            updateProduct.disabled = true
            addProduct.disabled = false

        }
    })       

}

async function deleteRow(e){
    let id = e.target.id;

    let urlDelete = `${url}${id}`;
    
    await fetch(urlDelete,{
        method: "DELETE",
        }
        
    )
    loading()

}

attachEvents();