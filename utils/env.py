import os
from date import path,create_env

if os.path.exists(path+".env"):
    print(create_env["env_failed"])
else:
    env = open(".env", "w")
    env.write(
        "FLASK_DEBUG=development \nDATABASE_URL=mysql+pymysql://user:password@localhost:3306/db_name \nDB_NAME=db_name \nSECRET_KEY=secretkey",
    )
    print(create_env["env_success"])