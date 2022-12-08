#About the REST API template

- Clone repository

###- Important! Do not move terminal path!
*The terminal path should always be where the project is hosted*

- ####Project dependencies
	- python 3.10
	- pipenv

- ####Command of init
$`pipenv install && pipenv shell`

- ####Command to create the .env file
$`pipenv run env`

- ##Connect your database in the .env file

- ####Command to start the database tables
$`pipenv run init && pipenv run migrate && pipenv run upgrade`

- ####Command to start the rest api
$`pipenv run start`

- ##IMPORTANT!
	- #####Every time the "models" are modified, execute this command
	$`pipenv run migrate && pipenv run upgrade`

<hr>
######To learn more about this template, start the project and read the documentation that is in the project!
<hr>
######- Created by 01-ERFA

