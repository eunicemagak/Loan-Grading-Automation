
import os
import mysql.connector
from dotenv import load_dotenv
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
load_dotenv()

dbconn = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_DATABASE'))

cur =dbconn.cursor()

cur.execute('''delete from _tmp_latest_loan''')
cur.execute('''insert into _tmp_latest_loan
SELECT * FROM azima.v_users_latest_loan
where curdate() >= date_add(date(pay_date), interval 3 day)and repayment_status = 'PAID' ''')

logging.info('updated latest loans')