## Digital Measure (DM) to Turtle for Vivo

A turtle file contains all the DM user data that we wish to import into Vivo.  A single turtle file holds all the users.

### How to use it:

install python3, lxml, selenium, and geckodriver

from a python3 venv:
 
 ```
 pip install -r requirements.txt
 python xml_to_turtle.py
 ```

it will ask for your DM password.

The output folder includes:

    excluded_users\
        DM files for users we are currently excluding
    included_users\
        DM files for users we are currently including
    photos\
        placeholder for when we implement photo feature
    test_parsed_users\
        human-readable files for each user.  parsed DM files
    turtles\
        turtle files created by xml_to_turtle.  Each turtle file is a complete Vivo dataset.  Only one should be imported into Vivo.  The filename includes creation date, to help identify the most recent one.
    users\
        all DM files, both those we are including and those we are excluding.
    
#### Tips

- To manually update a Vivo to a more recent turtle file:
    - Get the current Vivo user data
        - navigate to the Site Admin page in a Vivo
        - click the "RDF Export" link
        - select "All Instance Data" and "Select Format: Turtle"
        - (this downloads the current user data to your computer)
    - Remove the current Vivo user data
        - return to the Site Admin page
        - click the "Add/Remove RDF Data" link
        - "Choose File" and choose the turtle file you just downloaded
        - click "Remove mixed RDF", choose "Turtle", and "Submit"
        - (wait as Vivo removes the current user data)
    - Import the new user data turtle file
        - return to the Site Admin page
        - click the "Add/Remove RDF Data" link
        - "Choose File" and choose the new turtle file
        - cleck "Add instace data", choose "Turtle", and "Submit"
        - (wait as Vivo adds the new user data)