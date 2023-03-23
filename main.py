from flask import Flask
from controllers.marker_controller import marker_controller

app = Flask(__name__)
app.register_blueprint(marker_controller)

if __name__ == '__main__':
    app.run(debug=True)
