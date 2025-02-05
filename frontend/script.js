function getWeather() {
    let city = document.getElementById("city").value;
    
    if (city === "") {
        alert("Please enter a city name.");
        return;
    }

    fetch(`http://127.0.0.1:8000/weather?city=${city}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById("result").innerHTML = `<p style="color:red">${data.error}</p>`;
            } else {
                document.getElementById("result").innerHTML = `
                    <h3>${data.city}</h3>
                    <p>Temperature: ${data.temperature}°C</p>
                    <p>Humidity: ${data.humidity}%</p>
                    <p>Condition: ${data.weather}</p>
                `;
            }
        })
        .catch(error => console.error("Error fetching data:", error));
}
