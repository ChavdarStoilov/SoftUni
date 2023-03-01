function attachEvents() {
  const urlStudents = "http://localhost:3030/jsonstore/collections/students";
  const firstName = document.querySelector("input[name='firstName']");
  const lastName = document.querySelector("input[name='lastName']");
  const facNumber = document.querySelector("input[name='facultyNumber']");
  const grade = document.querySelector("input[name='grade']");
  const table = document.getElementById("results").tBodies[0];

  const submitBtn = document.getElementById("submit");

  submitBtn.addEventListener("click", submiting);

  function presentData() {
    fetch(urlStudents)
      .then((response) => response.json())
      .then((data) => {
        for (dataRow in data) {
          let studentFirstName = data[dataRow]["firstName"];
          let studentLastName = data[dataRow]["lastName"];
          let studentFacNumber = data[dataRow]["facultyNumber"];
          let studentGrade = data[dataRow]["grade"];

          let row = document.createElement("tr");

          let tdFirstname = document.createElement("td");
          tdFirstname.textContent = studentFirstName;

          let tdLastName = document.createElement("td");
          tdLastName.textContent = studentLastName;

          let tdFacNumber = document.createElement("td");
          tdFacNumber.textContent = studentFacNumber;

          let tdGrade = document.createElement("td");
          tdGrade.textContent = studentGrade;

          row.appendChild(tdFirstname);
          row.appendChild(tdLastName);
          row.appendChild(tdFacNumber);
          row.appendChild(tdGrade);

          table.appendChild(row);
        }
      });
  }

  function submiting() {
    if (firstName.value && lastName.value && facNumber.value && grade.value) {
      let theName = firstName.value;
      let secondName = lastName.value;
      let number = facNumber.value;
      let theGrade = grade.value;

      
      firstName.value = "";
      lastName.value = "";
      facNumber.value = "";
      grade.value = "";

      data = {
        firstName: theName,
        lastName: secondName,
        facultyNumber: number,
        grade: theGrade,
      };

      fetch(urlStudents, {
        method: "post",
        headers: {
          "Content-type": "applicaiton/json",
        },
        body: JSON.stringify(data),
      });
    // presentData();

      
    }

  }
  // presentData();
}

attachEvents();
