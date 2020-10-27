let countrySelected = $("#id_default_country").val();
if (!countrySelected) {
  $("#id_default_country").css("color", "#adb5bd");
}
$("#id_default_country").change(function () {
  countrySelected = $(this).val();
  if (!countrySelected) {
    $(this).css("color", "#adb5bd");
  } else {
    $(this).css("color", "#444");
  }
});

$(document).ready(function () {
  document.querySelectorAll("input").forEach((item) => {
    item.addEventListener("change", function(item) {
      console.log();
      isValid = $(this).valid();
      if (isValid) {
        $(this).addClass("is-valid");
      } else {
        $(this).addClass("is-invalid");
        $(this).next('.error').addClass('invalid-feedback')
      }
    });
  });
});

function toggleDetails(id){
    console.log(id)
    var x = document.getElementById(id)
    x.classList.toggle("d-none");
  }

