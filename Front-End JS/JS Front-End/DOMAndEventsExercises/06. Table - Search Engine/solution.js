function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);
   var selected = [];

   function onClick() {
      for (let i = 0; i < selected.length; i ++) {
         selected[i].removeAttribute("class")
      }
      let searchFor = document.getElementById("searchField")
      let tableRows = document.getElementsByClassName("container")[0].rows
   

      for (let r = 1; r < tableRows.length -1; r++ ){
         let tableCells = tableRows[r].cells
         for (let c = 0; c < tableCells.length; c ++){
            if (tableCells[c].innerText.match(searchFor.value) != null && searchFor.value) {
               selected.push(tableCells[c].parentElement)
               tableCells[c].parentElement.setAttribute("class", "select");

            }
         }
      }

      searchFor.value = ""
   }
};