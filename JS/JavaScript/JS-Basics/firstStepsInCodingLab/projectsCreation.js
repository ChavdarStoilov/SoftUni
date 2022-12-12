function projects(data){
    let name = data[0]
    let neededTime = data[1] * 3
    let countProjects = data[1]

    console.log(`The architect ${name} will need ${neededTime} hours to complete ${countProjects} project/s.`);
}


projects(["George ", "4 "])