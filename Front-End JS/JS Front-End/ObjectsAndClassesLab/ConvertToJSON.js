function convector(firstName, lastName, hairColor) {

    let json = {
        "name": firstName,
        "lastName": lastName,
        "hairColor": hairColor
    }
    
    return JSON.stringify(json)
}

console.log(convector('George', 'Jones',
'Brown'));