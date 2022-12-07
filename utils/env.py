import os
from date import create_env

path = os.getcwd()
if os.path.exists(path+'"\ \"'.replace(" ", "").replace('"', '')+".env"):
    print(create_env["env_failed"])
else:
    env = open(".env", "w")
    env.write(
        "FLASK_DEBUG=development \n DATABASE_URL=mysql+pymysql://user:password@localhost:3306/db_name \n DB_NAME=db_name \n SECRET_KEY=secretkey",
    )
    print(create_env["env_success"])