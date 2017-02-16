

for the Mcq app type "127.0.0.1:8000/quiz/" for the home page

This app mainly consist of of two parts.

1->user registration for the quiz
2->admin provision for managing the questions

User Registration
-----------------

In user you need to input the username,email and password for the
registration purpose. Sumbit button will take you to the quiz page, there 
you can submit your answers. The submit button in the quiz page will take you to 
the score page.

Note:
	1. only one answer for each question.


Admin-page
----------
In the admin home page you can see questions as links.
Click a question and you can see the details of that particular question

In the admin page you can do three things

1. Add a question
2. See results in a table(the score for users who attempted the quiz)

When a question get clicked there will be three options

1.Edit
2.Delete->will take you to a confirmation page
3.Add a question


Models Used
-----------------------

Two models are used here

Question and Result

Question
---------
There are 6 fields in the Question section
question no,question text,then 5 options and a answer

Result
-------
Result consist of username,email and password


