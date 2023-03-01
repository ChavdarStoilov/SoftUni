function attachEvents() {
    const urlPosts = "http://localhost:3030/jsonstore/blog/posts"
    const urlComments = "http://localhost:3030/jsonstore/blog/comments"

    const btnLoadPost = document.getElementById("btnLoadPosts")
    const btnViewPost = document.getElementById("btnViewPost")
    const listPosts = document.getElementById("posts")
    const title = document.getElementById("post-title")
    const postBody = document.getElementById("post-body")
    const postComment = document.getElementById("post-comments")

    btnLoadPost.addEventListener("click", loadingPosts)
    btnViewPost.addEventListener("click", viewPost)

    let getPosts ={

    }

    function loadingPosts() {
        fetch(urlPosts)
        .then(response => response.json())
        .then((data) => {
            for (row in data){
                let title = data[row]["title"]
                let value = data[row]["id"]
                let body = data[row]["body"]
    
                if (!(value in getPosts)) {
                    getPosts[value] = body
                }

                
                let option = document.createElement("option")
                option.setAttribute("value", value)
                option.textContent = title

                listPosts.appendChild(option)

            }
        })
    }

    function viewPost(){
        
        if (listPosts.selectedOptions.length != 0) {
            let selectedPost = listPosts.selectedOptions[0]
            fetch(urlComments)
            .then(response => response.json())
            .then((data) => {
                for (rows in data) {
                    let postId = data[rows]["postId"]
                    let text = data[rows]["text"]
                    let commendId = data[rows]["id"]
    
                    if (selectedPost.value === postId) {
                        title.textContent = selectedPost.textContent
                        postBody.textContent = getPosts[postId]
                        
                        let newLi = document.createElement("li")
                        newLi.setAttribute("id", commendId)
                        newLi.textContent = text

                        postComment.appendChild(newLi)
                    }
                }
           })
        }
       
    }

}

attachEvents();

// console.log(`${title}\n${value}\n${body}`);
