L.mapbox.accessToken = 'pk.eyJ1IjoiYmVucmVpdGVyIiwiYSI6ImpzNmFSV3MifQ.vf_utYUIeH6BauUso8sn0w';
// Create a map in the div #map

var minTime = 0;
var maxTime = 1000;
var map = L.mapbox.map('map', 'benreiter.jo6c0mfh')
    .setView([40.939467, -73.768145], 15);

var getWikiData = function (article){
  var request = $.get("https://boiling-depths-4153.herokuapp.com/wiki?article="+article);
  request.success(function( data ) {
    console.log(data);
  });
}

var circles = [];

map.on('ready', function(e){
  var bounds = map.getBounds();
  var swla = bounds._southWest.lat;
  var swln = bounds._southWest.lng;
  var nela = bounds._northEast.lat;
  var neln = bounds._northEast.lng;
  var request = $.get("https://boiling-depths-4153.herokuapp.com/data?swla="+swla+"&swln="+swln+"&nela="+nela+"&neln="+neln); //use join. jesus.
  request.success(function( data ) {
    for (var i = 0; i < data.length; i++){ 
      var article = data[i];
      var circle = L.circle([article.lat, article.lng], 200).addTo(map);
      circle.data = article;
      circles.push(circle);
      circle.on('click', function(e) {
        console.log("here");
        console.log(this.data.article);
        getWikiData(this.data.article);
        
      });
    }
  });



});
map.on('moveend', function(e){
   
  var bounds = map.getBounds();
  var swla = bounds._southWest.lat;
  var swln = bounds._southWest.lng;
  var nela = bounds._northEast.lat;
  var neln = bounds._northEast.lng;
  var request = $.get("https://boiling-depths-4153.herokuapp.com/data?swla="+swla+"&swln="+swln+"&nela="+nela+"&neln="+neln); //use join ffs.
  request.success(function( data ) {
    for (var i = 0; i < circles.length; i++){
      map.removeLayer(circles[i]);
    }
    for (var i = 0; i < data.length; i++){ 
      var article = data[i];
      var circle = L.circle([article.lat, article.lng], 200).addTo(map);
      circle.data = article;
      circles.push(circle);
      circle.on('click', function(e) {
        getWikiData(this.data.article);
        
      });
    }
  });
});

var slider = $('.nstSlider').nstSlider({
    "crossable_handles": false,
    "left_grip_selector": ".leftGrip",
    "right_grip_selector": ".rightGrip",
    "value_bar_selector": ".bar",
    "value_changed_callback": function(cause, leftValue, rightValue) {
        $(this).parent().find('.leftLabel').text(leftValue);
        minTime = leftValue;
        $(this).parent().find('.rightLabel').text(rightValue);
        maxTime = rightValue;
    }
});
slider.nstSlider('set_range', -2000, 2015);
slider.nstSlider('set_position', 500, 750);

