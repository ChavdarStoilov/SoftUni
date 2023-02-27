function pianist(input){
    let countPainist = input[0]
    let thePainist = {
        "piece": [],
        "composer": [],
        "key": []

    }

    for (let i = 1; i <= countPainist; i++){
        let items = input[i].split("|")
        thePainist["piece"].push(items[0])
        thePainist["composer"].push(items[1])
        thePainist["key"].push(items[2])
        
    }

    
    for (let i = 3; i < input.length; i++){
        let commands = input[i].split("|")

        if (commands[0] === "Stop") {
            let output = []
      
            for (let i= 0; i< thePainist["piece"].length; i++){
                
                let piece = thePainist["piece"][i]
                let composer = thePainist["composer"][i]
                let key = thePainist["key"][i]
                output.push(`${piece} -> Composer: ${composer}, Key: ${key}`)
            }

            return output.join("\n")
        }
        else if (commands[0] === "Add"){
            if (thePainist["piece"].indexOf(commands[1]) == -1){

                thePainist["piece"].push(commands[1])
                thePainist["composer"].push(commands[2])
                thePainist["key"].push(commands[3])
                console.log(`${commands[1]} by ${commands[2]} in ${commands[3]} added to the collection!`);
            }
            else {
                console.log(`${commands[1]} is already in the collection!`);
            }
        }
        else if (commands[0] === "Remove"){
            let index = thePainist["piece"].indexOf(commands[1])

            if (index === -1){
                console.log(`Invalid operation! ${commands[1]} does not exist in the collection.`);
            }
            else {
                thePainist["piece"].splice(index, 1)
                thePainist["composer"].splice(index, 1)
                thePainist["key"].splice(index, 1)
                console.log(`Successfully removed ${commands[1]}!`);
            }

        }
        else if (commands[0] === "ChangeKey") {
            let index = thePainist["piece"].indexOf(commands[1])

            if (index === -1){
                console.log(`Invalid operation! ${commands[1]} does not exist in the collection.`);
            }
            else {
                thePainist["key"].splice(index, 1, commands[2])
                console.log(`Changed the key of ${commands[1]} to ${commands[2]}!`);
            }
        }
    }
}



console.log(pianist([
  '4',
  'Eine kleine Nachtmusik|Mozart|G Major',
  'La Campanella|Liszt|G# Minor',
  'The Marriage of Figaro|Mozart|G Major',
  'Hungarian Dance No.5|Brahms|G Minor',
  'Add|Spring|Vivaldi|E Major',
  'Remove|The Marriage of Figaro',
  'Remove|Turkish March',
  'ChangeKey|Spring|C Major',
  'Add|Nocturne|Chopin|C# Minor',
  'Stop'
]

))