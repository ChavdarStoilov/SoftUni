function app(input) {
    let products = input[0].split("!")
    let end = false

    for (let i = 1; i < input.length; i++) {
        let command = input[i].split(" ")

        if (command.join(" ") === "Go Shopping!"){
            end = true
            break
        }
        
        else if (command[0] === "Urgent"){
            if (products.indexOf(command[1]) === -1){
                products.unshift(command[1])
            }
        }
        else if (command[0] === "Unnecessary") {
            if (products.indexOf(command[1]) !== -1){
                products.splice(products.indexOf(command[1]), 1)
            }
        }
        else if (command[0] === "Correct") {
            if (products.indexOf(command[1]) !== -1){
                products[products.indexOf(command[1])] = command[2]
            }
        }
        else if (command[0]=== "Rearrange") {
            if (products.indexOf(command[1]) !== -1){
                item = products.splice(products.indexOf(command[1]), 1)
                products.push(item)
            }
            ;
        }
    }

    
    if (end) {
        console.log(products.join(", "));
    }
}

app(["Tomatoes!Potatoes!Bread",
"Unnecessary Milk",
"Urgent Tomatoes",
"Go Shopping!"])

