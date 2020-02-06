from flask import Flask
import logging

from controllers import trending


application = Flask(__name__)
application.logger.handlers = []
application.logger.addHandler(logging.StreamHandler())

modules = [trending]
for module in modules:
    application.register_blueprint(module.routes)


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8888, debug=True, threaded=True)
