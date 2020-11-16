# GameSpace

GameSpace is an E-commerce store centered around all things gaming. With a catalogue spanning many consoles and genres, users can efficiently 
find, purchase and experience new games. With twitch functionality users can also watch live gameplay to experience products prior to purchase. 
Users also have the option of saving their data to streamline the checkout process. Game developers can easily add new games and with twitch id return functionality
can easily set up twitch streaming for their games too. 

## Table of Content
1. [**UX**](#ux)
    - [**Strategy**](#strategy)
    - [**Scope**](#scope)
        - [**User Stories**](#user-stories)
    - [**Structure**](#structure)
        - [**Database Schema**](#database-schema)
    - [**Skeleton**](#skeleton)
        - [**Wireframes**](#wireframes)
    - [**Surface**](#surface)
        - [**Design**](#design)
        - [**Themes**](#themes)
        - [**Icons**](#icons)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features left to implement**](#features-left-to-implement)
    - [**Technologies Used**](#technologies-used)

3. [**Testing**](#testing)

4. [**Deployment**](#deployment)
        - HomeApp
        - GameApp
        - Twitch_API App
        - Bag App
        - Checkout App
        - Profiles App
        - Development to Deployment

5. [**Credits**](#credits)


7. [**Media**](#media)

8. [**Acknowledgements**](#acknowledgements)


## UX
The aim was to produce a sleak efficient E-commerce store that boosted game sales while,
engaging with the user and bringing them enjoyment and excitement for their purchase in the process.

### Strategy 

Given the type of business to consumer interaction the site uses there were three main points to strategy when designing:
- A streamlined checkout process with a minimum of steps in order to have a minimum of time between the emotional decision to purchase and 
the completion of that purchase for the user. 
- A stress on engagement through media to encourage a user's emotional connection to a product. 
- Simple interactivity and feedback to the user to create a simple and relaxing shopping experience.

### Scope
Functional features required:
- Game App
- Twitch App
- Bag App
- Checkout App
- Profiles App

Content required
- A way for user to experience/connect with a game without buying it (through media).
- Media aimed at enthusing the emotional decision behind a purchase. 
- Navigational streamlinging through a sidenav to allow easy use and efficiently transport users to the game they are interested in.

### User Stories
Follow the link for a full list of user stories -
**UserStories**(#https://docs.google.com/spreadsheets/d/1BrhNhX1Fiv-3raMT9crMyYyqyEfbfkIgaHa_c50PAEY/edit?usp=sharing)


### Structure
For information architecture see [**Database Schema**](#https://github.com/jamiebird119/game_space/blob/792ef9b4cec575be88bfac5a9415c218069f3f8a/database-schema.png)

### Skeleton 
For wireframes see

### Surface


#### Design
##### Theme
Bootswatch darkly was used for a general dulcet theme and styling with majority of elements following this format for a consistent 
and crisp user experience. Rounded images and use of cards for game details collate relavent information for the user.

##### Icons
Font Awesome is used to provide iconography that is consistent and informs the user to increase the usability of the site. Branded logos 
such as that of Playstation and Xbox were used from Font Awesome because of their notability and eyecatching familiarity assisting in giving the site purpose clearly
and adding value to the products provided.

## Features

Here is a list of current features:

- Account registry/login: A user can create their own profile in order to streamline the checkout process.
- User Profile Page: The user profile page allows users to update their information and view there order history.
- User Profile Image: A user can add a profile image via the profile page (See features to be added 'User reviews')
- Collapsible Order History: An order number can be extended to view the specific details or selected to open the order confirmation itself.
- Game Search/ Filter: A search bar and filter select allow users to located specific games via console/genre and to filter results via price/rating/etc.
- Collapsible Side Nav: The side nav allows quick game search functionality via selecting the console or genre they with to view games for. 
- Game Details: A game can be selected to view the specific details of that game.
- Twitch Stream Search: From the details page a user can view the live twitch streams currently available for that game. 
- Twitch Embed player: A user can select a stream to watch live that stream in an embed player
- Bag App: The user can add games to a bag and view their bag at any time to see the games, edit the quantities of that game or remove items. They can also see the total costs of their purchases.
- Discount Addition: When checking out the user can add a discount code to apply discounts.
- Checkout: A user can checkout by filling in the form, entering their card details and submitting.
- Add/Edit Game: As a superuser, for game developers, a user can add new games (see Twitch ID search) or edit existing games, should their cost or detials change.
- Remove Game: As a superuser, for game developers, a user can remove games from the list of available products.
- Search Twitch ID: As a superuser, the user can search using a game name for the Twitch Id relating to that game to add it when adding a product to set up Twitch stream functionality.

### Existing Features

**Account registry/login**
- A user can become a member on the site, by clicking the register button on the home page or on the navigation and filling the form.
- A user can verify their account, by following the link sent to them via email and clicking verify.
- A user can login, by clicking the login button, after registering and entering their username and password,
- A user can retrieve a lost password, by clicking forgot password, entering their email and following the link sent to them.

**User Profile Page** 
- A user can view their profile page, by clicking account and profile in the navigation menu once logged in.
- A user can update their account information, by filling in the form and clicking save.
- A user can uploda a profile image, by selecting the file input on their profile page, selecting the file from their computer and clicking save.
- A user can view their previous orders, by scrolling to the order history section and then selecting to view more information on the order they want to see or selecting the order number to open the history in a new window. 

**Game Search/Filter**
- A user can perform a keyword search, by entering the keyword into the search bar in the navigation menu and clicking search.
- A user can view the total number of responses for their given search, by looking above the games return on the results page.
- A user can filter results, by clicking the dropdown at the top of the results page and selecting the filter criteria they want to use.

**Side Navigation Menu** 
- A user can quickly search for a specific genre/console, by clicking the side burger icon and clicking the corresponding link they want to search in the menu that appears.

**Game Details**
- A user can view the details of a specific game, by clicking on its image or name to open the game details page.
- A user can add the game to their bag, by clicking add to bag.

**Twitch Streams Search**
- A user can return the streams for the current viewed game, by clicking Twitch in the container nav menu on the game's details page.

**Twitch Streams Embed Player** 
- A user can select a stream to watch, by clicking the image or channel name on the list of streams returned.

**Bag App**
- A user can view the items currently in their bag, by clicking the bag icon in the main nav menu.
- A user can adjust the quantity of an item in their bag, by clicking the quantity selector, in the item line, to edit the value and then clicking the update icon underneath.
- A user can remove an item from their bag, by clicking the X remove icon in the item line in their bag. 
- A user can go to the checkout page, by clicking the checkout button at the bottom of the bag page.

**Checkout/Discount**
- A user can see if their discount can be applied, by entering it into the corresponding field on the checkout page and clicking apply button.
- A user can purchase the items in their bag, by entering their personal details into the form and clicking pay and then viewing the order confirmation either on the page loaded or via email.

**Add/Edit Games**
- A super user can add a game, by selecting the product management page, clicking add game and filling in the details of the game they want to add.
- A superuser can edit a game, by selecting edit game on either the game's details page or on the product management page and editting the form to match updated game detials and then clicking save. 
- A superuser can remove a game, by clicking remove either on the game details page or on the product management page. 

**Twitch ID Search**
- A superuser can search the twitch ID for a specific game, by entering the game name to the field on the product management page and clicking search.
- A superuser can set up twitch functionality, by addint the returned id to the corresponding field when adding the game. 

### Features Left to implement

**Game Reviews Section**
- The user profile image upload is a precurser to this in that the idea would be to have the users image and review posted at the bottom of the game details page allowing it to be viewed by other users.
- This was not implemented as it was decided it was not necessary for the core functionality of the site, however could be added to increase user engagement.

**User Wishlist**
- The ability for users to add games to a wishlist on their account.
- This would allow developers to get feedback on game popularities and allow the user to recieve updates when their favourite games go on sale or have specific events.

**Twitch and Social Account Logins** 
- Allow users to register using twitch/discord account info.
- This would streamline the registration/login processes for the user and allow them to collate their information into one place.

**Additional game media**
- At present, apart from streams, game media is restricted to one image at a time. Ideally this would be updated to a gallery to give a more rounder,
view of the game without users having to watch a stream. For the purposes of load times and keeping file storage to a minimum this has not been implemented yet however.

**Links to related products**
- This feature would link similar games (for example sequels or prequels) or games that have similar genre tags. This would be viewed on the games page and 
would allow a browsing user to see other games they may like increasing the likelihood of them making a purchase. 

**SuperUser Account Models**
- Creating a model specifically to handle super users so each can only edit/update games they have added.


### Technologies Used
**HTML5, CSS3, Javascript, Python, Django**
- The languages used to deliver the site and the full stack framework in python. 
**Bootstrap**
- Used to provide front end consistency and aesthetically pleasing visuals
**Bootswatch Darkly**
- Theme used for element specific styling and overall theme of site
**JQuery + JqueryValidate**
- Utilised in JS to assist interactive functionality. Validate specifically used for real time form validations
**FontAwesome**
- Icons included for UX purposes
**AllAuth**
- Provides user authentification functionality and handles issue to do with this.
**CrispyForms**
- Used to alter form imput fields and provide consistency
**TwitchAPI**
- Allows for streaming of live gameplay from twitch to an embed player
**Stripe**
- Processes payment intents and provides webhook functionality for ensuring order creation.
**django-countries**
- Alters country input field on forms
**django-extensions**
- Utilised to create database schema visualisation
**psycopg and postgres**
- Hosts deployed version database for all models.
**Gunicorn**
- Used in deployment in the procfile setup
**smtp**
- Provides send mail functionality
**Amazon AWS S3**
- Hosts static and media files for deployed site
**Heroku**
- Serves the deployed version of the site to the public

## Testing

## Deployment

### Home App
Once django was imported and installed, the first thing created was the home app. As part of this a simple view and url were created and a full base template upon which
all future htmls would be built. This contained blocks for all major features and navigation and menu features present on each page. 

### Game App
The Game App followed this, with the creation of the Genre, Console and Game models. The genre and console models were linked by a many to many relationship 
with the game model. With model data then loaded using fixtures this relationship had to be added manually later in the site admin page. For feasibility it was the most
efficient method for the small sample data however for more extensive site data this ideally would be automated. 
Using the newly made models, the game and game details pages were created to render data to the user. With this search query functionality was created to handle 
keywords searches able to be matched to the name, description, console or genre of the game. In built filter select was added and a product count and search query 
given to users to show in results what they were searching.  

### Twitch API App
From the game details page a smaller navigation was included to make space for the twitch area. Using the twitch developer page
it became obvious that users first needed authorisation using an OAuth token. This was returned after setting up the required variables in twitch
and used to return a set of stream data for a particular game_id. Initially prior to the development of the streams return, a snippet was prototyped in repl.it using a fixed token and the name of a game to return a game_id, which became 
the basis for the return function used in product management when adding a new game. 
The stream data could then be rendered to the stream.html with a stream_id variable used to create a link to each stream that would then be loaded in the embed player on twitch_stream.html. 
(**NB** While each new user gets an OAuth token that is subsequently saved in the session cookies, it is not clear whether this value expires. Ideally code would be altered to included
this possible eventuality but for now it serves the purpose)

### Bag App
The bag app was created and along with bag.html a context processor was created for the bag contents. The functionality to add items to the bag
was also then added and to give each item a console and quantity. It was decided that items can only be added one at a time by the user instead of choosing a quantity, becuase how often would a user
want several hard copies of a game on the same console. The value can be editted in the bag app however. Bag tools were also created to work out totals.

### Checkout App
This lead nicely on to the checkout app which was created. As part of this the first items initialised were the Order, Orderlineitem and Discount models all of which 
would be necassary for full checkout. The OrderLineItem was an inline portion of the order model and was created for each item in a user bag. The Discount model was an optional 
foreign key field on the order model. Discount were applied using a charfield primary key code, and a json field containing information on to what games the 
discount applied. Due to the foreign key nature of the field it does mean that only one discount can be applied the a bag, however this is made aware to the user upon successful application 
of a discount. Forms were then produced from the OrderModel and integrated with stripe to the checkout page. The stripe payment intent was set up along with 
webhook and handler to process incomplete orders. 

### Profiles App
Lastly prior to deployment the profiles app was created with the UserProfile model being initialised first. This contains default information for the user
which linked to checkout and could be saved by the user when checking out. The user profile page was created to take in form data if the user wanted to change this. 
A profile image field was also added and could be updated using this profile page. This as it has been said earlier would be a precursor to a review section where the user image and review 
would be shown on the game details page when they leave a review. 

### Development to Deployment
The site was originally developed on Gitpod and can be run locally using:
`$ python3 manage.py runserver` 
This was then pushed to a heroku provider available at 
[GameSpace](#https://game-space-ecommerce.herokuapp.com/)

The differences between the developmental and deployment version are as follows:
- The developmental server hosts media and static files locally whereas the deployed version uses an Amazon S3 bucket for file hosting. 
- In development emails sent to users are sent to the development console whereas in the deployed version the backend uses smtp to sent the emails to the user. 
- On the developmental server an sql database is used where as on the deployed version a postgres database provides access to models. 
(**NB** It is IMPORTANT to note that on the developmental server not all genre/console to game relationships have been fully implemented, as they have on the deployed site. The developemental version will not allow the username
to add games without console values to the bag so if using dev version to test please use a game with a console value only!)
- Finally debug is set to false on the deployed version and USE_AWS is set to True. 

## Media
Game images and info for PC, PS and Xbox games from [Steam](#https://store.steampowered.com/)
Switch game info from [Nintento](#https://store.nintendo.co.uk/games/nintendo-switch/view-all.list)

## Acknowledgements
Thanks to Reuben Ferrante for his help and input and the other tutors at Code Institute for their help and patience. 





Test Stripe
Payment Intents API
When using the Payment Intents API with Stripe's client libraries and SDKs, ensure that:

Authentication flows are triggered when required (use the regulatory test card numbers and PaymentMethods.)
No authentication (default U.S. card): 4242 4242 4242 4242.
Authentication required: 4000 0027 6000 3184.
The PaymentIntent is created with an id empotency key to avoid erroneously creating duplicate PaymentIntents for the same purchase.
Errors are caught and displayed properly in the UI.