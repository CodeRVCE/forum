
import MySQLdb

db = MySQLdb.connect(host='localhost',
                     user='root',
                     passwd='root',
                     db='forum') 


def add_question(title, desc, asker):
    cursor = db.cursor()
    cursor.execute('insert into questions (title, description, asker) values ("%s", "%s", "%s")' % (title, desc, asker))
    db.commit()

def getall_qs():
    cursor = db.cursor()
    cursor.execute('select * from questions')
    questions = [question for question in cursor]
    return questions

def add_answer(qid, answer, answerer):
    cursor = db.cursor()
    cursor.execute('insert into answers values (%s, "%s", "%s")' % (qid, answer, answerer))
    db.commit()

def get_answers(qid):
    cursor = db.cursor()
    cursor.execute('select * from answers where qid=%s' % qid)
    questions = [question for question in cursor]
    return questions

#TODO: optimize
def get_num_ans(qid):
    return len(get_answers(qid))

def get_question(qid):
    cursor = db.cursor()
    cursor.execute('select * from questions where id="%s"' % qid)
    return cursor.fetchone()
    

if __name__ == '__main__':
    cursor = db.cursor()
    cursor.execute('')
    # create tables



