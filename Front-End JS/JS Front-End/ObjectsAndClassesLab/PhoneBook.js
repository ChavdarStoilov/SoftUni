function phoneBook(arry) {
    let book = {
        
    }

    for (i in arry) {
        let [name, phone] = arry[i].split(" ")

        if (!(name in book)) {
            book[name]
        }
        book[name] = phone
    }

    for (key in book) {
        console.log(`${key} -> ${book[key]}`);
    }
    
}

phoneBook(['George 0552554',
'Peter 087587',
'George 0453112',
'Bill 0845344'])