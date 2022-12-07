import os, shutil
from subprocess import check_output
from utils import engine
from date import db_reset


path = os.getcwd()
if os.path.exists(path+'"\ \"'.replace(" ", "").replace('"', '')+"migrations"):
    try:
        shutil.rmtree(path+'"\ \"'.replace(" ", "").replace('"', '')+"migrations")
        engine.execute(db_reset["command"]["drop"])
        engine.execute(db_reset["command"]["create"])
        check_output(db_reset["command"]["reset"], shell=True)
        print(db_reset["messages"]["success"])
    except:
        print(db_reset["messages"]["failed_except"])
else:
    print(db_reset["messages"]["failed"])



