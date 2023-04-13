window.addEventListener('load', solve);

function solve() {
    const totalPointsElement = document.getElementById('total-sprint-points');
    const taskIdHiddenElement = document.getElementById('task-id');
    const titleElement = document.getElementById('title');
    const descriptionElement = document.getElementById('description');
    const labelElement = document.getElementById('label');
    const pointsElement = document.getElementById('points');
    const assigneeElement = document.getElementById('assignee');

    const taskBtn = document.getElementById('create-task-btn');
    const deleteBtn = document.getElementById('delete-task-btn'); //disabled
    taskBtn.addEventListener('click', taskHandler);

    const taskSectionElement = document.getElementById('tasks-section');

    let data = {};
    let idConter = 0;
    let pointsCounter = 0;
    let iconsMapper = {
        feature: '&#8865',
        low: '&#9737',
        high: '&#9888',
    }

    let additionClassMapper = {
        feature: "feature",
        low: "low-priority",
        high: "high-priority",
    }


    function taskHandler(e) {
        e.preventDefault();
        data = {
            title: titleElement.value,
            description: descriptionElement.value,
            label: labelElement.value,
            points: pointsElement.value,
            assignee: assigneeElement.value,
        }
        if (!data.title || !data.description || !data.label || !data.points || !data.assignee) {
            alert('wrong data');
            return
        }


        idConter++;
        let article = document.createElement('article');
        article.id = `task-${idConter}`;
        taskIdHiddenElement.value = article.id;
        article.classList.add('task-card');

        let iconToAdd = '';
        let classToAdd = '';
        if (data.label === 'Feature') {
            iconToAdd += iconsMapper['feature']
            classToAdd += additionClassMapper['feature']

        } else if (data.label === 'Low Priority Bug') {
            iconToAdd += iconsMapper['low']
            classToAdd += additionClassMapper['low']

        } else if (data.label === 'High Priority Bug') {
            iconToAdd += iconsMapper['high']
            classToAdd += additionClassMapper['high']
        }

        let label = cunstomHtml('div', 'task-card-label', data.label, article);
        label.innerHTML += " "+iconToAdd;
        label.classList.add(classToAdd)

        label.classList.add('feature')
        let title = cunstomHtml('h3', 'task-card-title', data.title, article);
        let description = cunstomHtml('p', 'task-card-description', data.description, article);
        let points = cunstomHtml('div', 'task-card-points', `Estimated at ${data.points} pts`, article);
        let assignee = cunstomHtml('div', 'task-card-assignee', `Assigned to: ${data.assignee}`, article);
        let divBtnContainer = cunstomHtml('div', 'task-card-actions', '', article)

        let delBtn = document.createElement('button');
        delBtn.textContent = 'Delete';
        delBtn.addEventListener('click', deleteHandler);
        divBtnContainer.appendChild(delBtn);
        taskSectionElement.appendChild(article)

        titleElement.value = '';
        descriptionElement.value = '';
        labelElement.value = '';
        pointsElement.value = '';
        assigneeElement.value = '';
        debugger
        pointsCounter += Number(data.points);
        totalPointsElement.textContent = `Total Points ${pointsCounter}pts`
    }

    function deleteHandler(e) {
        let task = e.target.parentNode.parentNode;
        let label = task.children[0].textContent;
        if (label.includes('Feature')) {
            labelElement.value = 'Feature'

        } else if (label.includes('Low')) {
            labelElement.value = "Low Priority Bug";
        } else if (label.includes('High')) {
            labelElement.value = "High Priority Bug";
        }

        let title = task.children[1].textContent;
        let description = task.children[2].textContent;
        let points = task.children[3].textContent.split(' ')[2];
        let assignee = task.children[4].textContent.split(': ')[1];

        titleElement.value = title;
        descriptionElement.value = description;
        pointsElement.value = points;
        assigneeElement.value = assignee;

        taskBtn.disabled = true;
        deleteBtn.disabled = false;

        labelElement.disabled = true;
        titleElement.disabled = true;
        descriptionElement.disabled = true;
        pointsElement.disabled = true;
        assigneeElement.disabled = true;

        deleteBtn.addEventListener('click', function deleteTask() {
            
            e.target.parentNode.parentNode.remove();
            taskBtn.disabled = false;
            deleteBtn.disabled = true;

            labelElement.disabled = false;
            titleElement.disabled = false;
            descriptionElement.disabled = false;
            pointsElement.disabled = false;
            assigneeElement.disabled = false;

            titleElement.value = '';
            descriptionElement.value = '';
            labelElement.value = '';
            pointsElement.value = '';
            assigneeElement.value = '';

            pointsCounter -= Number(points);
            totalPointsElement.textContent = `Total Points ${pointsCounter}pts`
        });

    }


    function cunstomHtml(type, className, text, parent) {
        let newElement = document.createElement(type);
        newElement.classList.add(className);
        newElement.textContent = text;
        if (parent) {
            parent.appendChild(newElement);
        }
        return newElement
    }







}