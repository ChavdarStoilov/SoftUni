function lockedProfile() {
  window.onclick = (e) => {
    let btn = e.target;

    // console.log(btn.checked);
    if (btn.localName === "button") {
      let divId = btn.previousElementSibling.id;
      let inputId = divId.slice(0, 5);
      let radioButtonName = `${inputId}Locked`;
      let radioButton = document.getElementsByName(radioButtonName)[1];

      if (radioButton.checked && btn.textContent == "Show more") {
        document.getElementById(divId).style.display = "block";
        btn.textContent = "Hide it";

        document.getElementsByTagName(`${inputId}Username`).disabled = false;
        document.getElementsByTagName(`${inputId}Email`).disabled = false;
        document.getElementsByTagName(`${inputId}Age`).disabled = false;
        document.getElementsByTagName(`${inputId}Username`).readOnly = false;
        document.getElementsByTagName(`${inputId}Email`).readOnly = false;
        document.getElementsByTagName(`${inputId}Age`).readOnly = false;
      } else if (btn.textContent == "Hide it" && radioButton.checked) {
        document.getElementById(divId).style.display = "none";
        btn.textContent = "Show more";
      }
    }
  };
}
