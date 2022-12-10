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
    }
}