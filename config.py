"""
Configuration file for flask sample application
"""
import os

# enable CSRF
WTF_CSRF_ENABLED = True

# secret key for authentication
SECRET_KEY = 'secret_key_2'

# CONSUMER_KEY_PEM_FILE = os.path.abspath('consumer_key.pem')
# with open(CONSUMER_KEY_PEM_FILE, 'w') as wfile:
#     wfile.write(os.environ.get('CONSUMER_KEY_CERT', ''))

# Specify your tool's consumer_key and secret_key combination here
PYLTI_CONFIG = {
    "consumers": {
        "consumer_key_2": {
            "secret": 'secret_key_2',
            # "cert": CONSUMER_KEY_PEM_FILE
        }
    }
}

# # Remap URL to fix edX's misrepresentation of https protocol.
# # You can add another dict entry if you have trouble with the
# # PyLti URL.
# PYLTI_URL_FIX = {
#     "https://localhost:8000/": {
#         "https://localhost:8000/": "http://localhost:8000/"
#     },
#     "https://localhost/": {
#         "https://localhost/": "http://192.168.33.10/"
#     }
# }
