// initialize Leaflet
let map = L.map('map').setView([46.715, 1.71], 6);

// add the OpenStreetMap tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 18,
  attribution: '&copy; <a href="https://openstreetmap.org/copyright">OpenStreetMap contributors</a>'
}).addTo(map);

// show the scale bar on the lower left corner
L.control.scale().addTo(map);

// show a marker on the map
L.marker([50.715, 1.71]).bindPopup('France').addTo(map);


a = '127.0.0.1:8000'


let url = "http://www.simteiva.fr/api/v1/loc/"

function get_map_data(url) {
  fetch(url)
  .then(response => response.json())
  .then(function(data) {
    for (var i in data) {
      console.log("Creating markers")
      L.marker([data[i].lon, data[i].lat]).bindPopup().addTo(map);
    }
  })
}

console.log("getting map data")
get_map_data(url);
