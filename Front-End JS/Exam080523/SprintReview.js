function sprint(input) {
    const counter = input.shift()

    let data = {

    };

    for (let i = 0; i < counter; i++) {
        
        row = input.shift().split(":")
        
        if (!(row[0] in data)){
            data[row[0]] = [{
                "taskId": row[1],
                "title": row[2],
                "status": row[3],
                "estimatedPoints": row[4]
            }];
        }
        else {
            data[row[0]].push({
                "taskId": row[1],
                "title": row[2],
                "status": row[3],
                "estimatedPoints": row[4]
            });
        }
    };

    for (i in input) {
        action = input[i].split(":")

        
        if (action[0] === "Add New"){
            if (!(action[1] in data)){
                console.log(`Assignee ${action[1]} does not exist on the board!`);
                ;
            }
            else {
                data[action[1]].push( {
                    "taskId": action[2],
                    "title": action[3],
                    "status": action[4],
                    "estimatedPoints": action[5]
                })
            }
        }
        else if (action[0] === "Change Status") {
            if (!(action[1] in data)){
                console.log(`Assignee ${action[1]} does not exist on the board!`);
            }
            else {
                for (i in data[action[1]]) {
                    if (data[action[1]][i]["taskID"] === action[2]) {
                        data[action[1]["taskId"]] = action[2]
                        break
                    }
                    
                    console.log(`Task with ID ${action[2]} does not exist for ${action[1]}!`);
                }
                
            }
        
        }
        else if (action[0] === "Remove Task"){
            if (!(action[1] in data)){
                console.log(`Assignee ${action[1]} does not exist on the board!`);
            }
            else if (Number(action[2]) > data[action[1]].length) {
                console.log('Index is out of range!');
            }
            else {
                data[action[1]].splice(action[2], 1);
            }
        }
    }


    
    totalPoints = {
        "ToDo": 0,
        "In Progress": 0,
        "Code Review": 0,
        "Done": 0
    }

    for (i in data) {

        for (row in data[i])
            console.log(i, row, data[i][row] ,data[i][row]["status"]);
            type = data[i][row]["status"]
            
            if (type === "ToDo") {
                totalPoints["ToDo"] += Number(data[i][row]["estimatedPoints"])
            }
            else if (type === "In Progress") {
                totalPoints["In Progress"] += Number(data[i][row]["estimatedPoints"])
            }
            else if (type === "Code Review") {
                totalPoints["Code Review"] += Number(data[i][row]["estimatedPoints"])
            }
            else if (type === "Done") {
                totalPoints["Done"] += Number(data[i][row]["estimatedPoints"])
            }
    }

    console.log(
        `ToDo: ${totalPoints["ToDo"]}pts\nIn Progress: ${totalPoints["In Progress"]}pts\nCode Review: ${totalPoints["Code Review"]}pts\nDone Points: ${totalPoints["Done"]}pts`
    );

}


sprint(
    [
        '5',
        'Kiril:BOP-1209:Fix Minor Bug:ToDo:3',
        'Mariya:BOP-1210:Fix Major Bug:In Progress:3',
        'Peter:BOP-1211:POC:Code Review:5',
        'Georgi:BOP-1212:Investigation Task:Done:2',
        'Mariya:BOP-1213:New Account Page:In Progress:13',
        'Add New:Kiril:BOP-1217:Add Info Page:In Progress:5',
        'Change Status:Peter:BOP-1290:ToDo',
        'Remove Task:Mariya:1',
        'Remove Task:Joro:1',
    ]
)