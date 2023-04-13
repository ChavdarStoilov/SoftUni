window.addEventListener('load', solve);

function solve() {

    let currentData = {
        "firstName": null,
        "secondName": null,
        "dateIn": null,
        "dateOut": null,
        "people": null
    }

    const nextBtn = document.getElementById("next-btn")

    nextBtn.addEventListener("click", moveToRevserInfo)

    function moveToRevserInfo(event) {
        event.preventDefault();

        const firstNames = document.getElementById("first-name")
        const lastName =  document.getElementById("last-name")
        const dateIn = document.getElementById("date-in")
        const dateOut = document.getElementById("date-out")
        const people = document.getElementById("people-count")
        const infoTable = document.getElementsByClassName("info-list")[0]
        
        if (firstNames.value && lastName.value && dateIn.value && dateOut.value && people.value && Number(people.value) > 0) {
            currentData["firstName"] = firstNames.value
            currentData["secondName"] = lastName.value
            currentData["dateIn"] = dateIn.value
            currentData["dateOut"] = dateOut.value
            currentData["people"] = people.value

            content = `
                <li class="reservation-content">
                    <article>
                        <h3>Name: ${firstNames.value} ${lastName.value}</h3>
                        <p>From date: ${dateIn.value}</p>
                        <p>To date: ${dateOut.value}</p>
                        <p>For ${people.value} people</p>
                    </article>
                    <button class="edit-btn">Edit</button>
                    <button class="continue-btn">Continue</button>
            `

            infoTable.innerHTML = content

            firstNames.value = ""
            lastName.value = ""
            dateIn.value = ""
            dateOut.value = ""
            people.value = ""

            nextBtn.disabled = true

            const editingBnt = document.getElementsByClassName("edit-btn")[0]
            const continueBnt = document.getElementsByClassName("continue-btn")[0]

            editingBnt.addEventListener("click", editing)
            continueBnt.addEventListener("click", continueReserv)

        }

        function editing(event) {
            target = event.target
            owner = target.parentElement.parentElement
            owner.removeChild(target.parentElement)
            
            firstNames.value = currentData["firstName"]
            lastName.value = currentData["secondName"]
            dateIn.value = currentData["dateIn"]
            dateOut.value = currentData["dateOut"]
            people.value = currentData["people"]

            nextBtn.disabled = false
            
        }

        function continueReserv(event) {
            target = event.target
            owner = target.parentElement.parentElement
            owner.removeChild(target.parentElement)

            const conifmTable = document.getElementsByClassName("confirm-list")[0]

            content = `
                <li class="reservation-content">
                    <article>
                        <h3>Name: ${currentData["firstName"]} ${currentData["secondName"]}</h3>
                        <p>From date: ${currentData["dateIn"]}</p>
                        <p>To date: ${currentData["dateOut"]}</p>
                        <p>For ${currentData["people"]} people</p>
                    </article>
                    <button class="confirm-btn">Confirm</button>
                    <button class="cancel-btn">Cancel</button>
            `

            conifmTable.innerHTML = content

            const editingBnt = document.getElementsByClassName("confirm-btn")[0]
            const continueBnt = document.getElementsByClassName("cancel-btn")[0]

            editingBnt.addEventListener("click", confirmReserv)
            continueBnt.addEventListener("click", cancelReserv)
        }

        function confirmReserv(event) {
            target = event.target
            owner = target.parentElement.parentElement
            owner.removeChild(target.parentElement)

            end = document.getElementById("verification")

            end.setAttribute("class", "reservation-confirmed")
            end.textContent = "Confirmed."
            nextBtn.disabled = false
        }

        function cancelReserv(event) {
            target = event.target
            owner = target.parentElement.parentElement
            owner.removeChild(target.parentElement)

            end = document.getElementById("verification")

            end.setAttribute("class", "reservation-cancelled")
            end.textContent = "Cancelled."
            nextBtn.disabled = false
        }
    }

}





    
    



206677153 or 
201012527 or 
200005693 or 
203811234 or 
201259303 or 
204091394 or 
200005693 or 
202575927 or 
203811234 or 
203811234 or 
201259303 or 
200005693 or 
201259303 or 
202575927

