# DC-Killer
Get notifications every day your favorite food appears in the dining hall!

#### Problem
The food served at the Haverford Dining Center (The DC) changes every day based on a rotating biweekly schedule. Some days
are bad and some days are really good. A problem my friends and I keep having is that sometimes we 
eat out on good days when our favorite food (chicken tenders) are being served in the dining hall. A solution to this 
problem is a program that notified us every day whether our favorite food is being served in the dining hall.

#### Implementation
The program will be a web app that runs every day at a specified time. The app downloads and scans the DC menu and
converts the data to a form that's easy to manipulate. The information that would be nice to have is the items
being served each meal, the meal times which are variable, and dietary information for each food. There needs to 
be a front end for the use to interact with the program and select foods. There needs to be a notification system which at
first will be a text message alert of all the user's favorite foods that are being served that day. If nothing the user likes
is being served then maybe it will send a joke, a cute message, or a recipe to suggest something the user hasn't tried. Twilio
will be used to send the SMS message.

#### Organization
In each file below there is a 'TODO' statement at the top. That, along with the number next to it
states what needs to get done. The number indicates priority with 3 being highest priority.

web_scraper.py  - Handles retrieving the menu every day and sending the notification. The main file to run.
web_frontend.py - Handles everything the user sees.
SMS_backend.py  - Handles all methods associated with notifying the user through Twilio.
bottle.py       - Web framework for Python (Similar to Flask)
social.py       - (Planned) Handles all social features. Social creates user stickiness meaning it's there to encourage
                  users to keep using the application.
                  

#### Dependencies
Python 2.7
Bottle (version not clear yet)

#### Potential for Improvement
The ability to like or favorite foods
Facebook integration
The ability to suggest foods your friends like or favorite
A menu interface that can show the menu being served along with other info like:
  Dietary info (Vegan, Vegetarian, Gluten Free, Halal, Kosher)
  Nutritional info (Calorie Count, Ingredients)

  
