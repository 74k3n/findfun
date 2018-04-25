  window.onload = function() {
 
    $("#loginBtn").click(function() {
      $("#login-modal").modal();
    });

    $("#regBtn").click(function() {
      $("#registration-modal").modal();
    });

    $("#signup-link").click(function() {
      $("#login-modal").modal('toggle');
      $("#registration-modal").modal('toggle');
    });

    $("#login-link").click(function() {
      $("#registration-modal").modal('toggle');
      $("#login-modal").modal('toggle');
    });

    $("#start").click(function() {
      getStart = document.getElementById("start");
      getStart.parentNode.removeChild(getStart);
      $(".fadeOutClass").fadeOut("slow", function() { 
        initMap();
        $("#map-container").attr('class', 'col-lg-12 my-auto');
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

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
  var csrftoken = getCookie('csrftoken');

  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
  });


  $('#loginForm').submit(function(e){
    var formId = $(this).attr('id');
    var submitBtn = $(this).find('input[type=submit]');
    $('#password-error').css('display', 'none');
    $('#no-user-error').css('display', 'none');
    e.preventDefault();
    $.ajax({

      type: "POST",
      data: $(this).serialize(),
      success: function(data){

        var login_response = jQuery.parseJSON(data);
        console.log(login_response);

        if(login_response.login == "Success") {
          setTimeout( function() {
            $('#login-modal').modal('toggle');
            setTimeout( function() {
              window.location.replace("/");
            }, 500);
          }, 500);
        } else if (login_response.user == "nouser"){
          $('#no-user-error').fadeIn("slow", function() {
          });
        } else if (login_response.user == "password wrong") {
          $('#password-error').fadeIn("slow", function() {
          });
        } else if ((login_response.user == "not active") && (login_response.username)) {
          $('#login-modal').modal('hide');
          document.getElementById(formId).reset();
        } else {
          if (login_response.login == "Failed") {
            alert("Invalid Login!");
          } else {
            document.getElementById(formId).reset();
            $('#login-modal').modal('hide');
            alert("An error has occured!");
          }
        }
      },
      error: function(data) {

        $('#login-modal').modal('hide');
        alert("An error has occured!");

      }
    });
  });


  $('#signupForm').submit(function(e){
    var formId = $(this).attr('id');
    var submitBtn = $(this).find('input[type=submit]');
    $('#username-exists-error').css('display','none');
    $('#e-mail-exists-error').css('display','none');
    $('#e-mail-invalid-error').css('display','none');
    $('#password-short-error').css('display','none');
    $('#password-nomatch-error').css('display','none');
    submitBtn.prop('disabled', true);
    e.preventDefault();
    $.ajax({
      type: "POST",
      data: $(this).serialize(),
      success: function(data){
        var signup_response = jQuery.parseJSON(data);
        console.log(signup_response);
        if (signup_response.username == "taken") {
          $('#username-exists-error').fadeIn("slow", function() {
          });
        } 
        if (signup_response.email == "taken") {
          $('#e-mail-exists-error').fadeIn("slow", function() {
          });
        }
        if (signup_response.email == "invalid") {
          $('#e-mail-invalid-error').fadeIn("slow", function() {
          });
        }
        if (signup_response.password == "short") {
          $('#password-short-error').fadeIn("slow", function() {
          });

        }
        if (signup_response.password_c == "nomatch") {
            $('#password-nomatch-error').fadeIn("slow", function() {
            });
        }

        if (signup_response.register == "Success") {
            $('#successReg').fadeIn("slow", function() {
            });
            setTimeout( function() {
              $('#registration-modal').modal('toggle');
              setTimeout( function() {
                window.location.replace("/");
              }, 500);
            }, 2000);
            


        } else if (signup_response.error == "True") {
            $('#registration-modal').modal('toggle');
            alert("An error has occured!");
        }
      },
      error: function(data) {
        $('#register-modal').modal('hide');
        alert("An error has occured!");
      }
    });
  });


  



