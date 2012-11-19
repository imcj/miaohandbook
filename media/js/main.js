String.prototype.format = function() {
  var args = arguments;
  return this.replace(/{(\d+)}/g, function(match, number) { 
    return typeof args[number] != 'undefined'
      ? args[number]
      : match
    ;
  });
};

function getParameterByName(name)
{
  name = name.replace(/[\[]/, "\\\[").replace(/[\]]/, "\\\]");
  var regexS = "[\\?&]" + name + "=([^&#]*)";
  var regex = new RegExp(regexS);
  var results = regex.exec(window.location.search);
  if(results == null)
    return "";
  else
    return decodeURIComponent(results[1].replace(/\+/g, " "));
}

function page_index ( ) {
  $.getJSON ( "/api/v1/cat/", function ( data ) {
      $.each ( data['objects'], function ( index, cat ) {
          $(".home ul").append ( "<li><a href=\"detail.html?id={0}\"><img src=\"/media/{1}\" /></a></li>".format ( cat['id'], cat['avatar'] ) )
      } );
  } )
}

function page_detail ( ) {
  var cat_id = getParameterByName ( 'id' );
  $.getJSON ( "/api/v1/cat_full/{0}/".format ( cat_id ), function ( data ) {
      $("#text-summary").html ( data['summary'] );
  } );
  $.getJSON ( "/api/v1/cat_photo/?cat={0}".format ( cat_id ), function ( data ) {
      $.each ( data['objects'], function ( index, photo ) {
          $(".detail ul").append ( "<li><a href=\"/media/{0}\"><img src=\"/media/{1}\" /></a></li>".format ( photo['480'], photo['220'] ) );
      } );
      var
          options = {},
          instance = window.Code.PhotoSwipe.attach( $('#Gallery a'), options );
  } );
}

document.addEventListener ( 'DOMContentLoaded', function ( ) {
  var path = document.location.pathname;
  var path = path.substr ( path.lastIndexOf ( "/" ) + 1 );

  switch ( path ) {
    case "index.html": {
      page_index ( );
      break;
    }
    case "detail.html": {
      page_detail ( );
    }
  }

} );

