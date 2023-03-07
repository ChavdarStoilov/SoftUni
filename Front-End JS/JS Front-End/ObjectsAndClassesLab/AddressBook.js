function addressBook(arry) {

    let book = {

    }
    
    for (row in arry) {
        let [name, address] = arry[row].split(":")
        
        if(!(name in book)) {
            book[name]
        }
        book[name] = address
    }

    
    const sortedBooks = Object.keys(book)
    .sort()
    .reduce((address, key) => {
        address[key] = book[key];

        return address;
    }, {})

    
    for (names in sortedBooks) {
        console.log(`${names} -> ${sortedBooks[names]}`);
    }
}

addressBook(['Tim:Doe Crossing',
'Bill:Nelson Place',
'Peter:Carlyle Ave',
'Bill:Ornery Rd'])