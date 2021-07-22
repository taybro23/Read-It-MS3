# Taylor Brookes - Milestone Project 3
## Read-It Testing Documentation

# Table Of Contents

1. [Code Validation](#code-validation)
    - [HTML5](#html5)
    - [CSS3](#css3)
    - [JS](#js)
    - [Python](#python)
2. [Features and Functionality](#features-and-functionality)
    - [Responsiveness](#responsiveness)
    - [Features (A-Z)](#features)
3. [User Stories](#user-stories)
4. [Bugs and Fixes](#bugs-and-fixes)

# Code Validation

### HTML5
[W3C HTML Validator](https://validator.w3.org/#validate_by_input) was used to check my HTML – result.

### CSS3 
[W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) was used to make sure my CSS was compliant – result.

### JS
[JSLint](https://www.jslint.com/) was used to check my JavaScript – result.

### Python
[PEP8 Online](http://pep8online.com/) was what I used to make sure my Python Code was PEP8 compliant – result.

[Back to contents](#table-of-contents)

# Features and Functionality

### Responsiveness

-	The responsiveness of this site was tested using a Windows Laptop, an Apple MacBook Pro, a Samsung Galaxy S20 mobile phone and an iPhone 12. 

## Features
## (A-Z)

### Add Book Review

-	Form – All inputs work as intended, with requirements being displayed and inputs highlighted red if not filled in and required. 
-	Submit – Submit button correctly sends the data to the database.

### Book Review Cards

-	Hover – I added a hover effect on the book review cards so that the user can easily see which book review they are looking at, and this works well.  
-	Info & Review Icon – The Info & Review icon works as intended, sliding up the book review information over the book image.
-	Buttons – The correct buttons are displayed depending on whether the user is logged in, logged out or is the Admin of the site. 

### Bookmark Book Function

-	I had a bit of trouble when implementing this feature as I was initially not writing my code correctly to link it to the database. I looked carefully over my code and the database I was trying to connect it to, and managed to work it out so that the bookmark was saved on the database, and displayed on the ‘My Profile’ page.

### Buttons

-	Links - All buttons on the site have been tested to make sure that the direct the users to the relevant page. 
-	Hover – Every button has an alternative colour when hovered over, and they were all checked to make sure the correct colours were displayed when hovered over.

### Delete Book Function

-	Delete function was tested with a number of books from both the ‘Book Reviews’ page and the ‘My Profile’ page. Both were working as expected.

### Edit Book Review

-	Pre-fill – When a user edits a book review, the form is correctly filled in with the information they have previously entered. 
-	Buttons – Both the cancel and edit review buttons work as intended, with the edit review button correctly updating the database. 

### Flash Messages

-	All flash messages were tested across the site to make sure they popped up when they should, and that the text in the flash message is correct and not misspelt. 

### Footer

-	Links - All footer social links were tested, and correctly navigated the user to the relevant site. 
-	The footer remained at the bottom of the site regardless of amount of content, and this was tested by removing all content from the page, and re-entering it. 

### Logout

-	The logout feature works as intended and correctly logs the user out of the site. 

### Navbar

-	Links - All navbar links were thoroughly tested on both laptop and mobile views, and they all worked as intended, and directed the user to the correct page.

### Register/Log In Forms

-	Requirements – Username/Password requirements are listed below the Password input on the register page so users know when signing up what the requirements are for a new Username/Password. I have tested these features to make sure they work.
-	Username – Both forms were extensively tested to make sure that the same username could not be used more than once, and that the incorrect password could not be used to access an account that did not belong to them. 
-	Empty Fields – If a required input is left blank, it will turn red and a notification will pop up below the field, asking for the field to be filled in. 

### Search Bar

-	Search – Search function was tested by adding books and then searching for the titles and authors. All searches worked as intended. If no search results are found, correct message is shown.
-	Clear – The clear button clears the search bar and refreshes the page. This too works as intended.


[Back to contents](#table-of-contents)

# User Stories

[Back to contents](#table-of-contents)

# Bugs and Fixes

When I added the search functionality to the site and reloaded the webpage, I got the following error;

TypeError: object of type 'Cursor' has no len()

This was my python code at the time of the error;

![Code error 1](static/images/testing/code1.jpg)

I was unsure how to fix this and I managed to find a fix by consulting the student slack channels. Someone else had had the same issue before me so I looked over the comments and found the fix in the comments. 
Student Abi Harrison had spoken to a course tutor and found the following fix;

The books were being returned but not as a list in def books(). I changed this by wrapping mongo.db.books.find() in list(). This rectified the issue, and the fixed code is below.

![Code fix](static/images/testing/code2.jpg)


[Back to contents](#table-of-contents)