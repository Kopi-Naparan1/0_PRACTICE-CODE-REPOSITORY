// Grab DOM elements
const form = document.getElementById("form");
const city = document.getElementById("city");
const result = document.getElementById("result");

// Guard clause: Check if any of the DOM elements are missing
if (!form || !city || !result) {
  console.error("Form, city input, or result element not found in the DOM.");
  // Exit early if essential elements are missing
  throw new Error("Critical UI elements are not present.");
}

// Attach event listener to the form submit event
form.addEventListener("submit", async function (event) {
  event.preventDefault(); // Prevent default form submission behavior (page reload)

  const chosenCity = city.value.trim(); // Get city input and trim whitespace

  // Validate: If city name is empty, inform the user and exit early
  if (!chosenCity) {
    result.textContent = "Please enter a city name.";
    return;
  }

  result.textContent = `Loading...`; // Provide feedback that the request is in progress

  try {
    // Fetch geolocation data using encoded city name to handle special characters
    const geoResponse = await fetch(
      `https://geocoding-api.open-meteo.com/v1/search?name=${encodeURIComponent(
        chosenCity
      )}`
    );

    // Check if the response status is not OK (e.g., 404, 500)
    if (!geoResponse.ok) throw new Error("Geolocation API error");

    const geoData = await geoResponse.json();

    // Validate: If no results are returned, inform the user
    if (!geoData.results || geoData.results.length === 0) {
      result.textContent = "City not found.";
      return;
    }

    // Extract latitude and longitude from the first search result
    const { latitude, longitude } = geoData.results[0];

    // Fetch weather data using the coordinates
    const weatherResponse = await fetch(
      `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current_weather=true`
    );

    // Check if weather API responded successfully
    if (!weatherResponse.ok) throw new Error("Weather API error");

    const weatherData = await weatherResponse.json();

    // Validate: Make sure current weather data is available
    if (!weatherData.current_weather) {
      result.textContent = "Weather data unavailable.";
      return;
    }

    // Extract temperature and wind speed from the API response
    const temp = weatherData.current_weather.temperature;
    const wind = weatherData.current_weather.wind_speed;

    // Display the weather information to the user
    result.textContent = `Temperature: ${temp}°C | Wind: ${wind} km/h`;
  } catch (err) {
    // Handle and log any unexpected errors
    console.error("Error:", err);
    result.textContent = "Error fetching weather.";
  }
});
