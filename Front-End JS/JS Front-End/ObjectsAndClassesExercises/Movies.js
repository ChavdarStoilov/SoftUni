function movies(params) {
    let allMovie = []

    for (i in params){
        let row = params[i].split(" ")
        let indexDirecotr = row.indexOf("directedBy")
        let indexOnDate = row.indexOf("onDate")

        if (row[0] === "addMovie"){
            let movie = row.slice(1).join(" ")
            if (!(movie in allMovie)) {
                allMovie.push({
                    "name": movie
                })
            };
        }
        else {
            for (let movies in allMovie){
                let rows = allMovie[movies]
                if (row[indexDirecotr] === "directedBy"){
                    let movie = row.slice(0, indexDirecotr).join(" ")

                    if (rows["name"] === movie){
                        let director = row.slice(indexDirecotr + 1).join(" ");
                        rows["director"] = director
                    }
                }
                else if(row[indexOnDate] === "onDate") {
                    let movie = row.slice(0, indexOnDate).join(" ")
                    let data = row.slice(indexOnDate + 1, row.length).join(" ");
                    if (rows["name"] === movie){
                        rows["date"] = data
                    }
                }
            }
        }
        
    }
    
    for (row in allMovie) {
        let movie = allMovie[row]

        if (movie["director"] && movie["date"] && movie["name"]){
            console.log(JSON.stringify(movie));
        }

    }
}



movies([
    'addMovie Fast and Furious',
    'addMovie Godfather',
    'Inception directedBy Christopher Nolan',
    'Godfather directedBy Francis Ford Coppola',
    'Godfather onDate 29.07.2018',
    'Fast and Furious onDate 30.07.2018',
    'Batman onDate 01.08.2018',
    'Fast and Furious directedBy Rob Cohen'
    ])