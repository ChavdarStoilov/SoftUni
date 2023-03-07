function heroes(input) {
    let inventory = []

    for (let i in input){
        let [heroName, heroLevel, item] = input[i].split(" / ")

        inventory.push({
            Hero: heroName,
            level: Number(heroLevel),
            items: item 
        })

    }

    inventory.sort((a,b) => a.level - b.level);

    for (let i = 0; i < inventory.length; i ++) {
        let names = inventory[i]["Hero"]
        let levels = inventory[i]["level"]
        let item = inventory[i]["items"]

        console.log(`Hero: ${names}\nlevel => ${levels}\nitems => ${item}`);

    }
}



heroes([
    'Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara'
    ])