function attachEvents() {
  const getWeather = document.getElementById("submit");
  const weathers = document.getElementById("forecast");
  const current = document.getElementById("current");
  const upcoming = document.getElementById("upcoming");

  getWeather.addEventListener("click", getingWeaher);

  function getingWeaher() {
    let location = document.getElementById("location").value;
    
    // weathers.innerHTML = `
    // <div id="current">
    //     <div class="label">Current conditions</div>
    // </div>
    // <div id="upcoming">
    //     <div class="label">Three-day forecast</div>
    // </div>
    // `

    let url = "http://localhost:3030/jsonstore/forecaster/locations";
    
    try {
      fetch(url)
        .then((response) => response.json())
        .then((data) => {
          for (i in data) {
            if (location === data[i]["name"]) {
              let locationCode = data[i]["code"];
              today(locationCode);
              threeDays(locationCode);
              weathers.style.display = "block";
            }
          }

        })
        .catch(() =>{
            weathers.innerHTML = "<h1>Error</h1>";
            weathers.style.textAlign = "center";
            weathers.style.display = "block";
        })
    } catch {
      console.log("error");
    }
  }

  function today(code) {
    
    let url = `http://localhost:3030/jsonstore/forecaster/today/${code}`;
    fetch(url)
      .then((response) => response.json())
      .then((data) => {

        let symbols = {
            "Sunny": `☀`,
            "Partly sunny": `⛅`,
            "Overcast": `☁`,
            "Rain":	`☂`,
            "Degrees": `°`

        }

        let newDiv = document.createElement("div")
        newDiv.setAttribute("class", "forecasts")

        let spanSymbol = document.createElement("span")
        spanSymbol.setAttribute("class", "condition symbol")

        let spanCondition = document.createElement("span")
        spanCondition.setAttribute("class", "condition")

        let spanLocation = document.createElement("span")
        let spanInfo = document.createElement("span")
        let spanWeather = document.createElement("span")
        spanLocation.setAttribute("class", "forecast-data")
        spanInfo.setAttribute("class", "forecast-data")
        spanWeather.setAttribute("class", "forecast-data")


        let location = data["name"]
        let forecastData = data["forecast"]

        let condition = forecastData["condition"]
        let high = forecastData["high"]
        let low = forecastData["low"]

        spanSymbol.textContent = symbols[condition]
        spanLocation.textContent = location
        let degree = symbols['Degrees']
        spanInfo.textContent = `${low}${degree}/${high}${degree}`
        spanWeather.textContent = condition

        spanCondition.appendChild(spanLocation)
        spanCondition.appendChild(spanInfo)
        spanCondition.appendChild(spanWeather)
        spanCondition.appendChild(spanWeather)

        newDiv.appendChild(spanSymbol)
        newDiv.appendChild(spanCondition)
        current.appendChild(newDiv)

      })
      .catch(() => {
        console.log("Error");
      });
  }

  function threeDays(code) {
    let url = `http://localhost:3030/jsonstore/forecaster/upcoming/${code}`;
    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        let newDiv = document.createElement("div")
        newDiv.setAttribute("class", "forecast-info")

        let symbols = {
            "Sunny": `☀`,
            "Partly sunny": `⛅`,
            "Overcast": `☁`,
            "Rain":	`☂`,
            "Degrees": `°`

        }

        let forecast = data["forecast"]
        
        for (row in forecast) {

            let condition = forecast[row]["condition"]
            let high = forecast[row]["high"]
            let low  = forecast[row]["low"]

            let spanUpcoming = document.createElement("div")
            spanUpcoming.setAttribute("class", "upcoming")
    
            let spanSymbol = document.createElement("span")
            spanSymbol.setAttribute("class", "symbol")
            spanSymbol.textContent = symbols[condition]
    
            let spanforecastInfo = document.createElement("span")
            spanforecastInfo.setAttribute("class", "forecast-data")
            let degree = symbols['Degrees']
            spanforecastInfo.textContent = `${low}${degree}/${high}${degree}`
    
            let spanForeWeather = document.createElement("span")
            spanForeWeather.setAttribute("class", "forecast-data")
            spanForeWeather.textContent = condition


            spanUpcoming.appendChild(spanSymbol)
            spanUpcoming.appendChild(spanforecastInfo)
            spanUpcoming.appendChild(spanForeWeather)

            newDiv.appendChild(spanUpcoming)
            

        }

        upcoming.append(newDiv)

      })

  }
}

attachEvents();
