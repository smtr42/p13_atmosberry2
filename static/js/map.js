// initialize Leaflet
var map = L.map('map').setView([46.715, 1.71], 6);
L.marker([46.715, 1.71]).bindPopup('The center of the world').addTo(map);

// add the OpenStreetMap tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 18,
  attribution: '&copy; <a href="https://openstreetmap.org/copyright">OpenStreetMap contributors</a>'
}).addTo(map);

// show the scale bar on the lower left corner
L.control.scale().addTo(map);

// show a marker on the map
L.marker([46.715, 1.71]).bindPopup('The center of the world').addTo(map);


var circle = L.circle([46.715, 1.71], {
  color: 'red',
  fillColor: '#f03',
  fillOpacity: 0.5,
  radius: 5000
}).addTo(map);
