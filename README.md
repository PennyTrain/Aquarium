venv\Scripts\activate
# Glass Fish Aquarium

## Introduction
---
* Glass Fish Aquarium is a fun website where users can leave reviews on the Aquarium, along with that users can also post their at home aquariums and create their own account!
Glass Fish Aquarium is built using Django using Python, JavaScript, CSS and HTML.
[View live project here](https://glassfish-aquarium-e2673bbcde39.herokuapp.com/)
---

### Wireframe Mockups!
---

* The Home Page
---
![Home page browser wireframe](/static/images/readme-images/browser-home.png)
![Home page phone wireframe](/static/images/readme-images/phone-home.png)
---

* The Gallery Page
---
![Gallery page browser wireframe](/static/images/readme-images/browser-gallery.png)
![Gallery page phone wireframe](/static/images/readme-images/phone-gallery.png)
---

* The Visit Page
---
![Visit page browser wireframe](/static/images/readme-images/browser-visit.png)
![Visit page phone wireframe](/static/images/readme-images/phone-visit.png)
---

* The Sign up Page
---
![Sign up page browser wireframe](/static/images/readme-images/browser-sign-up.png)
![Sign up page phone wireframe](/static/images/readme-images/phone-sign-up.png)
---

* The Log in Page
---
![Log in page browser wireframe](/static/images/readme-images/browser-log-in.png)
![Log in page phone wireframe](/static/images/readme-images/phone-log-in.png)
---

* The Log out Page
---
![Log out page browser wireframe](/static/images/readme-images/browser-log-out.png)
![Log out page phone wireframe](/static/images/readme-images/phone-log-out.png)
---

* The Reviews Page
---
![Review page browser wireframe](/static/images/readme-images/browser-reviews.png)
![Review page phone wireframe](/static/images/readme-images/phone-reviews.png)
---

* The Review details Page
---
![Review details page browser wireframe](/static/images/readme-images/browser-review-detail.png)
![Review details page phone wireframe](/static/images/readme-images/phone-review-detail.png)
---

* How the review looks in detail when you are the author
---
![Detailed review for superusers/authors browser wireframe](/static/images/readme-images/browser-review-owner.png)
![Detailed review for superusers/authors browser wireframe](/static/images/readme-images/phone-review-owner.png)
---

* The Create a post Page
---
![Create post page browser wireframe](/static/images/readme-images/browser-review-create.png)
![Create post page phone wireframe](/static/images/readme-images/phone-review-create.png)

## User Stories

* There are more user stories at [Link to github project](https://github.com/users/PennyTrain/projects/2)
### The Strategy Plane
* The Glass Fish Aquarium website is designed to be a site for users to create reviews and share their at home aquariums with other users!

- First Time Visitor Goals

1. As a first time visitor, I want to be able to navigate the site easily.
2. As a first time visitor, I want it to be clear whether or not I am logged in.
3. As a first time visitor, I want to be able to see reviews.

- Returning Visitor Goals

1. As a returning visitor, I want to be able to create an account easily.
2. As a returning visitor, I want to be able to post reviews.

- Frequent Visitor Goals

1. As a frequent visitor, I want to be able to update my reviews.
2. As a frequent visitor, I want to be able to update my account.

- Organization Goals 

1. As an organization, we want to promote the Aquarium and bring in more business.
2. As an organization, we want to be easily accessible to interested parties.
3. As an organization, we want a consistent base of people who love aquariums and form an online community!

## Features
---

### Home Page Video
---
* The Homepage features a video os an aquarium

![Screenshot of the homepage](/static/images/readme-images/home-page.png)


### Gallery 
---
* The Gallery page is full of fun facts about fish along with photos

![Screenshot of the gallery](/static/images/readme-images/gallery.png)

### Responsive Navbar
---
* The navbar is responsive and collapsable

![Screenshot of the Navbar when mobile](/static/images/readme-images/responsive-navbar.png)

### Functioning Profile
---
* The website has a fully functioning profile aspect

![Screenshot of a profile](/static/images/readme-images/profile-crud.png)

### Functioning Review
---
*

![Screenshot of a review](/static/images/readme-images/review-crud.png)

## Future Enhancements

* In the future, I would like to add comments, therefore users can comment on others reviews and photos of their fish at home.
* In the future, I would like to add a search bar to the gallery page therefore people can search if their is a specific fish they would like to see.
* In the future,I would like to add a search bar to the review page therefore people can search if their is a specific review and/or at home aquarium they would like to see!


## Testing
---

#### Testing Strategy

- Throughout this project I was doing manual testing as I went, therefore if there was a bug it was found and dealt with right away.

### Python Validation
---

To check that my code was valid I ran it all through [Pep8](https://pep8ci.herokuapp.com/)
I found that in some files, such as the env.py file the lines were too long however these were only the links, the cloudinary links in my models! However for readibility I have left them...  
I ran all of these apps through PEP8
- reviews
- glassfish
- main
- accounts

### CSS Validation
---

- I ran my css through [W3 Validator](https://jigsaw.w3.org/css-validator/validator)
![CSS Validator Response](/static/images/readme-images/css-validation.png)


### HTML Validation
---
- When validating my HTML I inspected the page in order to get the raw HTML due to Django using template tags it is not possible to just copy and paste the files.
- The only errors I got were stray th, tr and td elements when using {{forms}}.
- However all original HTML written by me contained no errors
- I ran my HTML through [W3 Validator](https://validator.w3.org/)

- Home Page: No errors
- Gallery Page: No errors
- Reviews Page: No errors
- Log Out Page: No errors
- Review Detail Page: No errors
- Delete Profile Page: No errors
- Sign Up Page: There were errors in the built in forms I used, however I cannot access them to change it. The only errors I got were stray th, tr, td and ul elements when using {{forms}}.
- Log In Page: There were errors in the built in forms I used, however I cannot access them to change it. The only errors I got were stray th, tr and td elements when using {{forms}}.
- Profile Page: There were errors in the built in forms I used, however I cannot access them to change it. The only errors I got were stray th, tr and td elements when using {{forms}}.
- Create Review Page: There were errors in the built in forms I used, however I cannot access them to change it. The only errors I got were stray th, tr and td elements when using {{forms}}.
- Update Review Page: There were errors in the built in forms I used, however I cannot access them to change it. The only errors I got were stray th, tr and td elements when using {{forms}}.

### Unregistered site user access 
---
The overall site navigation consisted of me manually testing the site and navigating around it to ensure that all my views and everything is rendering to the site correctly.

### CRUD Functionality
---
- Reviews CRUD

![Screenshot of the review testcase](/static/images/readme-images/test-case3.png)

- Account CRUD

![Screenshot of the account testcase](/static/images/readme-images/test-case4.png)

### Responsiveness

![Screenshot of the responsive testcase](/static/images/readme-images/test-case2.png)

### Links (navbar & footer)

![Screenshot of the links testcase](/static/images/readme-images/test-case1.png)

### Notable Bugs

* During testing I noticed that users could access any part of the page if they typed the url in manually, to fix this I added this on top of my views a decorator @login_required(login_url="/accounts/login/").


#### Technologies Used

* asgiref==3.7.2
* autopep8==2.0.4
* beautifulsoup4==4.12.3
* bleach==6.1.0
* blinker==1.7.0
* certifi==2023.11.17
* cffi==1.16.0
* charset-normalizer==3.3.2
* click==8.1.7
* cloudinary==1.36.0
* colorama==0.4.6
* crispy-bootstrap4==2023.1
* crispy-bootstrap5==0.7
* cryptography==41.0.7
* defusedxml==0.7.1
* dj-database-url==0.5.0
* dj3-cloudinary-storage==0.0.6
* Django==4.2.9
* django-allauth==0.57.0
* django-bootstrap-v5==1.0.11
* django-crispy-forms==2.1
* django-environ==0.11.2
* django-summernote==0.8.20.0
* Flask==3.0.0
* gunicorn==20.1.0
* idna==3.6
* itsdangerous==2.1.2
* Jinja2==3.1.2
* MarkupSafe==2.1.3
* oauthlib==3.2.2
* psycopg2==2.9.9
* pycodestyle==2.11.1
* pycparser==2.21
* PyJWT==2.8.0
* python3-openid==3.2.0
* requests==2.31.0
* requests-oauthlib==1.3.1
* setuptools==69.0.3
* six==1.16.0
* soupsieve==2.5
* sqlparse==0.4.4
* tzdata==2023.4
* urllib3==1.26.18
* webencodings==0.5.1
* Werkzeug==3.0.1
* whitenoise==5.3.0

## Deployment


### Project Deployment

The site was deployed via Heroku, and the live link can be found here - [
To deploy the project through Heroku I followed these steps:
* Sign up / Log in to [Heroku](https://www.heroku.com/)
* From the main Heroku Dashboard page select 'New' and then 'Create New App'
* Give the project a name - I entered The-Pantry and select a suitable region, then select create app. The name for the app must be unique.
* This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, navigate to the resources tab.
* Add the database to the app, in the add-ons section search for 'Heroku Postgres', select the package that appears and add 'Heroku Postgres' as the database
* Navigate to the setting tab, within the config vars section copy the DATABASE_URL to the clipboard for use in the Django configuration.
* Within the django app repository create a new file called env.py - within this file import the os library and set the environment variable for the DATABASE_URL pasting in the address copied from Heroku. The line should appear as os.environ["DATABASE_URL"]= "Paste the link in here"
* Add a secret key to the app using os.environ["SECRET_KEY"] = "your secret key goes here"
* Add the secret key just created to the Heroku Config Vars as SECRET_KEY for the KEY value and the secret key value you created as the VALUE
* In the settings.py file within the django app, `import Path from pathlib, import os and import dj_database_url`
* insert the line `if os.path.isfile("env.py"): import env`
* remove the insecure secret key that django has in the settings file by default and replace it with `SECRET_KEY = os.environ.get('SECRET_KEY')`
* replace the databases section with `DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))}` ensure the correct indentation for python is used.
* In the terminal migrate the models over to the new database connection
* Navigate in a browser to cloudinary, log in, or create an account and log in. 
* From the dashboard - copy the CLOUDINARY_URL to the clipboard
* in the env.py file created earlier - add os.environ["CLOUDINARY_URL"] = "paste in the Url copied to the clipboard here"
* In Heroku, add the CLOUDINARY_URL and value copied to the clipboard to the config vars
* Also add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars
* this key value pair must be removed prior to final deployment
* Add the cloudinary libraries to the list of installed apps, the order they are inserted is important, `cloudinary_storage` goes above `django.contrib.staticfiles` and `cloudinary` goes below it.
* in the Settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
* Link the file to the templates directory in Heroku `TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')`
* Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]
* Add Heroku to the ALLOWED_HOSTS list the format will be the app name given in Heroku when creating the app followed by .herokuapp.com
* In your code editor, create three new top level folders, media, static, templates
* Create a new file on the top level directory - Procfile
* Within the Procfile add the code - web: guincorn PROJECT_NAME.wsgi
* In the terminal, add the changed files, commit and push to GitHub
* In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors.
* Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

#### Create a clone of this repository
Creating a clone enables you to make a copy of the repository at that point in time - this lets you run a copy of the project locally:
This can be done by:
* Navigate to https://github.com/PennyTrain/Aquarium/
* click on the arrow on the green code button at the top of the list of files
* select the clone by https option and copy the URL it provides to the clipboard
* Navigate to your code editor of choice and within the terminal change the directory to the location you want to clone the repository to.
* type 'git clone' and paste the https link you copied from github
* press enter and git will clone the repository to your local machine

#### Installing requirements.txt
Due to certian packages being required the system nneds to know which ones in order to runt his project as successfully as possible.
* Everytime I installed a new package to use on the development I ran the command `pip freeze --local > requirements.txt`
* This saves the current packages that are required to the requirements.txt file itself. 

* However when Cloning or starting in a new workspaces the content(packages) within the requirements.txt will need to be installed this is done by the following command `pip install -r requirements.txt`


## Credits
--- 
### Content
---
* The text for all pages was created by myself.
* Icons used for the various links on the site were taken from [Font Awesome](https://fontawesome.com/)
* The reference material on HTML and CSS provided by [w3schools.com](https://www.w3schools.com/)

### Media
---
* The css reset was provided by [css reset](http://meyerweb.com/eric/tools/css/reset/)
* The Favicon, links and meta code were generated by [Realfavicongenerator.net](https://realfavicongenerator.net).
* The images used on the webisite were generated by [Pixabay](https://pixabay.com/photos/)

### Reference Material
---
* W3 Schools was used as a reference point for HTML, CSS and JavaScript.

### Acknowledgements
---
* I'd like to thank the following:
- Matt Bodden, for the significant ideas for my project - your guidance truly made a difference!
- Oliver Train, for all his help regarding his patience and pointing me in the right direction.
- Dario Carrasquel, for all his help during this project as my mentor.