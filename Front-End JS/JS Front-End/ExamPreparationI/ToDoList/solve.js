const list = "http://localhost:3030/jsonstore/tasks/";
const title = document.getElementById("title");
const btnAdd = document.getElementById("add-button");
const btnLoad = document.getElementById("load-button");
const toDoList = document.getElementById("todo-list");

function attachEvents() {
    btnAdd.addEventListener("click", adding);
    btnLoad.addEventListener("click", loading);
}

function loading(e) {
    if (e) {
        e.preventDefault();
    }
    
    toDoList.innerHTML = "";
    fetch(list)
      .then((res) => res.json())
      .then((list) => {
        Object.values(list)
          .forEach(({ name, _id }) => {
       
            let li = document.createElement("li");
            li.setAttribute("id", _id);
            let span = document.createElement("span");
            span.textContent = name;
    
            let removeBtn = document.createElement("button");
            removeBtn.textContent = "Remove";
            removeBtn.addEventListener("click", deleting)
            let editBtn = document.createElement("button");
            editBtn.textContent = "Edit";
            editBtn.addEventListener("click", editing)
    
            li.appendChild(span);
            li.appendChild(removeBtn);
            li.appendChild(editBtn);
    
            toDoList.appendChild(li);
          })
      })
}

function adding(event) {
    event.preventDefault();

    if (title.value) {
        let titles = title.value;
        title.value = ""

        data = {
            "name": titles,
        };

        fetch(list, {
            method: "POST",
            headers: {
                "Content-type": "application/json",
            },
            body: JSON.stringify(data),
        })
        .then(() => loading(event));
    }
}


async  function deleting(e){
    let target = e.target;
    let id = target.parentElement.id;

    let url = `${list}${id}`

    await fetch(url, {
        method: "DELETE",
    })
    loading()

} 

function editing(e) {
    const parentElement = e.target.parentElement;
    id = e.target.parentElement.id
    e.target.parentElement.innerHTML = `
    <input value='${
      e.target.parentElement.querySelector("span").textContent
    }'/>
      <button id="${id}" class="remove-button">Remove</button>
      <button id="${id}" class="submit-button">Submit</button>`;
    let remove = document.querySelector('.remove-button');
    remove.addEventListener('click', deleting);
    let submit = document.querySelector('.submit-button');
    submit.addEventListener('click', submiting);
  }
  

function submiting(e){
    target = e.target
    
    values = target.parentElement.children[0]

    data = {
        "name": values.value,
    };

    url = `${list}${target.parentElement.id}`;

    fetch(url, {
        method: "PATCH",
        body: JSON.stringify(data),
    })
    loading(e)

}

attachEvents();
