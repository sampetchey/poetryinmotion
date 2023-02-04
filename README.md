# Poetry in Motion

<br/>

## Table Of Contents

- General Information
- Demo
- Wireframe Mockups
- Technologies
- UI
- UX
- Database
- Accessibility
- Challenges
- Features
- Defensive Design
- Testing
- Deployment
- Credits

<br/>

## General Information

The idea behind Poetry in Motion is to easily write, share and store poems as they are inspired. Creativity is often promoted by sharing and collaborating. The open nature of this site acts like a forum, with participants able to create, view and edit posts. 

The key to this site is in its simplicity, using the python language to communicate with a database on MongoDB containing the text. In addition the poem content, the database records the title, date it was written and authorship.

<br/>

## Demo

A live demo of the website can be found...

https://flask-poetry-in-motion-project.herokuapp.com/

<br/>

## Wireframe Mockups


## Technologies

### Languages

- HTML5
- CSS3
- Javascript
- Python3

### Libraries

- jQuery 3.4.1
- Dnspython 1.16.0
- Flask 1.1.1
- Flask-PyMongo 2.3.0
- PyMongo 3.10.1

### Tools

- MongoDB

### Hosting

- Github
- Heroku

<br/>

## UI

### Colors, Fonts & Layout

The overall layout of the page is aimed to be minimalistic in order to give the poems as much attention and real estate as possible.

- want to see if I can generate different colour poem cards - 

Otherwise keep it simple grey to maintain the focus on poetry.

### Responsiveness

The website has been built with a mobile-first approach and is highly responsive. The layout of poem cards changes over four different screen sizes, using the Materialize grid system

<br/>

## UX

The use of icons containing popup descriptors was to improve the simplicity and user experience. The words of the poems need to be center stage, so additional words of instructions looked clunky. Simple creative icons, promoting an action were judged as the best way of promoting a good user experience.


### User Stories

- As a user, I want to be able to add my own poems to the database (Create)
- As a user, I want to view the poems I have written (Read)
- As a user, I want to be able to edit my poems. (Update)
- As a user, I want to be able to delete poems. (Delete)

Future user stories/functions (TBA):

- As a user, I want to create my own profile/login where I can store my own poems and protect them from being edited by others. (TBA)
- As a user, I want to be able to comment on poems shared by others in the database. (TBA)
- As a user, I want to be able to quickly share poems with my friends on social media. (TBA)
- As a admin user I want to be able to edit and delete any poems in the database. (TBA)

<br/>

## Database

The database chosen for this is a non-relational database hosted on MongoDB.

The application uses 1 database collections, 'poems'.

The basic information of each poem (title, text, date and author) is stored as a key value whilst the content of each key is stored as a string.

<br/>

## Features

### Feature Overview

- Users can add new poems to the database. (Create)
- Users can browse through and view all poems contained in the database. (Read)
- Users can edit poems in the database. (Update)
- Users can delete poems in the database. (Delete)

### Feature 1 - Add Poems (Create)

**User story: "As a user, I want to be able to add poems to the database."**

Users can easily add poems to the database by navigating to the 'create' pen icon in the top left corner of the page.

This opens the 'create poem' page containing four main fields: Title, text, date written and 'written by'.   

The **Title** field allows the user to add a name/title of the poem.

The **text box** field allows the user to add the text of their poem.
The field expands as more text is added.

The **Date Written** field allows the user to enter a date when the poem was written.
This opens a calendar with today's date highlighted. Users can select the date their poem was written and it is saved in a text format.

### Feature 2 - Browse Poems (Read)

**User story: "As a user, I want to browse through and view all poems contained in the database."**

Poems are displayed in a grid format on the main page. They display a short summary, including the poem title and some content. An enlarge icon on each poem card prompts users to view the poem. It is then displayed in full when clicked. 

### Feature 3 - Edit Poems (Update)

**User story: "As a user, I want to be able to edit my poems."**

Each poem card has the same create button used the header. This prompts users to be able to edit each poem. The existing content is displayed on the edit poem fields where it can be changed. Clicking save updates these changes to the website. If the changes do not want to be kept, the cancel button will return the user to the main page without any changes made. 

## Feature 4 - Delete Poems (Delete)

**User story: "As a user, I want to be able to delete poems. (Delete)"**

Deleting a poem is possible from within the edit page. This is to avoid accidental deletes on the main page, where the full poems cannot be seen. Clicking delete removes the poem from the database and returns the user to the main page.

### Features Left To Implement

Going forward I would like to implement the following features:

- Login feature: Enabling users to create an account and log in using their chosen credentials.
- Restrict edit/delete: Only enabling logged in admins or logged in users to edit/delete poems.
- Search feature: Allow users to change the order in the poems are displayed, which could be alphabetical, by when it was written, or the author's name.
- Sharing feature: Create social share buttons for users to share poems on social media.
- Rating feature: Enabling users to vote on poems.
- Comment section: Enabling users to comment on shared poems.
- Backend Validation: Add further backend validation to further add to defensive design, such as to check when the delete button is clicked.
- Admin approval of new content, meaning a admin level user has to approve new poems before they become publicly available.

<br/>

## Testing

### Manual Testing



### Responsive design:



### Screen Size Testing/Compability



### Browser Compability

Browser             | Version           | Comments
--------------------|-------------------|---------
Firefox             | 72.0.2 (64-bit)   | No errors observed
Edge                | 44.18362.449.0    | No errors observed
Chrome              | 80.0.3987.122     | No errors observed
Opera               | 67.0.3575.31      | No errors observed

### Navigation

Navigation was kept simple with a fixed navbar at the page top in order to give the body as much real estate as possible.


<br/>

## Deployment



**How to deploy to Github:**



**How to clone this repository in order to run the code locally on your machine:**



**How to deploy to Heroku using GitPod:**



**Running the application locally using Gitpod:**



<br/>

## Credits

### Content

All of the text content on the website was written by me, Sam Petchey.


### Acknowledgements

A very big thank you goes to my Code Institute Mentor Brian M. for his invaluable support and guidance throughout this project.

### Disclaimer

The content of this website is for educational purposes only.