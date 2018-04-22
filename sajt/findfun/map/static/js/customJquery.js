  window.onload = function() {

      
    $("#loginBtn").click(function() {
      $("#loginModal").modal();
    });

    $('#loginForm').submit(function(e) {
      $('#loginModal').modal('toggle');
      return false;
    });

    $("#start").click(function() {
      getStart = document.getElementById("start");
      getStart.parentNode.removeChild(getStart);
      $(".fadeOutClass").fadeOut("slow", function() { 
        initMap();
        $("#map-container").attr('class', 'col-lg-10 my-auto');
        $("#locationInfoContainer").attr('class', 'col-lg-2 rounded my-auto');
        $("#map").fadeIn("slow", function() {
        });
        $("#locationInfoContainer").fadeIn("slow", function() {
        });
        $("#search").fadeIn("slow", function() {
        });
        $(".fadeInClass").fadeIn("slow", function() {
        });

      });
    });

  }
  function handleLocationError(browserHasGeolocation, infoWindow, pos) {
        infoWindow.setPosition(pos);
        infoWindow.setContent(browserHasGeolocation ?
                              'Error: The Geolocation service failed.' :
                              'Error: Your browser doesn\'t support geolocation.');
        infoWindow.open(map);
      }


