import os

path = os.getcwd()

path = path+'"\ \"'.replace(" ", "").replace('"', '')

db_name = os.getenv("DB_NAME") if os.getenv("DB_NAME") != None else ""

create_env = {
    "env_success": "Created .env file",
    "env_failed": "The .env exist"
}

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
