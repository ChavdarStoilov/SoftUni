function attachEvents() {
    const author = document.querySelector('input[name="author"]')
    const content = document.querySelector('input[name="content"]')
    const send = document.getElementById("submit")
    const refresh = document.getElementById("refresh")
    const messages = document.getElementById("messages")

    const urlChat = "http://localhost:3030/jsonstore/messenger"

    send.addEventListener("click", sendMessege)
    refresh.addEventListener("click", refreshChat)

    function sendMessege() {
    
        data = {
            "author": author.value,
            "content": content.value
        }

        fetch(urlChat, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(data)
        })

        author.value = ""
        content.value = ""
    }
    
    function refreshChat() {
        messages.value = ""
        output = []
        fetch(urlChat)
        .then(response => response.json())
        .then((data)=> {
            
            for (row in data) {
                let author = data[row]["author"]
                let message = data[row]["content"]
                output.push(`${author}: ${message}`)
            }
            messages.value = output.join("\n")

        })

        
    }
    

}

attachEvents();

'Spami: Hello, are you there?\nGarry: Yep, whats up :?\nGeorge: Hello, guys! :))\n' 
'Spami: Hello, are you there?\nGarry: Yep, whats up :?\nGeorge: Hello, guys! :))'