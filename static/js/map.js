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
// L.marker([46.715, 1.71]).bindPopup('The center of the world').addTo(map);


let url = "http://www.simteiva.fr/api/v1/loc/"

function get_map_data(url) {
  fetch(url)
  .then(response => response.json())
  .then(function(data) {
    for (var i in data) {
      L.marker([data[i].lat, data[i].lon]).bindPopup('Meow').addTo(map);
    }
  })
}

get_map_data(url);