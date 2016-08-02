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

## Installation steps

* `mkdir <root_folder>`
* `cd <root_folder>`
* `virtualenv venv -p python3`
* `. venv/bin/activate`
* `git clone https://github.com/harshad91/rqa.git`
* `cd rqa`
* `pip install -r requirements.txt`
* `python manage.py runserver`

### Celery worker process (in a new terminal window)

`python manage.py worker --loglevel=info`