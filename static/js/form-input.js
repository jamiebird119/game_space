function check_input(input) {
  document.querySelectorAll(input).forEach((item) => {
    item.addEventListener("change", function (item) {
      isValid = $(this).valid();
      if (isValid) {
        $(this).addClass("is-valid");
      } else {
        $(this).addClass("is-invalid");
        $(this).next(".error").addClass("invalid-feedback");
      }
    });
  });
}
$(document).ready(function () {
  check_input("textarea");
  check_input("input");
  check_input("select");
  check_input("#card_element");
});
