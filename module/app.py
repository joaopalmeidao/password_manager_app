from flask import Flask,render_template,url_for,redirect,request,flash,send_file
from extensions import db,login_manager
from models import PasswordManager,User
from flask_login import login_required,current_user
import pandas as pd
from datetime import datetime
import os
from module import PATH_DIRETORIO,PATH_ARQUIVOS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SECRET_KEY'] = 'HDIUH89adh9HSadjkbdjsa98dna9u'


db.init_app(app)


with app.app_context():
    db.create_all()
    
    # USERS = [
    #     PasswordManager(email='admin@jpsoftwaresco.com.br',site_url='www.jpsoftwaresco.com.br',site_password='admin'),
    #     PasswordManager(email='guest@jpsoftwaresco.com.br',site_url='www.jpsoftwaresco.com.br',site_password='guest')
    # ]
    # for U in USERS:
    #     db.session.add(U)
    # db.session.commit()
    
    # users = User.query.all()
    # print(users)

# For managing sessions during login
login_manager.init_app(app)


from .auth import auth
app.register_blueprint(auth)


@login_manager.user_loader
def load_user(user_id):
    # using the user id as primary key as id for session
    return User.query.get(int(user_id))
    
@app.route("/")
def index():
    if not current_user.is_authenticated:
        return render_template("login.html")
    passwordlist = PasswordManager.query.all()
    return render_template('index.html', passwordlist=passwordlist)

@app.route("/home")
def home_page():
    passwordlist = PasswordManager.query.all()
    return render_template('home.html', passwordlist=passwordlist)    

@app.route("/add",methods=["GET","POST"])
@login_required
def add_password():
    if request.method == 'POST':
        email = request.form['email']
        site_url = request.form['site_url']
        site_password = request.form['site_password']
        new_password_details = PasswordManager(email=email,site_url=site_url,site_password=site_password)
        db.session.add(new_password_details)
        db.session.commit()
        flash("Password Added")
        return redirect('/')

@app.route('/delete/<int:id>')
@login_required
def delete(id):
    new_password_to_delete = PasswordManager.query.get_or_404(id)

    try:
        db.session.delete(new_password_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    task = PasswordManager.query.get_or_404(id)

    if request.method == 'POST':
        task.email = request.form['email']
        task.site_url = request.form['site_url']
        task.site_password = request.form['site_password']
        try:
            db.session.commit()
            flash("Password Updated")
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', task=task)


@app.route('/export')
@login_required
def export_data():
    timestr = datetime.today().strftime('%Y%m%d%H%M%S')
    consulta = PasswordManager.query.all()
    dados = list(item.__dict__ for item in consulta)
    
    df = pd.DataFrame(dados)
    
    file_name = f"Export_Password_{timestr}.xlsx"
    file_path = os.path.join(PATH_ARQUIVOS, file_name)
    
    df.to_excel(file_path,index=False)

    return send_file(file_path,
        mimetype='text/csv',
        download_name=file_name,
        as_attachment=True)

