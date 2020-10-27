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


function toggleDetails(id){
    console.log(id)
    var x = document.getElementById(id)
    x.classList.toggle("d-none");
  }

