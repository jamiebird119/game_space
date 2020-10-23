/* core logic from https://stripe.com/docs/payments/accept-a-payment#web-setup and
from https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware/4201818c00aa4ba3a0dae243725f6e32/90cda137ebaa461894ba8c89cd83291a/?child=first */

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

var style = {
  base: {
    backgroundColor:"#fff",
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

var card = elements.create('card', {style: style});
card.mount('#card-element');