function employee(params) {
    let list = {

    }

    for (row in params) {
        let name = params[row]
        let personNumber = name.length

        if (!(name in list)) {
            list[name] = personNumber
        }
    }

    for (person in list) {
        console.log(`Name: ${person} -- Personal Number: ${list[person]}`);
    }

}


employee([
    'Silas Butler',
    'Adnaan Buckley',
    'Juan Peterson',
    'Brendan Villarreal'  
    ])