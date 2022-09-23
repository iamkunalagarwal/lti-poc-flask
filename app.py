from flask import Flask
from pylti.flask import lti
from flask import request as flask_request

VERSION = '0.0.1'
app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def hello_world():
    print("Home page loaded.")
    return 'Welcome to Home page!'


def error(exception=None):
    """ render error page
    :param exception: optional exception
    :return: the error.html template rendered
    """
    return "Error in LTI connection. \n {}".format(str(exception))


@app.route('/lti/', methods=['GET', 'POST'])
@lti(request='initial', error=error, app=app)
def index(lti=lti):
    """ initial access page to the lti provider.  This page provides
    authorization for the user.
    :param lti: the `lti` object from `pylti`
    :return: index page for lti provider
    """

    # Access the payload to LTI post request
    print('LTI initial page loaded.')
    print(lti)
    print(type(lti))
    print(flask_request.method)
    params = flask_request.form.to_dict()
    print("params: {}".format(params))

    # User's name
    name = params['lis_person_name_full']
    print(f'{name=}')

    # Custom parameters
    print("custom_field_name_01: {}".format(params['custom_field_name_01']))
    # print("custom_field_name_02: {}".format(params['custom_field_name_02']))

    return "Hello {}! I'm LTI tool called from Canvas.".format(params['lis_person_name_full'])


# main driver function
if __name__ == '__main__':
    app.run()
