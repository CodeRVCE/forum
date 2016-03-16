
## The Architecture of Forum

### The Underlying Models

* QuestionPool
Contains a pool of questions.

* Question
Each question contains:
    * Title
    * Description
    * Asker id
    * Timestamp
    * Votes
    * A list of answers corresponding to that question.

* Answer
Each answer contains:
    * Answerer id
    * Answer statement
    * Timestamp
    * Votes

* Users
A pool of users.

* User
Each user contains:
    * Handle (primary key)
    * Account Type
    * Email ID
    * Password (hashed)
