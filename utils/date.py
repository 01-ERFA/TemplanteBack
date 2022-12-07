import os

create_env = {
    "env_success": "Created .env file",
    "env_failed": "The .env exist"
}

db_reset = {
    "command": {
        "drop": "DROP DATABASE "+ os.getenv("DB_NAME") + ";",
        "create": "CREATE DATABASE " + os.getenv("DB_NAME") + ";",
        "reset": "pipenv run init && pipenv run migrate && pipenv run upgrade"
    },
    "messages": {
        "success": "db reset success",
        "failed": "Error: use 'pipenv run init' to start db",
        "failed_except": "Error: could not restart base, check DB_NAME name in .env"
    }

}
