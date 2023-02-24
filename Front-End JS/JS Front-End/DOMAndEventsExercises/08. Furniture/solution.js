function solve() {

  let table = document.getElementsByClassName("table")[0].children[1];
 


  window.onclick = e => {
    id = e.target;  // to get the element
    let bought = {
      name: [],
      parent: []
    };
    let price = 0;
    let decoration = 0;
  

    if (id.tagName === "BUTTON" && id.textContent === "Generate"){
      let arryInput = document.getElementsByTagName("textarea")[0].value.replace("[", "").replace("]", "").split(/(?=, {)/g)

      for (let i = 0; i < arryInput.length; i++){
        let input = arryInput[i]
        if (i != 0){
          input = arryInput[i].replace(", ", "")
        }
    
        let jsonInput = JSON.parse(input)

        let newRow = document.createElement("tr");
        let cell1 = newRow.insertCell(0);
        let cell2 = newRow.insertCell(1);
        let cell3 = newRow.insertCell(2);
        let cell4 = newRow.insertCell(3);
        let cell5 = newRow.insertCell(4);
        cell1.innerHTML = `<img src="${jsonInput["img"]}">`;
        cell2.innerHTML = `<p>${jsonInput["name"]}</p>`;
        cell3.innerHTML = `<p>${jsonInput["price"]}</p>`;
        cell4.innerHTML = `<p>${jsonInput["decFactor"]}</p>`;
        cell5.innerHTML = `<input type="checkbox">`;
  
        table.appendChild(newRow);
      }


    }
    else if (id.tagName === "BUTTON" && id.textContent === "Buy"){
      document.getElementsByTagName("textarea")[1].value = ""

      for (let i = 0; i < table.rows.length; i++){
        let checkBox = table.rows[i].children[4].children[0];

        let childrenId = table.rows[i].children[4].children[0].parentElement.parentElement

        if (checkBox.checked) {
          col = table.rows[i].children[4].children[0].parentElement.parentElement.children

          bought["name"].push(col[1].textContent)
          bought["parent"].push(childrenId)
          price += Number(col[2].textContent)
          decoration += Number(col[3].textContent)

          }
          
          
        }

      for (let i = 0; i< bought["parent"].length; i++){
        parent = bought["parent"][i].parentNode;
        parent.removeChild(bought["parent"][i]);
      }

      let output = document.getElementsByTagName("textarea")[1]
      let avrg = (decoration / bought["name"].length).toFixed(2)
      output.value = `Bought furniture: ${bought["name"].join(", ")}\nTotal price: ${price.toFixed(2)}\nAverage decoration factor: ${avrg}`

    }

   
    document.getElementsByTagName("textarea")[0].value = ""
  
  }
}

//Bought furniture: Tablet, Vase\nTotal price: 2015.00\nAverage decoration factor: 7.60'
//'Bought furniture: Tablet, Vase\nTotal price: 2015.00\nAverage decoration factor: 7.6'
// function solve() {
//   const tBody = document.getElementsByTagName('tbody')[0];
//   const textInput = document.getElementsByTagName('textarea')[0];
//   const generateBtn = document.getElementsByTagName('button')[0];
//   const buyBtn = document.getElementsByTagName('button')[1];
//   const resultOutput = document.getElementsByTagName('textarea')[1];

//   generateBtn.addEventListener('click', function () {
//       let furnitureArray = JSON.parse(textInput.value);
//       for (furniture of furnitureArray) {
//           //Create tr
//           const newTr = document.createElement('tr');
//           //Create image td
//           const newImageTd = document.createElement('td');
//           const newImageImg = document.createElement('img');
//           newImageImg.src = furniture['img'];
//           newImageTd.appendChild(newImageImg);
//           newTr.appendChild(newImageTd);
//           //Create name td
//           const newNameTd = document.createElement('td');
//           const newNameP = document.createElement('p');
//           newNameP.innerHTML = furniture['name'];
//           newNameTd.appendChild(newNameP);
//           newTr.appendChild(newNameTd);
//           //Create price td
//           const newPriceTd = document.createElement('td');
//           const newPriceP = document.createElement('p');
//           newPriceP.innerHTML = furniture['price'];
//           newPriceTd.appendChild(newPriceP);
//           newTr.appendChild(newPriceTd);
//           //Create decoration td
//           const newDecorationTd = document.createElement('td');
//           const newDecorationP = document.createElement('p');
//           newDecorationP.innerHTML = furniture['decFactor'];
//           newDecorationTd.appendChild(newDecorationP);
//           newTr.appendChild(newDecorationTd);
//           //Create checkbox td
//           const newCheckboxTd = document.createElement('td');
//           const newCheckbox = document.createElement('input');
//           newCheckbox.type = 'checkbox';
//           newCheckboxTd.appendChild(newCheckbox);
//           newTr.appendChild(newCheckboxTd);
//           //Append tr to the table
//           tBody.appendChild(newTr);
//       }
//   });

//   buyBtn.addEventListener('click', function () {
//       const trs = document.querySelectorAll('tbody tr');
//       let totalFurniture = {
//           furniture: '',
//           totalPrice: 0,
//           totalDecFactor: 0,
//       };
//       let counter = 0;
//       for (i = 0; i < trs.length; ++i) {
//           if (
//               trs[i]
//                   .getElementsByTagName('td')[4]
//                   .getElementsByTagName('input')[0].checked
//           ) {
//               totalFurniture['furniture'] += `${
//                   trs[i]
//                       .getElementsByTagName('td')[1]
//                       .getElementsByTagName('p')[0].innerHTML
//               }, `;
//               totalFurniture['totalPrice'] += Number(
//                   trs[i]
//                       .getElementsByTagName('td')[2]
//                       .getElementsByTagName('p')[0].innerHTML
//               );
//               totalFurniture['totalDecFactor'] += Number(
//                   trs[i]
//                       .getElementsByTagName('td')[3]
//                       .getElementsByTagName('p')[0].innerHTML
//               );
//               counter++;
//           }
//       }
//       if (totalFurniture['furniture'] !== '') {
//           resultOutput.value = `Bought furniture: ${totalFurniture[
//               'furniture'
//           ].substring(
//               0,
//               totalFurniture['furniture'].length - 2
//           )}\nTotal price: ${totalFurniture['totalPrice'].toFixed(
//               2
//           )}\nAverage decoration factor: ${totalFurniture['totalDecFactor'] / counter}`;
//       }
//   });
// }