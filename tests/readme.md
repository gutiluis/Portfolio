### how to run pytest:
```bash
pytest
python -m pytest
```

### place modules under root. add project root directory to python modules search
```bash
pip install -e .
PYTHONPATH=. pytest
python -m pytest
```

---
architecture:
test route:
call client
assert response
### do not push an application context globally for every test, as it can interfere with how the session is cleaned up

``` python
def test_user_model(app):
    user = User()
    with app.app_context(): # context should be before creating or
        db.session.add(user)
        db.session.commit()
```
---
### design of specific context objects:
flask.app.test_client() # client requests
flask.app.app_context() # not always used with current_app()
``` python
with app.app_context():
    db.create_all()
```
flask.app.test_request_context()
g
session # proxy lives within a pushed request context
### reference:
https://bluesmonk.301621.xyz/flask-contexts.html

---
### python contextvars support:
- asyn views/ await
- async frameworks
- context isolation
- contextvars.ContextVar
- threads
- event loops
- greenlets


### flask context variables:
manage context in asynchronous framework from python library
flask uses python conextvars libarary under the hood
https://docs.python.org/3/library/contextvars.html


### see pep 567 context variables
### contextvars.ContextVar
- It is not possible to get a direct reference to the current Context object. use contextvars.copy_context()
- a context is a mapping of contextvars objects to their values
https://peps.python.org/pep-0567/

### a route can have get or post and others...

# 3 main ways to test a flask route:
- AUTOMATICALLY FOLLOW HTTP REDIRECTS
- SUBMIT REAL DATA REQUESTS
- TEST TEMPLATE_RENDER LIBRARY
# automatically follow http redirects:
submit data and follow the redirect
response = client.get(follow_redirects=True)
the client will continue to make requests until a non-redirect response is returned.

# submit real data requests:
Check the data sent (simulate form POST)
state response = client.post(data=…) to simulate a user submitting a form.
testing html form handling, validation, and database changes.
check for submission
verify db changes

# test template_render:
You listen to the template_rendered signal and check the context variables.
Useful when you care about what data the template received, not the HTTP request/response itself.
check template context
doesn't check actual http form submission or redirects
---
each has api endpoint has different testing aproach:
project has:
edit form with
detail form with db.session
index form with db query.all()
new project form db.session
about form only render_template
