let countrySelected = $("#id_default_country").val();
if (!countrySelected) {
  $("#id_country").css("color", "#888");
}
$("#id_country").change(function () {
  countrySelected = $(this).val();
  if (!countrySelected) {
    $(this).css("color", "#888");
  } else {
    $(this).css("color", "#444");
  }
});

