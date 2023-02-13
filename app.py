from flask import Flask
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/views")

if __name__ == '__main__':
    app.run(debug=True, port=8000)

# if __name__ == '__main__':
#     app.run(port=8080, host='0.0.0.0')