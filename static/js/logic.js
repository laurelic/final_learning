// // Store our API endpoint inside queryUrl
var pUrl = "https://raw.githubusercontent.com/jgoodall/us-maps/master/geojson/hrr.geo.json"

//Create a greyscale view layer
var lightLayer = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibGF1cmVsaWMiLCJhIjoiY2pteG9icGYyM3ZvaTNxbnk2a2F6MDZmciJ9.ZQhdib9of9UJDKThb3b1QA", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.light",
});

//initialize the faultlines layer
var hrrLines = new L.layerGroup();



//initialize base maps
var baseMaps = {
    "Outline View": lightLayer
};

//initialize the layer maps

//build the map
var map = L.map("map-id", {
    center: [39.8283, -98.5795],
    zoom: 5,
    worldCopyJump: true,
    layers: [
        lightLayer,
        hrrLines,
    ]
});


//ensure the legend can flow with the zoom and position view
map.on('zoomed', onZoomend);
function onZoomend(){
    if(map.getZoom()>0){
        map.removeControl(info);
    }
};

//layer the ampes on each other
// L.control.layers(baseMaps, overlayMaps, {
//     collapsed: false
// }).addTo(map);

//draw the plate lines
d3.json(pUrl, function(data) {
    L.geoJSON(data, {
        onEachFeature: function(feature, layer) {
            layer.bindPopup(feature.properties.HRRCITY);
        },
        style: {
            color: "#fdae61",
            weight: 2,
            fillOpacity: 0
        }
    }).addTo(hrrLines);
});


//create a geoJson and filter by magnitude to add to each layer
// d3.json(qUrl, function(data) {
//     var allQuakes = L.geoJSON(data);

//         var quake0 = L.geoJSON(data, {
//             filter: function(feature, layer) {
//                 return feature.properties.mag < 1;
//             },
//             pointToLayer: function(feature, latlng) {
//                 return L.circleMarker(latlng, {
//                     radius: feature.properties.mag * 2,
//                     color: "#66bd63",
//                     weight: 1,
//                     fillColor: "#66bd63",
//                     fillOpacity: 0.6,
//                     }).on('click', function() {
//                         this.bindPopup(feature.properties.title).openPopup();
//                     });
//             }
//         });
        
//         var quake1 = L.geoJSON(data, {
//             filter: function(feature, layer) {
//                 return feature.properties.mag >= 1 && feature.properties.mag < 2;
//             },
//             pointToLayer: function(feature, latlng) {
//                 return L.circleMarker(latlng, {
//                     radius: feature.properties.mag * 2,
//                     color: "#66bd63",
//                     weight: 1,
//                     fillColor: "#66bd63",
//                     fillOpacity: 0.6,
//                     }).on('click', function() {
//                         this.bindPopup(feature.properties.title).openPopup();
//                     });
//             }
//         });

//         var quake2 = L.geoJSON(data, {
//             filter: function(feature, layer) {
//                 return feature.properties.mag >= 2 && feature.properties.mag < 3;
//             },
//             pointToLayer: function(feature, latlng) {
//                 return L.circleMarker(latlng, {
//                     radius: feature.properties.mag * 2,
//                     color: "#a6d96a",
//                     weight: 1,
//                     fillColor: "#a6d96a",
//                     fillOpacity: 0.6,
//                     }).on('click', function() {
//                         this.bindPopup(feature.properties.title).openPopup();
//                 })
//             }
//         });
//         var quake3 = L.geoJSON(data, {
//             filter: function(feature, layer) {
//                 return feature.properties.mag >= 3 && feature.properties.mag < 4;
//             },
//             pointToLayer: function(feature, latlng) {
//                 return L.circleMarker(latlng, {
//                     radius: feature.properties.mag * 2,
//                     color: "#fdae61",
//                     weight: 1,
//                     fillColor: "#fdae61",
//                     fillOpacity: 0.6,
//                     }).on('click', function() {
//                         this.bindPopup(feature.properties.title).openPopup();
//                 })
//             }
//         });
//         var quake4 = L.geoJSON(data, {
//             filter: function(feature, layer) {
//                 return feature.properties.mag >= 4 && feature.properties.mag < 5;
//             },
//             pointToLayer: function(feature, latlng) {
//                 return L.circleMarker(latlng, {
//                     radius: feature.properties.mag * 2,
//                     color: "#f46d43",
//                     weight: 1,
//                     fillColor: "#f46d43",
//                     fillOpacity: 0.6,
//                     }).on('click', function() {
//                         this.bindPopup(feature.properties.title).openPopup();
//                 })
//             }
//         });
//         var quake5 = L.geoJSON(data, {
//             filter: function(feature, layer) {
//                 return feature.properties.mag > 5;
//             },
//             pointToLayer: function(feature, latlng) {
//                 return L.circleMarker(latlng, {
//                     radius: feature.properties.mag * 2,
//                     color: "#d73027",
//                     weight: 1,
//                     fillColor: "#d73027",
//                     fillOpacity: 0.6,
//                     }).on('click', function() {
//                         this.bindPopup(feature.properties.title).openPopup();
//                 })
//             }
//         });


//         quake0.addTo(quakeLayers.tier0)
//         quake1.addTo(quakeLayers.tier1)
//         quake2.addTo(quakeLayers.tier2)
//         quake3.addTo(quakeLayers.tier3)
//         quake4.addTo(quakeLayers.tier4)
//         quake5.addTo(quakeLayers.tier5)
// });




