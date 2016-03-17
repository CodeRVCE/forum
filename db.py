"""

"""

import MySQLdb
from werkzeug.local import Local


class BoardDB:
    """
    BoardDB is the model for the question board. A BoardDB object
    provides API for accessing the question board and internally
    maps those updates to a mysql database.
    """

    # Thread-local Storage
    local = Local()

    def setup(self):
        self.connect()

    def teardown(self):
        # conn is weak-reference to the connection object. The object may
        # itself have been GC'ed away. Hence, in case of exception, just pass.
        try:
            BoardDB.local.conn.close()
        except:
            pass

    def connect(self):
        BoardDB.local.conn = MySQLdb.connect(host='localhost', user='root',
                                             passwd='root', db='forum')

    def execute_query(self, query, param=None):
        try:
            cursor = BoardDB.local.conn.cursor()
            cursor.execute(query, param)
        except (AttributeError, MySQLdb.OperationalError):
            self.connect()
            cursor = BoardDB.local.conn.cursor()
            cursor.execute(query, param)
        BoardDB.local.conn.commit()
        return cursor

    def create_tables(self):
        create_questions_query = """create table questions
                                        (id bigint not null auto_increment
                                                            primary key,
                                         title varchar(200) not null,
                                         description varchar(10000) not null,
                                         asker varchar(100) not null)"""
        create_answers_query = """create table answers
                                        (qid bigint unsigned,
                                        answer varchar(10000),
                                        answerer varchar(100))"""
        self.execute_query(create_questions_query)
        self.execute_query(create_answers_query)

    def add_question(self, title, desc, asker):
        query = """insert into questions (title, description, asker)
                   values (%s, %s, %s)"""
        self.execute_query(query, (title, desc, asker))

    def getall_qs(self):
        query = 'select * from questions order by id desc'
        cursor = self.execute_query(query)
        questions = [question for question in cursor]
        return questions

    def add_answer(self, qid, answer, answerer):
        query = """insert into answers values
                        (%s, %s, %s)"""
        self.execute_query(query, (qid, answer, answerer))

    def get_answers(self, qid):
        query = 'select * from answers where qid=%s'
        cursor = self.execute_query(query, [qid])
        questions = [question for question in cursor]
        return questions

    # TODO: optimize
    def get_num_ans(self, qid):
        return len(self.get_answers(qid))

    def get_question(self, qid):
        query = 'select * from questions where id=%s'
        cursor = self.execute_query(query, [qid])
        return cursor.fetchone()


boardDB = BoardDB()

if __name__ == '__main__':
    boardDB.create_tables()
