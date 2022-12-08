<h1>About the REST API template</h1>

- Clone repository

<h2>Important! Do not move terminal path!</h2>

*The terminal path should always be where the project is hosted*

- <h3>Project dependencies</h3>

	- python 3.10

	- pipenv

<h3>Command of init</h3>

	pipenv install && pipenv shell

<h3>Command to create the .env file</h3>

	pipenv run env

<h3>Connect your database in the .env file</h3>

<h3>Command to start the database tables</h3>

	pipenv run init && pipenv run migrate && pipenv run upgrade

<h3>Command to start the rest api</h3>

	pipenv run start

<h2>IMPORTANT!</h2>
	<h4>Every time the "models" are modified, execute this command</h4>
	
	pipenv run migrate && pipenv run upgrade


*To learn more about this template, start the project and read the documentation that is in the project!*

-	Created by 01-ERFA

