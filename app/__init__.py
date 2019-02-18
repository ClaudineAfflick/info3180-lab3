from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '8d90b3065fda6c334a382c637c6ad189'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' # (or try 2525)
app.config['MAIL_USERNAME'] = '1c589a197b8864'
app.config['MAIL_PASSWORD'] = '1ff0f158179cbe'
mail = Mail(app)
from app import views