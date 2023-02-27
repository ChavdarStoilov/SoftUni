window.addEventListener("load", solve);

function solve() {

  let firstNameElement = document.getElementById("first-name");
  let lastNameElement = document.getElementById("last-name");
  let ageElement = document.getElementById("age");
  let storyTitleElement = document.getElementById("story-title");
  let genreElement = document.getElementById("genre");
  let storyElement = document.getElementById("story");
  let btnPublish = document.querySelector("#form-btn");

  btnPublish.addEventListener('click', function (event) {


    if (firstNameElement.value && lastNameElement.value && ageElement.value && storyTitleElement.value && storyElement.value) {
      event.preventDefault();
      const preview = document.querySelector("#preview-list");
      
      let li = document.createElement("li");
      li.setAttribute("class", "story-info");

      let article = document.createElement("article");

      let h4 = document.createElement("h4");
      h4.textContent = `Name: ${firstNameElement.value} ${lastNameElement.value}`;
      
      let pAge = document.createElement("p");
      pAge.textContent = `Age: ${ageElement.value}`;

      let pTitle = document.createElement("p");
      pTitle.textContent = `Title: ${storyTitleElement.value}`;

      let pGenre = document.createElement("p");
      pGenre.textContent = `Genre: ${genreElement.value}`;

      let pSotry = document.createElement("p");
      pSotry.textContent = storyElement.value;

      article.appendChild(h4);
      article.appendChild(pAge);
      article.appendChild(pTitle);
      article.appendChild(pGenre);
      article.appendChild(pSotry);

      li.appendChild(article);

      let btnSave = document.createElement("button");
      btnSave.setAttribute("class", "save-btn");
      btnSave.textContent = "Save Sotry";

      let btnEdit = document.createElement("button");
      btnEdit.setAttribute("class", "edit-btn");
      btnEdit.textContent = "Edit Sotry";
      
      let btnDelete = document.createElement("button");
      btnDelete.setAttribute("class", "delete-btn");
      btnDelete.textContent = "Delete Sotry";

      li.appendChild(btnSave);
      li.appendChild(btnEdit);
      li.appendChild(btnDelete);

      preview.appendChild(li);

      btnPublish.disabled = true;
      let editFirstName = firstNameElement.value
      let editLastName = lastNameElement.value
      let editAge = ageElement.value
      let editTitle = storyTitleElement.value
      let editStory = storyElement.value


      firstNameElement.value = "";
      lastNameElement.value = "";
      ageElement.value = "";
      storyTitleElement.value = "";
      storyElement.value = "";

      //My try:

      btnEdit.addEventListener('click', function (event) {
        event.preventDefault()
        firstNameElement.value = editFirstName
        lastNameElement.value = editLastName;
        ageElement.value = editAge;
        storyTitleElement.value = editTitle;
        genreElement.value = genreElement;
        storyElement.value = editStory;
        btnEdit.parentElement.remove();
        btnPublish.disabled = false;


      })

      btnSave.addEventListener('click', function (event) {
        event.preventDefault()
        let main = document.getElementById("main");
        main.innerHTML = "<h1>Your scary story is saved!</h1>";

      })

      btnDelete.addEventListener('click', function (event) {
        event.preventDefault()
        
        btnEdit.parentElement.remove();
        btnPublish.disabled = false;

      })

    }
  }
  );

}
