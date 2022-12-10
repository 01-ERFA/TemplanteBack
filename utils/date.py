import os

path = os.getcwd()
path = path+'"\ \"'.replace(" ", "").replace('"', '')

db_name = os.getenv("DB_NAME") if os.getenv("DB_NAME") != None else ""


db_reset = {
    "command": {
        "drop": "DROP DATABASE "+ db_name + ";",
        "create": "CREATE DATABASE " + db_name + ";",
        "reset": "pipenv run init && pipenv run migrate && pipenv run upgrade"
    },
    "messages": {
        "success": "db reset success",
        "failed": "Error: use 'pipenv run init' to start db",
        "failed_except": "Error: could not restart base, check DB_NAME name in .env"
    }

}

scripts = {
    "messages": {
        "script_help": "scripts for the template, see the documentation on the template.",
        "create_env" : {
            "start_message": "the data entered will not be displayed on the screen",
            "user": "your user of your database: ",
            "pswd": "password: ",
            "db_name": "database name: ",
            "secret_key": "enter a new secret key: ",
            "env_success": "SUCCESS: added the .env file",
            "env_failed": "SUCCESS: the .env file exists, the file was not modified",
            "env_failed_unexpected":"ERROR: unexpected error"
        },
        "delete_env": {
            "env_success": "SUCCESS: deleted the .env file",
            "env_failed": "SUCCESS: the .env file does not exist, could not be deleted",
            "env_failed_unexpected":"ERROR: unexpected error"
        },
        "flask": {
            "init":{
                "flask_success": "SUCCESS: flask init success",
                "failed_exist": "ERROR: flask has already started",
                "failed_unexpected": "ERROR: unexpected error"
            },
            "migrate": {
                "flask_success": "SUCCESS: flask migrate success, run 'pipenv run upgrade' to upgrade your database",
            },
            "upgrade": {
                "flask_success": "SUCCESS: your database has been updated"
            }
        }
    },
    "content":{
        "create_env": {
            "comment": "\n# Your environment variables will go here, to use them import the 'os' module and use it as an example: os.getenv('NAME') \n ",
            "developing": "\nFLASK_DEBUG=development \n ",
            "database_url_start": "\nDATABASE_URL=mysql+pymysql://",
            "database_url_end":"@localhost:3306/",
            "database_name": "\nDB_NAME=",
            "secret_key": "\nSECRET_KEY=",
            "line_separator": " \n ",
        }
    },
    "commands_developing": {
        "flask_init": "flask --debug db init",
        "flask_migrate": "flask --debug db migrate",
        "flask_upgrade": "flask --debug db upgrade"
    }
}