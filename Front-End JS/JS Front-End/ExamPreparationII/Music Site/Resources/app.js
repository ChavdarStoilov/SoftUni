window.addEventListener('load', solve);
 
function solve() {
    const form = document.querySelector('form');
    const genre = document.querySelector('#genre');
    const name = document.querySelector('#name');
    const author = document.querySelector('#author');
    const date = document.querySelector('#date');
    const likes = document.querySelector('#total-likes .likes p')
    const allHits = document.querySelector(".all-hits-container");

    var counter = 0;
 

    form.addEventListener('submit', function (event){
        
        if (genre.value && name.value && author.value && date.value){
                event.preventDefault();

                let newDiv = document.createElement("div");
                newDiv.setAttribute("class", "hits-info");

                let img = document.createElement("img");
                img.src = './static/img/img.png';

                let h2Genre = document.createElement("h2");
                h2Genre.textContent = `Genre: ${genre.value}`;

                let h2Name = document.createElement("h2");
                h2Name.textContent = `Name: ${name.value}`;

                let h2Autor = document.createElement("h2");
                h2Autor.textContent = `Author: ${author.value}`;

                let h3 = document.createElement("h3");
                h3.textContent = `Date: ${date.value}`;

                let btnSave = document.createElement("button");
                btnSave.setAttribute("class", "save-btn");
                btnSave.textContent = "Save song";

                let btnLike = document.createElement("button");
                btnLike.setAttribute("class", "like-btn");
                btnLike.textContent = "Like song";

                let btnDel = document.createElement("button");
                btnDel.setAttribute("class", "delete-btn");
                btnDel.textContent = "Delete";

            
                
                newDiv.appendChild(img);
                newDiv.appendChild(h2Genre);
                newDiv.appendChild(h2Name);
                newDiv.appendChild(h2Autor);
                newDiv.appendChild(h3);
                newDiv.appendChild(btnSave);
                newDiv.appendChild(btnLike);
                newDiv.appendChild(btnDel);
                
                allHits.appendChild(newDiv);

                genre.value = "";
                name.value = "";
                author.value = "";
                date.value = "";

                let saveBtn = document.getElementsByClassName("save-btn")[0];
                let likeBtn = document.getElementsByClassName("like-btn")[0];
                let delBtn =  document.getElementsByClassName("delete-btn")[0];
                
                
                btnLike.addEventListener('click', function(event){
                    event.preventDefault();
                    counter ++

                    likes.textContent = `Total Likes: ${counter}`;
                    likeBtn.disabled = true;
                }
                )
                saveBtn.addEventListener('click', function(event){
                    event.preventDefault();

                    let savedSongs = document.getElementsByClassName("saved-container")[0];
                
                    newDiv.removeChild(saveBtn);
                    newDiv.removeChild(likeBtn);
                    allHits.removeChild(newDiv);
                    savedSongs.appendChild(newDiv);

                })

                delBtn.addEventListener('click', function(event){
                    event.preventDefault();

        

                    delBtn.parentElement.remove();
                
                })
            }
            else {

                event.preventDefault();
            }
     

    
        }

    )
}





