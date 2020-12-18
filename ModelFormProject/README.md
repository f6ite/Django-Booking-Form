Kai's Booking System

setup
    cd C:/user/booking/modelformproject

    docker-compose build
    docker-compose up

    http://127.0.0.1:8000

Edited files:

    modelformproject:
        dockerfile
        docker-compose
        requirements.txt
        readme.md
        inplementationlog.txt

    modelformproject/detailsapp:
        admin.py
        forms.py
        models.py
        urls.py
        views.py

    modelformproject/modelformproject:
        settings.py
        urls.py

    modelformproject/templates:
        detail.html
        display.html
        display0.html
        userdetails.html

Test Accounts http://127.0.0.1:8000/admin :

    Superuser:
        User: Admin
        Pass: Admin
    Brad (Pub owner):
        User: Brad
        Pass: PubOwner

Key Features:

Allows booking of tables in time slots of 30 minutes each, doesn't allow for overlap in tables, timeslots, and pubs (if userpub = existingpub and usertable = existingtable and usertimeslot = existingtimeslot and userday == existingday: print error)
Currently supports booking for 3 pubs but could be expanded to support more through simple changes to models.py (under PUBNAME_CHOICES)
UI is simple but easy to use, due to built in Django capabilities it should be useable on mobile

Clean-up:

Open the modelformproject directory and run the command - bash dockerclean.sh, this will cleanup the images and container related to the booking system

Testing:

I tested the program on several of my friend's systems and asked them to try and break the program by creating invalid inputs for each section.

In terms of validation the program performed as expected, with no one being able to input information that would be unexpected.

Scalability is limited by SQLite, but that shouldn't be an issue as realistically you're only allowing booking in a limited timeframe, if you were allowing people to book dates in advance rather than the next day then you'd possibly encounter an issue, but in it's current iteration that's not something that should happen.