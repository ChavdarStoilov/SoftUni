function attachEvents() {
    const urlBook = "http://localhost:3030/jsonstore/phonebook";
    const phoneBookList = document.getElementById("phonebook");

    const person = document.getElementById("person");
    const phone = document.getElementById("phone");
    

    const loadBtn = document.getElementById("btnLoad");
    const createBtn = document.getElementById("btnCreate");

    loadBtn.addEventListener("click", loadPhones);
    createBtn.addEventListener("click", createNew);

    function loadPhones() {
        phoneBookList.innerHTML = ""

        fetch(urlBook)
        .then(response => response.json())
        .then((data) => {
            for (rows in data) {
                let person =  data[rows]["person"]
                let phone = data[rows]["phone"]
                let id = data[rows]["_id"]

                let newLi = document.createElement("li")
                newLi.setAttribute("class", "phonebook")
                newLi.textContent = `${person}: ${phone}`
                let deleteBtn = document.createElement("button")
                deleteBtn.setAttribute("id", id)
                deleteBtn.textContent = "Delete"

                newLi.appendChild(deleteBtn)
  
                phoneBookList.appendChild(newLi)
            };

            window.onclick = e => {
                let target = e.target
              
                if (target.textContent === "Delete" && target.tagName === "BUTTON") {
                    let id = target.id

                    let url = `http://localhost:3030/jsonstore/phonebook/${id}`

                    fetch(url, {
                        method: "DELETE",

                    })
                    // loadPhones()
                }
               
            }
        })

        
    };

    function createNew() {
        let personData = person.value
        let phoneData = phone.value

        person.value = ""
        phone.value = ""

        let data = {
            "person": personData,
            "phone": phoneData
          }
          
        fetch(urlBook, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(data)
        })

   
        // loadPhones()
    };


}

attachEvents();
