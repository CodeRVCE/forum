
import MySQLdb

class BoardDB:

    def connect(self):
        self.conn = MySQLdb.connect(host='localhost', user='root',
                                    passwd='root', db='forum')
    
    def execute_query(self, query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
        except (AttributeError, MySQLdb.OperationalError):
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(query)
        self.conn.commit()
        return cursor
    
    def create_tables(self):
        create_questions_query = """create table questions 
                                        (id bigint not null auto_increment primary key,
                                         title varchar(200) not null,
                                         description varchar(1000) not null,
                                         asker varchar(100) not null)"""
        create_answers_query = """create table answers 
                                        (qid bigint unsigned, 
                                        answer varchar(1000), 
                                        answerer varchar(100))"""
        self.execute_query(create_questions_query)
        self.execute_query(create_answers_query)

    def add_question(self, title, desc, asker):
        query = """insert into questions (title, description, asker) 
                   values ("%s", "%s", "%s")""" % (title, desc, asker)
        cursor = self.execute_query(query)

    def getall_qs(self):
        query = 'select * from questions'
        cursor = self.execute_query(query)
        questions = [question for question in cursor]
        return questions

    def add_answer(self, qid, answer, answerer):
        query = 'insert into answers values (%s, "%s", "%s")' % (qid, answer, answerer)
        cursor = self.execute_query(query)

    def get_answers(self, qid):
        query = 'select * from answers where qid=%s' % qid
        cursor = self.execute_query(query)
        questions = [question for question in cursor]
        return questions

    #TODO: optimize
    def get_num_ans(self, qid):
        return len(self.get_answers(qid))

    def get_question(self, qid):
        query = 'select * from questions where id="%s"' % qid
        cursor = self.execute_query(query)
        return cursor.fetchone()


boardDB = BoardDB()

if __name__ == '__main__':
    boardDB.create_tables()


