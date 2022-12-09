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
            "env_success": "SUCCESS: added the .env file",
            "env_failed": "SUCCESS: the .env file exists, the file was not modified",
            "env_failed_unexpected":"ERROR: unexpected error"
        }
    },
    "content":{
        "create_env": "\n# Your environment variables will go here, to use them import the 'os' module and use it as an example: os.getenv('NAME') \n \nFLASK_DEBUG=development \n \nDATABASE_URL=mysql+pymysql://user:password@localhost:3306/db_name \n \nDB_NAME=db_name \n \nSECRET_KEY=secretkey"
    }
}