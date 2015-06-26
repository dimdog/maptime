L.mapbox.accessToken = 'pk.eyJ1IjoiYmVucmVpdGVyIiwiYSI6ImpzNmFSV3MifQ.vf_utYUIeH6BauUso8sn0w';
// Create a map in the div #map

var map = L.mapbox.map('map', 'benreiter.jo6c0mfh')
    .setView([42, -71.50], 15);


map.on('click', function(e) {
});



map.on('ready', function(e){
  var request = $.get("http://localhost:3000/data");
  request.success(function( data ) {
    for (var i = 0; i < data.length; i++){ 
      var capitol = data[i];
      var circle = L.circle([capitol.latitude, capitol.longitude], 4000).addTo(map);
      circle.data = capitol;
      circle.on('click', function(e) {
        console.log(this.data.state);
        
      });
    }
  })

});
map.on('moveend', function(e){
  
  console.log(map.getBounds());
});
