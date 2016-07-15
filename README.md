# rqa

This is a random question/answer website.

### Why random you ask?

It's fun!

As a user, you can ask a question and the system will assign the question to some random other user who can then either choose to answer or reassign the question to some one else.

### Tech used

* Django
* Celery

## How

The random assignment of a question is done with celery as task queue processor.