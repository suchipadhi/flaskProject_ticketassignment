# Getting Started with Python app for ticket assignment.

To get started, we'll build a Python-flask app which helps in assigning tickets to agents in a customer care center.


## Prerequisites

You'll need the following:
* [SQLite]
* [Flask]
* [Python]

## Possible objectives

In order to avoid data complexity and data management a better assignment process or algorithm is needed for a company.

The better the solution is better is the automized process and less effort involved for its maintainance.


## 1. Clone the sample app

you can clone the project from [Git repo].
   ```

  ```

## 2. Run the app locally

First, you have to install the dependencies listed in the [requirements.txt]to run it locally.

I prefer using a virtual environment [virtual environment] to avoid my dependencies clash with those of my other Python projects.
  ```
pip install -r requirements.txt
  ```

Run the app.
  ```
python run.py
  ```

 View your app at:
  ``` 
http://127.0.0.1:5000/assignment_tasktoagent
  ```

## 3. List of routes mentioned in the app

Below i have mentioned the list of routes used in the app:
* [http://127.0.0.1:5000/assignment_tasktoagent](as the name suggests we can view the final result in this route)
* [http://127.0.0.1:5000/create_task]( it creates a table and display the message to the user as "Task created from a user request.")
* [http://127.0.0.1:5000/displaycreated_task](it shows the initial task created in the system)


## 4. Add a database

Next, we'll add SQLite database for the data. I choose this as it is integrated in pycharm and easy to handle local database. And now the data provided is of less complexity.

## 6. Use the database

Below are teh listed tables where we can refer to find the task details and agent details. dbname - identifier.sqlite.db

* [agent]
* [agent_names]
* [language]
* [task_source]
* [user]

## Scalability of the solution

maintainability and scalability of an app can be increased by using database normalisation and avoiding concurrency problems by optiomised design of the database.