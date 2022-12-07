from utils.config import app
# from utils.config import db, engine
from models.tasks import Task
from utils.session import session

if __name__ == '__main__':

    # db.metadata.drop_all(engine)
    # db.metadata.create_all(engine)

    task1 =  Task(
        title="hello workd",
        description="i am a test"
    )

    session.add(task1)
    session.commit()

    app.run(host="0.0.0.0", port=4000, debug=True)