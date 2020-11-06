# GameSpace

GameSpace is an E-commerce store centered around all things gaming. With a catalogue spanning many consoles and genres, users can efficiently 
find, purchase and experience new games. With twitch functionality users can also watch live gameplay to experience products prior to purchase. 
Users also have the option of saving their data to streamline the checkout process. Game developers can easily add new games and with twitch id return functionality
can easily set up twitch streaming for their games too. 

## Table of Content
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
        - [**Themes**](#themes)
        - [**Wireframes**](#wireframes)
        - [**Icons**](#icons)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features left to implement**](#features-left-to-implement)
    - [**Technologies Used**](#technologies-used)

3. [**Testing**](#testing)

4. [**Deployment**](#deployment)

5. [**Credits**](#credits)


7. [**Media**](#media)

8. [**Acknowledgements**](#acknowledgements)


## UX
GameSpace has been created with user experience in mind for ease of use and a stress on bringing value to said user. Search functionality 
can be found in several places, including the sidenav and search function in the navbar the aim is to give the user a variety of easy ways to find 
the exact product they want. Filter options also give the browsing user alternative ways to rank results. Each game can be selected to get more
in depth information and to view twitch streams. The bag tools allow users to see what they currently are set to purchase and how much they have to spend to get free 
delivery. 

### User Stories
Follow the link for a full list of user stories -
**UserStories**(#https://docs.google.com/spreadsheets/d/1BrhNhX1Fiv-3raMT9crMyYyqyEfbfkIgaHa_c50PAEY/edit?usp=sharing)


### Design
Axure was used to create detailed wireframes for all resolutions. 

#### Theme
Bootswatch darkly was used for a general dulcet theme and styling with majority of elements following this format for a consistent 
and crisp user experience. 


Game images and info from Steam.com
Swtich game info from https://store.nintendo.co.uk/games/nintendo-switch/view-all.list

Test Strip
Payment Intents API
When using the Payment Intents API with Stripe's client libraries and SDKs, ensure that:

Authentication flows are triggered when required (use the regulatory test card numbers and PaymentMethods.)
No authentication (default U.S. card): 4242 4242 4242 4242.
Authentication required: 4000 0027 6000 3184.
The PaymentIntent is created with an id empotency key to avoid erroneously creating duplicate PaymentIntents for the same purchase.
Errors are caught and displayed properly in the UI.