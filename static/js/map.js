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
L.marker([46.715, 1.71]).bindPopup('France').addTo(map);


var circle = L.circle([46.715, 1.71], {
  color: 'red',
  fillColor: '#f03',
  fillOpacity: 0.5,
  radius: 500
}).addTo(map);


let temp_url = "http://www.simteiva.fr/api/v1/data/"

function get_temperature_data(url) {
  fetch(url)
  .then(response => response.json())
  .then(function(data) {
      console.log(data)
      const lastItem = data.slice(-1).pop()
      console.log(lastItem)
      return lastItem
});}



let url = "http://www.simteiva.fr/api/v1/loc/"

function get_map_data(url) {
  fetch(url)
  .then(response => response.json())
  .then(function(data) {
    lastitem = get_temperature_data(temp_url)
    for (var i in data) {
      L.marker([data[i].lat, data[i].lon]).bindPopup(lastitem).addTo(map);
    }
  })
}
console.log("getting map data")
get_map_data(url);