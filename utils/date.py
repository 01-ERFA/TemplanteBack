scripts = {
    "messages": {
        "script_help": "scripts for the template, see the documentation on the template.",
        "create_env" : {
            "create": "you don't have the .env file yet, create it with 'pipenv run create_env'",
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
            "env_failed_unexpected": "ERROR: unexpected error"
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
        },
        "db":{
            "db_reset": {
                "success": "SUCCESS: database restarted successfully",
            }, 
            "db_create": {
                "success": "database created successfully",
                "failed": "could not create database"
            },
            "db_drop": {
                "success": "database deleted successfully",
                "failed": "could not drop database"
            },
            "others": {
                "not_migrations_file": "Error: no migrations exist, command could not be executed",
                "drop_suggest": "If you want to delete a database run: 'pipenv run db_drop'",
                "create_suggest": "If you want to create a database run: 'pipenv run db_create'",
                "start_migrations": "if you want to start the migrations: 'pipenv run init'",
                "engine_failed": "Error: Failed to create the engine to interact with the database, check in the .env file: 'DATABASE_URL' and 'DB_NAME'",
                "remove_migrations_success": "removed migrations successfully",
                "remove_migrations_failed": "could not remove migrations",
                "reset_migrations_success": "restarted migrations successfully",
                "reset_migrations_failed": "failed to restart migrations"
            }
        }
    },
    "content":{
        "create_env": {
            "comment": "\n# Your environment variables will go here, to use them import the 'os' module and use it as an example: os.getenv('NAME') \n ",
            "developing": "\nFLASK_DEBUG=development \n \nFLASK_APP=app.py \n ",
            "database_url_start": "\nDATABASE_URL=mysql+pymysql://",
            "database_url_end":"@localhost:3306/",
            "database_name": "\nDB_NAME=",
            "secret_key": "\nSECRET_KEY=",
            "line_separator": " \n ",
        }
    },
    "commands": {
        "commands_developing": {
            "flask_init": "flask --debug db init",
            "flask_migrate": "flask --debug db migrate",
            "flask_upgrade": "flask --debug db upgrade"
        },
        "commands_db": {
            "drop_start": "DROP DATABASE ",
            "create_start": "CREATE DATABASE ",
            "reset": "pipenv run init && pipenv run migrate && pipenv run upgrade",
            "semicolon": ";",
            "others":{
                "reset_migrations": {
                    "init": "pipenv run init",
                    "migrate": "pipenv run migrate",
                    "upgrade": "pipenv run upgrade"
                }
            }
        }
    },
    "aux_symbols":{
        "line_separator": " \n",
        "semicolon": ";"
    }
}