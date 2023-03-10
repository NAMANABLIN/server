from data import db_session
from data.Users import User
from data.Jobs import Job
import datetime
db_session.global_init('mars_explorer.db')
db_sess = db_session.create_session()

job = Job()
job.team_leader = 1
job.job = 'deployment of residential modules 1 and 2'
job.work_size = 15
job.collaborators = '2, 3'
job.is_finished = False
job.created_date = datetime.datetime.now()
db_sess.add(job)
db_sess.commit()