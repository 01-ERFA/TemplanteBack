import os
from date import path,create_env

if os.path.exists(path+".env"):
    print(create_env["env_failed"])
else:
    env = open(".env", "w")
    env.write(
        "\n# Your environment variables will go here, to use them import the 'os' module and use it as an example: os.getenv('NAME') \n \nFLASK_DEBUG=development \n \nDATABASE_URL=mysql+pymysql://user:password@localhost:3306/db_name \n \nDB_NAME=db_name \n \nSECRET_KEY=secretkey",
    )
    print(create_env["env_success"])