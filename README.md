# Taylor Brookes - Milestone Project 3
## Read-It

[Visit my live website here!](https://read-it-ms3.herokuapp.com/)

![]image here(www.)

# Table Of Contents

1. [Overview](#overview)
2. [UX](#ux)
3. [Design](#design)
4. [Features](#features)
5. [Technologies Used](#technologies-used)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Credits](#credits)

# Overview

Read-It is a site that is designed for people who are looking to keep a record of books that they have read, and share their reviews with others. 
Users are able to view books and reviews without needing to create an account. This allows new users to preview the site before registering so they have an idea of what the site is like. 
When a User decides to register, they will be able to log in with ease, create and manage their favourite books, and share them with other Users of the site. 

[Back to contents](#table-of-contents)

# UX

[Back to contents](#table-of-contents)

# Design

[Back to contents](#table-of-contents)

# Features

[Back to contents](#table-of-contents)

# Technologies Used

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

## Heroku.

This project is deployed using Heroku. The following steps were taken;

1.	Within GitPod, create the .gitignore and env.py files
2.	In the .gitignore file, set it to ignore the env.py file and __pycache__/ directory
3.	Within the env.py file, set the following environmental variable;
    - os.environ.setdefault(“IP”, “0.0.0.0”)
    - os.environ.setdefault(“PORT”, “5000”)
    - os.environ.setdefault(“SECRET_KEY”, “YOUR_SECRET_KEY”)
    - os.environ.setdefault(“MONGO_URI”, “mongo db link to go here”)
    - os.environ.setdefault(“MONGO_DBNAME”, “YOUR_DATABASE_NAME”)
4.	Make sure that the env.py file has been saved correctly and open the app.py file. Import OS, Flask and the env.py file.
5.	Create a requirements.txt file by typing in the terminal; pip3 freeze –local > requirements.txt
6.	For Heroku, you will also need a Procfile. Create this by using the terminal and typing; echo web: python app.py > Procfile. Access the Procfile and delete the bottom empty line to avoid any issues in the future
7.	Go to the Heroku site, and log in or create a profile. From the dashboard, select “New App”. Create a name for your app, select the correct region and click “Create App”.
8.	Navigate over to the “Deploy” tab and go to the “Deployment method” section. Click on GitHub
9.	Search for your repository name, and click “Connect” next to your repository name
10.	Next, go to the “Settings” tab, and scroll down to “Config Vars”. Click “Reveal config vars” 
11.	Enter the Key and Value pairs as per your env.py file;
    - IP : 0.0.0.0
    - PORT : 5000
    - SECRET_KEY : YOUR_SECRET_KEY
    - MONGO_URI : “mongo db link to go here”
    - MONGO_DBNAME : “your database name”
12.	Finally, go back to the “Deploy” tab, and scroll down to “Automatic deploys”. Click on “Enable Automatic Deploys” then “Deploy Branch”. 
13.	The app will now be built and upon completion, you will receive a message saying “Your app was successfully deployed.” 
14. You can now click on “Open App” which will launch the deployed app.

[Back to contents](#table-of-contents)

# Credits

[Back to contents](#table-of-contents)