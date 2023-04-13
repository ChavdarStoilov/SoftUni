window.addEventListener('load', solve);

function solve() {
   let firstName = document.getElementById("first-name")
   let lastName = document.getElementById("last-name")
   let numberOfPeople = document.getElementById("people-count")
   let fromDate = document.getElementById("from-date")
   let days = document.getElementById("days-count")
   let nextBtn = document.getElementById("next-btn")

   nextBtn.addEventListener("click", nextStep)
   

   function nextStep(event) {
        event.preventDefault();
   }
}


    
    
