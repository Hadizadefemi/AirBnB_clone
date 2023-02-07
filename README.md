# Airbnb clone
This project is a task from ALX Schools which goal is to deploy on our server a simple copy of the AirBnB website.
<br>

### A complete web application composed by:

* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and
debugging)

* A website (the front-end) that shows the final product to everybody: static and dynamic

* A database or files that store data (data = objects)

* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)
<br>


## Description

### Steps taken to build the web application

#### The console

* create our data model

* manage (create, update, destroy, etc) objects via a console / command interpreter

* store and persist objects to a file (JSON file)


The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My
object” and “How they are stored and persisted”. This means: from our console code (the command interpreter itself) and
from the front-end and RestAPI, we won't have to pay attention (take care) of how our objects are
stored.

This abstraction will also allow us to change the type of storage easily without updating all of our codebase.

The console will be a tool to validate this storage engine
