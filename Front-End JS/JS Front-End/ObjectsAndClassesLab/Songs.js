function song(arry) {
    let n = arry[0]
    let theType = arry[arry.length - 1]

    let allSongs = []

    class Songs {
        constructor(typeList, name, time){
            this.typeList = typeList
            this.name = name
            this.time = time
        }
    }

    for (let i = 1; i <= n; i++) {
       let [type, name, time]= arry[i].split("_")
       let songs = new Songs(type, name, time)
       allSongs.push(songs)

    }
    

    for (i in allSongs) {
        if (allSongs[i].typeList === theType){
            console.log(allSongs[i].name);
        }
        else if(theType === "all") {
            console.log(allSongs[i].name)
        };
    }
}



song([2,

    'like_Replay_3:15',
    
    'ban_Photoshop_3:48',
    
    'all']  )