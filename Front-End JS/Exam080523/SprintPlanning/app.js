window.addEventListener('load', solve);

function solve() {
    let taskNumber = 1
    let totalPoint = 0
    const data = {
        title: "",
        description: "",
        label: "",
        points: 0,
        assignee: ""
    }

    let title = document.getElementById("title")
    let description = document.getElementById("description")
    let label = document.getElementById("label")
    let points = document.getElementById("points")
    let assignee = document.getElementById("assignee")


    

    const createBtn = document.getElementById("create-task-btn")
    

    createBtn.addEventListener('click', createTask)
    
    function createTask(event) {
        event.preventDefault();
        data["title"] = document.getElementById("title").value
        data["description"] = document.getElementById("description").value
        data["label"] = document.getElementById("label").value
        data["points"] = document.getElementById("points").value
        data["assignee"] = document.getElementById("assignee").value

        const cretesection = document.getElementById("tasks-section")
        let totalPoints = document.getElementById("total-sprint-points")
        if (title.value && description.value && label.value && points.value > 0 && assignee.value) {
            
            typeOfLable = ""
            lebelicone = ""
            console.log(label.value);
            if (label.value == "Feature") {
                typeOfLable = "feature"
                lebelicone = "&#8865"
            }
            else if (label.value == "Low Priority Bug") {
                typeOfLable = "low-priority"
                lebelicone = "&#9737"
            }
            else if (label.value == "High Priority Bug") {
                typeOfLable = "high-priority"
                lebelicone = "&#9888"
            }

            let newArticle = document.createElement("article")
            newArticle.setAttribute("class", "task-card")
            newArticle.setAttribute("id", `task-${taskNumber}`)
            newArticle.innerHTML = `
                <div class="task-card-label ${typeOfLable}">${label.value} ${lebelicone}</div> 
                <h3 class="task-card-title">${title.value}</h3>            
                <p class="task-card-description">${description.value}</p>
                <div class="task-card-points">${points.value}</div>
                <div class="task-card-assignee"${assignee.value}</div>
                <div class="task-card-actions"><button id="task-delete-btn">Delete</button></div>
            `

            cretesection.appendChild(newArticle)
            taskNumber ++

            deleteTask = document.getElementById("task-delete-btn")

            deleteTask.addEventListener("click", function(event) {
                forDelete = event.target.parentElement.offsetParent
                
                const deleteBtn = document.getElementById("delete-task-btn")
                deleteBtn.addEventListener("click", function() {
                    cretesection.removeChild(forDelete)
                    totalPoints.textContent = `Total Points ${totalPoint}pts`
                    deleteBtn.disabled = true;
                    
                    title.value= ""
                    description.value = ""
                    label.value = ""
                    points.value = ""
                    assignee.value = ""
                })

                title.value= data["title"]
                description.value = data["description"]
                label.value = data["label"]
                points.value = data["points"]
                assignee.value = data["assignee"]
                totalPoint -= Number(data["points"])
                deleteBtn.disabled = false;
                createBtn.disabled = true;
                title.disabled = true;
                description.disabled = true;
                label.disabled = true;
                points.disabled = true;
                assignee.disabled = true;
                
            })
            
            totalPoint += Number(points.value)
            totalPoints.textContent = `Total Points ${totalPoint}pts`
        }
        
        title.value= ""
        description.value = ""
        label.value = ""
        points.value = ""
        assignee.value = ""

        
    }
}