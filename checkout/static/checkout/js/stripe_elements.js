/* core logic from https://stripe.com/docs/payments/accept-a-payment#web-setup and
from https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware/4201818c00aa4ba3a0dae243725f6e32/90cda137ebaa461894ba8c89cd83291a/?child=first */

var stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
var clientSecret = $("#id_client_secret").text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

var style = {
  base: {
    backgroundColor: "#fff",
    color: "#444",
    fontFamily: "Lato",
    fontSmoothing: "antialiased",
    fontSize: "15px",
    "::placeholder": {
      color: "#444",
    },
  },
  invalid: {
    color: "#dc3545",
    iconColor: "#dc3545",
  },
};

var card = elements.create("card", { style: style });
card.mount("#card-element");

card.addEventListener("change", function (event) {
  var errorDiv = document.getElementById("card-errors");
  if (event.error) {
    errorDiv.innerHTML(`
        <span class="icon" role="alert"><i class="fas fa-x"></i></span>
        <span>${event.error.message}</span>`);
  } else {
    errorDiv.textContent = "";
  }
});

var form = document.getElementById("payment-form");

form.addEventListener("submit", function (ev) {
  ev.preventDefault();
  card.update({ disabled: true });
  $("#submit-button").attr("disabled", true);
  stripe
    .confirmCardPayment(clientSecret, {
      payment_method: {
        card: card,
      },
    })
    .then(function (result) {
      if (result.error) {
        var errorDiv = document.getElementById("card-errors");
        // Show error to your customer (e.g., insufficient funds)
        errorDiv.innerHTML(`
        <span class="icon" role="alert"><i class="fas fa-x"></i></span>
        <span>${result.error.message}</span>`);
        card.update({ disabled: false });
        $("#submit-button").attr("disabled", false);
      } else {
        if (result.paymentIntent.status === "succeeded") {
          form.submit();
        }
      }
    });
});
