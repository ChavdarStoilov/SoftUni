// // function sprint(inputData) {
// //     const data = {};
// //     counter = Number(inputData.shift());

// //     for (let index = 0; index < counter; index++) {
// //         let [assignee, taskId, title, status, points] = inputData.shift().split(':')
// //         if (!data[assignee]) {
// //             data[assignee] = [];
// //         }
// //         data[assignee].push({
// //             taskId, title, status, points: Number(points),
// //         });
// //     }

// //     let actions = inputData.length;
// //     for (let i = 0; i < actions; i++) {
// //         let line = inputData.shift().split(":");
// //         let action = line[0];
// //         let assignee = line[1];
// //         if (!data[assignee]) {
// //             console.log(`Assignee ${assignee} does not exist on the board!`);
// //             continue;
// //         }

// //         if (action === "Add New") {
// //             data[assignee].push({
// //                 taskId: line[2],
// //                 title: line[3],
// //                 status: line[4],
// //                 points: Number(line[5]),
// //             })

// //         } else if (action === 'Change Status') {
// //             const index = data[assignee].findIndex(task => task.taskId === line[2]);
// //             if (index === -1) {
// //                 console.log(`Task with ID ${line[2]} does not exist for ${assignee}!`);
// //                 continue;
// //             }
// //             data[assignee][index].status = line[3];

// //         } else if (action === 'Remove Task') {
// //             const index = Number(line[2]);
// //             if (index < 0 || index >= data[assignee].length) {
// //                 console.log('Index is out of range!');
// //                 continue;
// //             }
// //             data[assignee].splice(index, 1);
// //         }
// //     }

// //     let totalToDoCounter = 0;
// //     let totalInProgressCounter = 0;
// //     let totalCodeReviewCounter = 0;
// //     let totalDoneCounter = 0;
// //     for (const assignee of Object.values(data)) {
// //         for (const task of assignee) {
// //             if (task.status === 'ToDo') {
// //                 totalToDoCounter += task.points
// //             } else if (task.status === 'In Progress') {
// //                 totalInProgressCounter += task.points
// //             } else if (task.status === 'Code Review') {
// //                 totalCodeReviewCounter += task.points
// //             } else if (task.status === 'Done') {
// //                 totalDoneCounter += task.points
// //             }
// //         }
// //     }

// //     console.log(
// //         `ToDo: ${totalToDoCounter}pts\nIn Progress: ${totalInProgressCounter}pts\nCode Review: ${totalCodeReviewCounter}pts\nDone Points: ${totalDoneCounter}pts`
// //     );
// //     if (totalDoneCounter >= totalToDoCounter + totalInProgressCounter + totalCodeReviewCounter) {
// //         console.log('Sprint was successful!');
// //     } else {
// //         console.log('Sprint was unsuccessful...');
// //     }
// // }

// sprint(
//     [
//         '4',
//         'Kiril:BOP-1213:Fix Typo:Done:1',
//         'Peter:BOP-1214:New Products Page:In Progress:2',
//         'Mariya:BOP-1215:Setup Routing:ToDo:8',
//         'Georgi:BOP-1216:Add Business Card:Code Review:3',
//         'Add New:Sam:BOP-1237:Testing Home Page:Done:3',
//         'Change Status:Georgi:BOP-1216:Done',
//         'Change Status:Will:BOP-1212:In Progress',
//         'Remove Task:Georgi:3',
//         'Change Status:Mariya:BOP-1215:Done'
//     ]
// )



for (let i = 10; i > 3; i -=2) {
    console.log(i);
}