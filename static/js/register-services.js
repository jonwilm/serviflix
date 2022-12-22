var stepDemoVertical = new Stepper(document.querySelector('#stepperDemoVertical'), {
  linear: false,
  animation: true,
});
stepDemoVertical.next();
stepDemoVertical.previous()

var cSelect = document.querySelectorAll("[data-choices]");
cSelect.forEach(el => {
  const t = { ...el.dataset.choices ? JSON.parse(el.dataset.choices) : {},
  ...{
    classNames: {
      containerInner: el.className,
      input: "form-control",
      inputCloned: "form-control-sm",
      listDropdown: "dropdown-menu",
      itemChoice: "dropdown-item",
      activeState: "show",
      selectedState: "active"
    }
  }
}
new Choices(el, t)
});

$('.card-membership').on('click', function() {
  $('.card-membership').removeClass('bg-primary')
  $('.card-membership').addClass('bg-primary-light')
  $(this).removeClass('bg-primary-light')
  $(this).addClass('bg-primary')
  $('input[type=radio]', this).prop('checked', 'true')
})

// Upload Images
function logoPreview(e) {
  if (e.files && e.files[0]) {
    if (e.files[0].type.match('image.*')) {
      var reader = new FileReader();
      reader.onload = function(e) {
        $('#logo-preview').html("<img src='"+e.target.result+"'><i class='bx bxs-edit bx-md text-primary'></i>")
        $('#reset-logo').removeClass('d-none')
      }
      reader.onerror = function(e) {
        $('#logo-preview').html("<i class='bx bxs-x-circle bx-md text-danger'></i>")
        $('#reset-logo').removeClass('d-none')
      }
      reader.readAsDataURL(e.files[0]);
    } else {
      $('#logo-preview').html('<p class="m-0 px-3 text-center text-danger">Formato invalido<br>Seleccione una imagen</p><i class="bx bxs-image-add bx-md text-primary"></i>')
    }
  }
}
function portadaPreview(e) {
  if (e.files && e.files[0]) {
    if (e.files[0].type.match('image.*')) {
      var reader = new FileReader();
      reader.onload = function(e) {
        $('#portada-preview').html("<img src='"+e.target.result+"'><i class='bx bxs-edit bx-md text-primary'></i>")
        $('#reset-portada').removeClass('d-none')
      }
      reader.onerror = function(e) {
        $('#portada-preview').html("<i class='bx bxs-x-circle bx-md text-danger'></i>")
        $('#reset-portada').removeClass('d-none')
      }
      reader.readAsDataURL(e.files[0]);
    } else {
      $('#portada-preview').html('<p class="m-0 px-3 text-center text-danger">Formato invalido<br>Seleccione una imagen</p><i class="bx bxs-image-add bx-md text-primary"></i>')
    }
  }
}
$('#logo-preview').on('click', function() {
  $('#id_logo').click()
})
$('#reset-logo').on('click', function() {
  $('#id_logo').val('')
  $('#logo-preview').html("<i class='bx bxs-image-add bx-md text-primary'></i>")
  $(this).addClass('d-none')
})
$('#portada-preview').on('click', function() {
  $('#id_image').click()
})
$('#reset-portada').on('click', function() {
  $('#id_image').val('')
  $('#portada-preview').html("<i class='bx bxs-image-add bx-md text-primary'></i>")
  $(this).addClass('d-none')
})

// Google Maps
function initMap() {
  var latitud = -31.399084
  var longitud = -64.3344318
  coord = {
    lng: longitud,
    lat: latitud
  }
  generarMapa(coord)
}
function generarMapa(coord) {
  var mapa = new google.maps.Map(document.getElementById("mapa"), {
    zoom: 15,
    center: new google.maps.LatLng(coord.lat, coord.lng)
  })
  var marcador = new google.maps.Marker({
    map: mapa,
    draggable: true,
    position: new google.maps.LatLng(coord.lat, coord.lng)
  })

  infoWindow = new google.maps.InfoWindow()
  const locationButton = document.getElementById('current-location');
  locationButton.classList.add("custom-map-control-button");
  locationButton.addEventListener("click", () => {
    // Try HTML5 geolocation.
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude,
          };

          infoWindow.setPosition(pos);
          mapa.setCenter(pos);
          marcador.setPosition(pos);
          document.getElementById('id_lat').value = pos.lat
          document.getElementById('id_lng').value = pos.lng
        },
        () => {
          handleLocationError(true, infoWindow, mapa.getCenter());
        }
      );
    } else {
      // Browser doesn't support Geolocation
      handleLocationError(false, infoWindow, mapa.getCenter());
    }
  });

  marcador.addListener('dragend', function(event) {
    document.getElementById('id_lat').value = this.getPosition().lat()
    document.getElementById('id_lng').value = this.getPosition().lng()
  })
}
function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(
    browserHasGeolocation
      ? "Error: El servicio de Geolocalización ha fallado."
      : "Error: Navegador no soporta Geolocalización."
  );
  infoWindow.open(mapa);
}

// Add Redes
var contadorRedes = 1
function addSocial() {
  let clon = $(".add-social:first").clone()
  clon.children('select').attr('name', 'socialnetwork_set-'+contadorRedes+'-name')
  clon.children('select').attr('id', 'id_socialnetwork_set-'+contadorRedes+'-name')
  clon.children('input').attr('name', 'socialnetwork_set-'+contadorRedes+'-url')
  clon.children('input').attr('id', 'id_socialnetwork_set-'+contadorRedes+'-url')
  clon.children('input').val('')
  contadorRedes++
  $('#id_socialnetwork_set-TOTAL_FORMS').val(contadorRedes)
  clon.appendTo("#content-redes");
}

// Add Paymethod
var contadorPaym = 1
function addPaymethod() {
  let clon = $(".add-paymethod:first").clone()
  clon.children('select').attr('name', 'paymentmethods_set-'+contadorPaym+'-paymethod')
  clon.children('select').attr('id', 'id_paymentmethods_set-'+contadorPaym+'-paymethod')
  contadorPaym++
  $('#id_paymentmethods_set-TOTAL_FORMS').val(contadorPaym)
  clon.appendTo("#content-paymethod");
}