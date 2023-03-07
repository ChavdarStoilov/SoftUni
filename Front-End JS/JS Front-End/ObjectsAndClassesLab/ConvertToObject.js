function convertor(input) {
    let json = JSON.parse(input)

    for (key in json) {
        console.log(`${key}: ${json[key]}`);
    }
}

console.log(convertor('{"name": "George", "age": 40, "town": "Sofia"}'));