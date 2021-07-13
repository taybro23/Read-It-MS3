# Taylor Brookes - Milestone Project 3
## Read-It

[Visit my live website here!](https://read-it-ms3.herokuapp.com/)

![]image here(www.)

# Table Of Contents

1. [Overview](#overview)
2. [UX](#ux)
    - [User Stories](#user-stories)
    - [Wireframes](#wireframes)
3. [Design](#design)
4. [Features](#features)
5. [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Database](#database)
    - [Frameworks Libraries and Programmes](#frameworks-libraries-and-programmes)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Credits](#credits)

# Overview

Read-It is a site that is designed for people who are looking to keep a record of books that they have read, and share their reviews with others. 
Users are able to view books and reviews without needing to create an account. This allows new users to preview the site before registering so they have an idea of what the site is like. 
When a User decides to register, they will be able to log in with ease, create and manage their favourite books, and share them with other Users of the site. 

[Back to contents](#table-of-contents)

# UX

## Target Audience

The target audience for my site is people who are avid readers. They’ll be able to keep a list of the books they have rated and reviewed, as well as view other people’s reviews. 

## User Stories

### First time and returning users

All users of this site will be looking for similar things, outlined below;
-	Easy and clear navigation throughout the entire site on all device types.
-	To be able to view/preview the site before registering an account.
-	Have clear Registration/Log In pages.
-	Have the ability to add their own reviews and keep a record of them.
-	To be able to edit and delete reviews posted.
-	Search the site to find other reviews.
-	For the review information to be clear and concise.
-	Find links where they can purchase the books.
-	To be provided with contact information and social links.
-	Once finished, to securely log out of the site.

### Site owner/admin

-	For users to have easy access to all areas of the site.
-	For the site to be clear and concise.
-	The ability for users to contact them for any feedback/issues surrounding the site.
-	To be able to add, edit and delete book reviews.
-	Have access to an admin account whereby the owner/admin can add affiliate links to each review left by a user, and earn money from those links. (For project purposes, these links will NOT be affiliate links, and will only be links to the books on Amazon.)

## Wireframes

To create the wireframes, I used Balsamiq. I started with the mobile wireframes and worked my way to a larger screen size. Below are the links to the completed wireframes;

-	[Mobile](static/images/wireframes/mobilewf.pdf)
-	[Desktop/Laptop](static/images/wireframes/desktopwf.pdf)

I kept the original ideas for the site as when I built it, I felt that everything worked well and I didn’t need to amend anything. 


[Back to contents](#table-of-contents)

# Design

[Back to contents](#table-of-contents)

# Features

[Back to contents](#table-of-contents)

# Technologies Used

## Languages

-	HTML5
-	CSS3
-	Javascript
-	Python3

## Database

-	Mongo DB

## Frameworks Libraries and Programmes

Flask
- A python web framework.

Jinja
- Template used by Flask and Python.

PyMongo
- Python tool for use with Mongo DB.

Werkzeug
- WSGI web application library used by Flask and Python.

Balsamiq - https://balsamiq.com/ 
- I used Balsamiq to create the wireframes for my project.

Font Awesome – https://fontawesome.com/ 
- Icons from Font Awesome were used throughout the site.  

Github – https://github.com/ 
- Github was used to store the code for my project.

Gitpod – https://gitpod.io/workspaces/ 
- I used Gitpod to write the code for my project and push it to Github.

Google Fonts – https://fonts.google.com/ 
- I used Google Fonts to find the right font for my project.

Heroku - https://id.heroku.com/login 
- Heroku was used to deploy the project. 

jQuery – https://jquery.com/
- jQuery was used for the main functions due to ease of use.

MaterializeCSS - https://materializecss.com/ 
- For this project, I used MaterializeCSS to help with the styling, layout and responsiveness of the finished site.


[Back to contents](#table-of-contents)

# Testing

[Back to contents](#table-of-contents)

# Deployment

## GitHub Pages

This site was created and managed using GitHub and GitPod. Outlined below is how this site was deployed.

-	Log into GitHub.
-	Go to the repository list and select the project you are looking to deploy.
-	Below the repository name is a menu. Select settings.
-	Scroll down to the “GitHub Pages” section of the page.
-	Under the subheading “Source”, select the branch you wish to deploy.
-	The page will refresh. Scroll down to the “GitHub Pages” section again and just below the heading, there will be a tick, with the line “Your site is published at…” and the URL.
-	Copy the URL and paste it into a new tab/window to view the live site.

## Forking the repository

Forking the repository allows you to make a copy of the original, and make changes without amending the original. 

-	Log into GitHub.
-	Select the repository you are looking for.
-	At the top of the repository, in line with the repository name and on the right hand side, will be a “Fork” button. Select this and it will fork the repository for you.
-	You will then have a copy of the original repository in your GitHub account repository list.

## Cloning the repository

You can run your own version by cloning the repository. To make a local clone, follow the steps below.

-	Log into GitHub.
-	Locate the repository for the site you are wishing to clone.
-	On the left of the green “GitPod” button will be a dropdown menu that says “Code”.
-	Select it and copy the URL under the “HTTPS” tab.
-	Open your preferred terminal. 
-	Type “git clone” and paste the copied URL.
-	Press Enter, and the code will be cloned. 

## Heroku

This project is deployed using Heroku. The following steps were taken;

1.	Within GitPod, create the .gitignore and env.py files.
2.	In the .gitignore file, set it to ignore the env.py file and pycache/ directory.
3.	Within the env.py file, set the following environmental variable;
    - os.environ.setdefault(“IP”, “0.0.0.0”)
    - os.environ.setdefault(“PORT”, “5000”)
    - os.environ.setdefault(“SECRET_KEY”, “YOUR_SECRET_KEY”)
    - os.environ.setdefault(“MONGO_URI”, “mongo db link to go here”)
    - os.environ.setdefault(“MONGO_DBNAME”, “YOUR_DATABASE_NAME”)
4.	Make sure that the env.py file has been saved correctly and open the app.py file. Import OS, Flask and the env.py file.
5.	Create a requirements.txt file by typing in the terminal; pip3 freeze –local > requirements.txt.
6.	For Heroku, you will also need a Procfile. Create this by using the terminal and typing; echo web: python app.py > Procfile. Access the Procfile and delete the bottom empty line to avoid any issues in the future.
7.	Go to the Heroku site, and log in or create a profile. From the dashboard, select “New App”. Create a name for your app, select the correct region and click “Create App”.
8.	Navigate over to the “Deploy” tab and go to the “Deployment method” section. Click on GitHub.
9.	Search for your repository name, and click “Connect” next to your repository name.
10.	Next, go to the “Settings” tab, and scroll down to “Config Vars”. Click “Reveal config vars”.
11.	Enter the Key and Value pairs as per your env.py file;
    - IP : 0.0.0.0
    - PORT : 5000
    - SECRET_KEY : YOUR_SECRET_KEY
    - MONGO_URI : “mongo db link to go here”
    - MONGO_DBNAME : “your database name”
12.	Finally, go back to the “Deploy” tab, and scroll down to “Automatic deploys”. Click on “Enable Automatic Deploys” then “Deploy Branch”. 
13.	The app will now be built and upon completion, you will receive a message saying “Your app was successfully deployed”. 
14. You can now click on “Open App” which will launch the deployed app.

[Back to contents](#table-of-contents)

# Credits

[Back to contents](#table-of-contents)