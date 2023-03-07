function towns(params) {
    
    let sities = {

    }


    for (row in params) {
        let [town, lati, long] = params[row].split(" | ")

        sities[town] = {
            "town": town,
            "latitude" : Number(lati).toFixed(2),
            "longitude": Number(long).toFixed(2)
        }

    }

    for (i in sities) {
        console.log(sities[i]);
    }

}

towns(['Sofia | 42.696552 | 23.32601',

'Beijing | 39.913818 | 116.363625'])