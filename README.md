# Hierarchical data example

A simple project to show how the Hierarchical data structure can work using gundam version models to show the different levels of the data tree. can be extended

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

must clone this project first using
```
git clone git@github.com:kbrooks87/hierarchical_data.git
```

What things you need to install the software and how to install them

```
Must have poetry installed to use
```

### Installing

A step by step series of examples that tell you how to get a development env running

installing through poetry you must open the folder the project is located in through the terminal then use

```
poetry install
```

And that will install all packages needed to run the project. then run

```
python manage.py createsuperuser
```

this allows you to create your sign in. Next run

```
python manage.py runserver
```

This starts the server for you. just navigate to 127.0.0.1:8000/admin to sign in

## Authors

* **Kelly Brooks**


## Acknowledgments

* Hat tip to anyone whose code was used - Joe(instructor at Kenzie Academy) whose demo video helped me keep on point with what i needed to look for and Detrich(SE Tutor at Kenzie Academy) who helped me figure out why my self in the model was throwing a fit.
