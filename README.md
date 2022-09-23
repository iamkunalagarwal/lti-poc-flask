# lti-poc-flask
This is a POC of LTI integrated inside Canvas LMS, using Flask and pylti.


## Setup
Step 1: Canvas -> Courses -> Settings -> Apps -> View App Configuration -> + Add

Step 2: Configure using XML pasted from https://canvas.instructure.com/doc/api/file.tools_xml.html

Step 3: Assign your CONSUMER_KEY and SECRET_KEY for Oauth.

Step 4: Set up LTI local on your localhost, update keys and run app.py

Step 5: Create module with external tool we created in the canvas course.


## Useful links:
- https://pylti.readthedocs.io/en/master/index.html
- https://canvas.instructure.com/doc/api/file.tools_xml.html
- https://github.com/mitodl/mit_lti_flask_sample
- https://colostate-dev.instructure.com/courses/140/modules
