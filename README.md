# The Plough Pub

![Responsice Mockup](media/images/preview.png)
![Responsice Mockup](media/images/preview_2.png)
![Responsice Mockup](media/images/preview_3.png)

The Plough website is designed to be a responsive website on both mobiles and laptops. The aim of this site to help a local business have an online presence to boost business.
This website will display events they are hosting, their menus, allow users to make a reservation, as well as allowing staff to edit, adjust and delete bookings.

## Link to Live site here

<https://the-plough.herokuapp.com/>

---

## Contents

- [The Plough Pub](#the-plough-pub)
  - [Link to Live site here](#link-to-live-site-here)
  - [Contents](#contents)
- [User Experience](#user-experience)
  - [Client goals](#client-goals)
  - [First time visitor goals](#first-time-visitor-goals)
  - [Returning visitor goals](#returning-visitor-goals)
- [Design](#design)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Imagery](#imagery)
  - [Wireframes](#wireframes)
- [Database models](#database-models)
- [Features](#features)
  - [Home Page](#home-page)
  - [Menu page](#menu-page)
  - [Events page](#events-page)
  - [Booking page](#booking-page)
  - [Staff page](#staff-page)
- [Future Implementations](#future-implementations)
- [Accessibility](#accessibility)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
  - [Lighthouse testing](#lighthouse-testing)
  - [Testing user stories](#testing-user-stories)
  - [Manual Testing](#manual-testing)
- [Credits](#credits)
  - [Content](#content)
  - [ Media](#media)
  - [ Acknowledgments](#acknowledgments)

---

# User Experience

The Plough website allows users and staff to do multiple things. Firstly, users will be able to make, reservations which can then be edited or cancelled by staff through a booking system. Staff can also create events, and the users cn see what events that will be occuring at the pub.

Having an online presence will help boost this businesses returns, as it will reach a wider audience who will be able to see what food, drink and events the Plough offers. First time users and especially those that have never visited the establishment may discover something that interests them and encourage them to book and visit the Pub. Returning members can keep visiting to see the latest events and book again

## Client goals

- To have an online presence where users can find out basic information about the pub

* To receive bookings from customers
* To be able to accept, edit and cancel bookings
* To be able to display the pubs menu's to viewers
* To be able to add, edit and delete events

## First time visitor goals

- To be able to gain more information about the pub (address, contact information etc)

* To be able to make a booking for the pub
* To be able to view the latest events happening at the pub
* To be able to view the different menus

## Returning visitor goals

- See the latest events
- To book a table again

# Design

## Colour Scheme

![Colors](media/images/colors.png)

I decided to go for darker greys and white color scheme, as it matches the images I would be using. It also gives a more classier feel which matches the pub itself, and I want users to feel this is a fancy establishement.

## Typography

4 fonts where used in the making of this project, Lato, Playfair Display, Roboto Slab and Montserrat.

Playfair display was used as it most reflected the real world logo of The Plough. As for the other fonts, I ensured they matched the style of the website and they are clear and easy to read. Roboto Slab was used on the main page as it is bolder and larger, which will draw attention to it

## Imagery

The images used on this site are meant to be images of the pub itself. As this is an example project, real images are not available, therefore images that closely reflect the Plough pub have been used. On the menu page, the images used are to show some of the products related to said menu that the Plough sell.

## Wireframes

<details>
<summary>Home page</summary>
- Desktop View
  
![Desktop View](media/images/Wireframe_home.png)

- Mobile view

![Mobile View](media/images/Wireframe-home-mobile.png)

</details>

<details>
<summary>Events page</summary>
- Desktop + Mobile View
  
![Desktop View](media/images/wireframe_event.png)

</details>

<details>
<summary>Menu's page</summary>
- Desktop View + Mobile View
  
![Desktop View](media/images/Wireframe_menus.png)

</details>
<details>
<summary>Menu's Detail page (Breakfast, Main, Drinks)</summary>
- Desktop View + Mobile View
  
![Desktop View](media/images/Wireframe-menu-detail.png)

</details>

<details>
<summary>Booking page</summary>
- Desktop View + Mobile view
  
![Desktop View](media/images/Wireframe_booking.png)

</details>

<details>
<summary>Admin/ Staff page</summary>
- Desktop View
  
![Desktop View](media/images/Wireframe-Admin-page.png)
</details>

# Database models

- These are entity relationship diagrams that visually show the structure of the database tables which were used as a reference when building the models

<details>
<summary>Events model</summary>

![Events model](media/images/Model-Events.png)

</details>

<details>
<summary>Booking model</summary>

![Booking model](media/images/Model-booking.png)

</details>

# Features

This website has several pages and some of these are viewable or appear differently depending on:

- If the user is logged in
- If the user is logged in as a customer
- If the user is signed in as an admin/ member of staff.

All pages use the base html, which contains a responsive navigation bar allowing users to get around the site. The Plough Logo is always on the top left, and also acts as a button to take the users back to the home page. If the user is not signed in, the nav bar contains a "Register" and a "Log In" button. If a customer is signed in, this will change to just a "Log out" button. If an admin/ staff member is logged in, an additional "Staff" button will appear on the nav bar which will take them to the staff home page.

All pages also contain the same footer, which has all the contact information of the pub, as well as the address and the social media links.

## Home Page

- Large masthead with a background image of the Plough with a button which can take users straight to the booking page

* 3 cards underneath each with relevant images to what they are related to
  - Reservation card
  - Menu's card
  - Book now card

## Menu page

- Contains 3 cards that the users can click on to see the different menus. A breakfast menu, a main menu and a drinks menu

## Events page

- As a customer user or a user that has not logged in, this page shows all the different events that will be happening at the Plough. Each event has a relevant image, date, time, information and the price.

* If logged in as an admin, a button at the top of the page will be visable allowing the user to add an event. Clicking this button takes the user to the add events page, where the user can fill out the form.

## Booking page

- Allows users to make a reservation. This page contains a form which users can fill out, and the restaurant can approve, edit or delete these bookings. The restaurant will email the customer to comfirm their booking.

* Only users that are logged in can access this page, if they are not logged in, they will be asked to log in.

## Staff page

- Only accessable to staff users. This page allows the user to see all bookings, ordered by date. Here, users can edit, approve and delete bookings.

# Future Implementations

- Fuctionality for users to view their own bookings, edit and cancel them
- Email functionality for booking confirmations to be sent automatically when approved, or when changes have been made
- Automatically approve bookings, and decline when certain criteria has been made such as duplicate booking, or too many bookings on the same day/time.
- Forgot password and change password functionality
- Allow social media log in
- Allow admin to edit users, delete users, create new staff users
- Automatic testing

# Accessibility

- Used semantic HTML
- Distinct color differences so all text is easy to read
- Using descriptive alt attributes on images on the site.
- Providing information for screen readers where there are icons used and no text

# Technologies Used

- HTML5 - Provides the content and structure for the website.
- CSS - Provides the styling for the website.
- Django - A model-view-template framework used to create The Plough
- Bootstrap - Used to style the front end
- JavaScript - Creates the interactive aspects of the website
- Python - Provides the functionality of the website.
- Compressor - Used to compress the images.
- Am I Responsive? - To show the website image on a range of devices.
- GitHub - Used to host and deploy the website.
- Gitpod - Used to create the code for the site
- Google Chrome DevTools - Used to test responsiveness and debug.
- Balsamiq - Used to create the wire-frame.
- Cloudinary - Used to host all static files .
- Heroku - Used to deploy the website
- Google Fonts - To import the fonts used on the website.
- Font Awesome - For the iconography on the website.
- PEP8 Validation - Used to validate Python code
- HTML Validation - Used to validate HTML code
- CSS Validation - Used to validate CSS code
- JSHint Validation - Used to validate JavaScript code

# Testing

- Validated by using online validation tools W3C HTML Validator, W3C CSS Validator, JSHint JavaScript Validator and the PEP8 Online Validator.

* HTML

  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fjamiebradford123.github.io%2FThe-Plough-Booking%2F)

* CSS
  - No errors were found when passing through the official [(Jigsaw) validator](/media/images/jigsaw-css.png)
* JavaScript
  - No errors were found when passing through the official [Jshint validator]()
    - The following metrics were returned:
    - There are 7 functions in this file.
    - Function with the largest signature take 1 arguments, while the median is 1.
    - Largest function has 12 statements in it, while the median is 2.
    - The most complex function has a cyclomatic complexity value of 4 while the median is 1.
* PEP8 EACH FILE

## Lighthouse testing

- Home Page
  ![Lighthouse home](media/images/lighthouse-main.png)

* Menu Page
  ![Lighthouse menu](media/images/lighthouse-menu.png)
* Events Page
  ![Lighthouse event](media/images/lighthouse-events.png)
* Booking Page
  ![Lighthouse book](media/images/lighthouse-book.png)
* Staff Page
  ![Lighthouse staff](media/images/lighthouse-staff.png)

## Testing user stories

- User story 1 - Have an online site containing basic information
  - As a user, I can find out more about this business by viewing the website and seeing basic information such as who they are, where they are and what they do.
  - Acceptance Criteria:
    - Website contains the name of the business and contact details such as phone number and address
      - Completed
    - Home page with a quick summary of what the business does - food, events, drinks
      - Completed
    - Menu's page to show the range of food and drink on offer
      - Completed

* User story 2 - Have an events page

  - As a Site Admin, I can create, edit and delete events that are taking place at the plough

  - Acceptance Criteria:
    - Only accessible by and admin/ staff log in
      - Completed
    - Ability to create, edit and delete an event
      - Completed

* User story 3 - Booking system
  - As a site user, I can create a booking for the restaurant.
  - Acceptance Criteria:
    - Create a booking
      - Completed
    - Select the date and time
      - Completed
    - Select the number of people
      - Completed
* User story 5- Accept and manage bookings
  - As a site admin I can manage all bookings by accepting, edit and delete bookings
  - Acceptance Criteria:
    - Admin page displaying all bookings
      - Completed
    - Ability to accept or reject booking
      - Completed
    - Ability to edit and delete a booking
      - Completed

## Manual Testing

Manual testing was used to ensure all aspects of this site work as intended.

| Page              | Test                                                                         | Completed? |
|-------------------|------------------------------------------------------------------------------|------------|
| Home Page         |                                                                              |            |
|                   | All visuals load (CSS, HTML)                                                 | Yes        |
|                   | Nav bar compresses on smaller screens                                        | Yes        |
|                   | Each nav link takes the user to the correct page                             | Yes        |
|                   | Book' button takes user to booking page                                      | Yes        |
|                   | Event's, Menu's and reserve a table buttons takes user to relevant page      | Yes        |
|                   | All images are clear, not stretched and visible                              | Yes        |
|                   | Page is viewable on small and large screen sizes                             | Yes        |
|                   | All text is readable                                                         | Yes        |
|                   | Footer is clear and readable on all sizes                                    | Yes        |
|                   | Footer links takes user to the correct social media site                     | Yes        |
| Menu page         |                                                                              | Yes        |
|                   | Nav bar works correctly                                                      | Yes        |
|                   | Page is clear on different screen sizes                                      | Yes        |
|                   | All font is readable                                                         | Yes        |
|                   | Each button takes user to relevant menu                                      | Yes        |
|                   | All images are clear and load on different screen sizes                      | Yes        |
|                   | Footer works and is visible |                                                | Yes        |
| Breakfast menu |  |                                                                              | Yes        |
|                   | Nav bar working and visible                                                  | Yes        |
|                   | Image loads in and is clear, and not stretched                               | Yes        |
|                   | Page title is clear and visible                                              | Yes        |
|                   | Menu is clear and readable on all screen sizes                               | Yes        |
| Main menu         |                                                                              | Yes        |
|                   | Nav bar working and visible                                                  | Yes        |
|                   | Image loads in and is clear, and not stretched                               | Yes        |
|                   | Page title is clear and visable                                              | Yes        |
|                   | Menu is clear and readable on all screen sizes                               | Yes        |
| Drinks menu       |                                                                              | Yes        |
|                   | Nav bar working and visable                                                  | Yes        |
|                   | Image loads in and is clear, and not stretched                               | Yes        |
|                   | Page title is clear and visable                                              | Yes        |
|                   | Menu is clear and readable on all screen sizes                               | Yes        |
| Events page       |                                                                              |            |
|                   | Add event button is only visable to logged in staff users                    | Yes        |
|                   | Add event button takes user to the add event form page                       | Yes        |
|                   | Edit and delete buttons on each event are only visable for admin/staff users | Yes        |
|                   | Edit button takes user to the edit form page                                 | Yes        |
|                   | Delete event deletes the event                                               | Yes        |
|                   | All images are clear and unstretched (unless user uploads a poor image)      | Yes        |
| Booking page      |                                                                              |            |
|                   | All fields must be entered                                                   | Yes        |
|                   | Number of guests must be a number                                            | Yes        |
|                   | Date must be in the future and a valid date                                  | Yes        |
|                   | Selecting a time works                                                       | Yes        |
|                   | A valid email must be entered                                                | Yes        |
|                   | Requests must be entered with max 200 characters                             | Yes        |
|                   | Successfully creates a booking that can be seen on the staff page            | Yes        |
| Create event page |                                                                              |            |
|                   | All fields must be entered                                                   | Yes        |
|                   | Date must be in the future and a valid date                                  | Yes        |
|                   | Selecting a time works                                                       | Yes        |
|                   | Content must be filled in                                                    | Yes        |
|                   | Image uploads correctly                                                      | Yes        |
|                   | Place holder image uploads correctly if no image is entered                  | Yes        |
|                   | Price must be entered and be a number                                        | Yes        |
| Edit Event        |                                                                              |            |
|                   | Add event button is only visable to logged in staff users                    | Yes        |
|                   | Add event button takes user to the add event form page                       | Yes        |
|                   | Edit and delete buttons on each event are only visable for admin/staff users | Yes        |
|                   | Edit button takes user to the edit form page                                 | Yes        |
|                   | Delete event deletes the event                                               | Yes        |
|                   | All images are clear and unstretched (unless user uploads a poor image)      | Yes        |
|                   | Event is successfully updated                                                | Yes        |
| Log in pages      |                                                                              |            |
|                   | Log in with correct information works correctly                              | Yes        |
|                   | Incorrect log ins are rejected                                               | Yes        |
|                   | User that is not logged in can register successfully                         | Yes        |
|                   | A logged in user will see a log out page instead                             | Yes        |
|                   | A staff/admin user will see a staff tab                                      | Yes        |
|                   | A registered user can log out successfully                                   | Yes        |
| Staff page        |                                                                              |            |
|                   | Table is readable on all screensizes                                         | Yes        |
|                   | Edit booking button takes user to the edit booking page                      | Yes        |
|                   | Approve button approves unapproved bookings                                  | Yes        |
|                   | Approve button disapproves approved bookings                                 | Yes        |
|                   | Delete button deletes the booking                                            | Yes        |
|                   | An edited booking changes to the new details                                 | Yes        |
|                   |                                                                              | Yes        |

# Credits

- Readme template - <https://github.com/kera-cudmore/Bully-Book-Club#bully-book-club-website>
- CI Tutorial projects - Hello Django and I Think I Blog for inspiration and a basis to build on

## Content

All content has been written by myself for a fictional pub

##  Media

All images were compressed using Optimizilla - https://imagecompressor.com/

All images are stored on Cloudinary - https://cloudinary.com/

Image sources

- Home page
  - Masthead - https: //res.cloudinary.com/dcmdyoyxi/image/upload/v1683464637/plough-homepage_gxlubk.webp
  - Event - https://billetto.co.uk/blog/wp-content/uploads/2020/03/victor-clime-0L-IgR1-3fE-unsplash-1024x683.jpg
  - Menu - https://i.etsystatic.com/11154166/r/il/fadea7/1948539947/il_fullxfull.1948539947_ey9l.jpg
  - Reserve a table - https://images.squarespace-cdn.com/content/v1/58c66929d1758e424e0341b6/1650618178048-O22DEXXAANY9MOUP664I/The+Akeman+Tring+restaurant+menu.jpg?format=2500w
- Menu page
  - Breakfast - https://www.egginfo.co.uk/sites/default/files/styles/large_main_image/public/2018/04/half%20english_charlie%20richards%20resized.jpg?h=9ef2d775&itok=6zYCw6LN
  - Breakfast page - https://ichef.bbci.co.uk/news/976/cpsprodpb/11AA1/production/_126635327_gettyimages-938158500.jpg
  - Main - https://res.cloudinary.com/dcmdyoyxi/image/upload/v1683464495/dinner_smyrkl.jpg
  - Main page - https://foolproofliving.com/wp-content/uploads/2020/05/Easy-Dinner-Recipes.jpg
  - Drinks - https://www.whitbreadinns.co.uk/en-gb/autumn-winter-2022/whitbread_inns_aw_drinks_2_32.png
  - Drinks page - https://www.beefeater.co.uk/en-gb/autumn-winter-2022/beefeater_autumn_winter_8_32.png
- Events page - All images uploaded by user and stored on cloudinary

##  Acknowledgments

- The Code Institute courses and walkthroughs for inspiration for this froject
- The Code Institute tutors for helping me with bugs and issues