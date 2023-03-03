function lockedProfile() {
    const urlUsers = "http://localhost:3030/jsonstore/advanced/profiles"
    const username = document.querySelector("input[name='user1Username']") 
    const userEmail = document.querySelector("input[name='user1Email']")
    const userAge = document.querySelector("input[name='user1Age']")
    const radioBtn = document.querySelector("input[name='user1Locked']")
    const profiles = document.getElementsByClassName("profile")
    const showHideBtn = document.querySelector(".profile > button")


    showHideBtn.addEventListener("click", showHide)

    function showHide(){
        
        if (showHideBtn.textContent === "Show more"){
            console.log(showHideBtn);
        }
        else if (showHideBtn.textContent === "Hide it"){

        }
        let lockOrUnlock = radioBtn.value


    }


}
