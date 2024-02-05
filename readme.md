# Create an Environment in Windows
For Python 3:
Create and name a virtual environment in Python 3 with:

py -3 -m venv <name of environment>

Activate the Environment on Windows
For Windows, activate the virtual environment with:

<name of environment>\Scripts\activate

venv\Scripts\activate

Set the FLASK_APP environment variable.
setx FLASK_APP "hello.py"

Run the Flask application with:
flask run

debug mode
python hello.py

https://phoenixnap.com/kb/install-flask

https://pythonbasics.org/flask-sqlalchemy/
https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application

The special __repr__ function allows you to give each object a string representation to recognize it for debugging purposes. In this case you use the student’s first name.

Creating the Database
Now that you’ve set the database connection and the student model, you’ll use the Flask shell to create your database and your student table based on the Student model.

With your virtual environment activated, set the app.py file as your Flask application using the FLASK_APP environment variable. Then open the Flask shell using the following command in your flask_app directory:

(venv) PS D:\dj\flask\demo_app> export FLASK_APP=app  /  setx FLASK_APP "hello.py"
(venv) PS D:\dj\flask\demo_app> flask shell

A Python interactive shell will be opened. This special shell runs commands in the context of your Flask application, so that the Flask-SQLAlchemy functions you’ll call are connected to your application.

Import the database object and the student model, and then run the db.create_all() function to create the tables that are associated with your models. In this case you only have one model, which means that the function call will only create one table in your database:

from app import db, Student
db.create_all()
Leave the shell running, open another terminal window and navigate to your flask_app directory. You will now see a new file called database.db in flask_app.

Note:

The db.create_all() function does not recreate or update a table if it already exists. For example, if you modify your model by adding a new column, and run the db.create_all() function, the change you make to the model will not be applied to the table if the table already exists in the database. The solution is to delete all existing database tables with the db.drop_all() function and then recreate them with the db.create_all() function like so:

db.drop_all()
db.create_all()

https://stackoverflow.com/questions/73961938/flask-sqlalchemy-db-create-all-raises-runtimeerror-working-outside-of-applicat

As of Flask-SQLAlchemy 3.0, all access to db.engine (and db.session) requires an active Flask application context. db.create_all uses db.engine, so it requires an app context.

with app.app_context():
    db.create_all()
When Flask handles requests or runs CLI commands, a context is automatically pushed. You only need to push one manually outside of those situations, such as while setting up the app.

Instead of calling create_all in your code, you can also call it manually in the shell. Use flask shell to start a Python shell that already has an app context and the db object imported.

$ flask shell
>>> db.create_all()
Or push a context manually if using a plain python shell.

$ python
>>> from project import app, db
>>> app.app_context().push()
>>> db.create_all()