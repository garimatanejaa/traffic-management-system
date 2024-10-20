let map, marker;
let autocomplete;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 40.7128, lng: -74.0060},
        zoom: 13
    });

    marker = new google.maps.Marker({
        map: map,
        draggable: true
    });

    autocomplete = new google.maps.places.Autocomplete(
        document.getElementById('location'),
        {types: ['geocode']}
    );

    autocomplete.addListener('place_changed', onPlaceChanged);
    
    google.maps.event.addListener(marker, 'dragend', function() {
        map.setCenter(marker.getPosition());
    });
}

function onPlaceChanged() {
    const place = autocomplete.getPlace();
    if (place.geometry) {
        map.setCenter(place.geometry.location);
        marker.setPosition(place.geometry.location);
    }
}

document.getElementById('prediction-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const position = marker.getPosition();
    const codedDay = document.getElementById('coded-day').value;
    const weather = document.getElementById('weather').value;
    const isHoliday = document.getElementById('is-holiday').value;

    fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            lat: position.lat(),
            lng: position.lng(),
            CodedDay: codedDay,
            Weather: weather,
            IsHoliday: isHoliday
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('result').innerHTML = `<div class="alert alert-danger">${data.error}</div>`;
        } else {
            document.getElementById('result').innerHTML = `<div class="alert alert-info">Predicted Traffic at (${data.lat.toFixed(4)}, ${data.lng.toFixed(4)}): <strong>${data.prediction}</strong></div>`;
            
            // Add a colored circle to the map
            new google.maps.Circle({
                strokeColor: data.prediction === 'Congested' ? '#FF0000' : '#00FF00',
                strokeOpacity: 0.8,
                strokeWeight: 2,
                fillColor: data.prediction === 'Congested' ? '#FF0000' : '#00FF00',
                fillOpacity: 0.35,
                map: map,
                center: {lat: data.lat, lng: data.lng},
                radius: 1000
            });
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerHTML = '<div class="alert alert-danger">An error occurred. Please try again.</div>';
    });
});

initMap();