from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
from database import *
app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['UPLOAD_FOLDER'] = 'static/uploads'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_data():
    if 'isauth' not in session:
        flash('You need to login to access this page', 'danger')
        return redirect(url_for('login'))
    if request.method == 'POST':
        file = request.files['file']
        if file:
            try:
                filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(filename)
                dataset = Dataset(name=file.filename, path=filename)
                save_to_db(dataset)
                flash('File uploaded successfully', 'success')
                return redirect(url_for('index'))
            except Exception as e:
                flash(f'An error occured {e}', 'danger')
                return redirect(url_for('upload_data'))
    return render_template('upload.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password = request.form['cpassword']
        email = request.form['email']
        if not username or not password or not email:
            flash('Please fill out the form', 'danger')
            return redirect(url_for('register'))
        try:
            user = User(username=username, password=password, email=email)
            save_to_db(user)
            flash('User registered successfully', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'An error occured {e}', 'danger')
            return redirect(url_for('register'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not username or not password:
            flash('Please fill out the form', 'danger')
            return redirect(url_for('login'))
        db = get_db()
        user = db.query(User).filter_by(username=username, password=password).first()
        if user:
            session['user'] = user.username
            session['user_id'] = user.id
            session['isauth'] = True
            session['email'] = user.email
            flash('User logged in successfully', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('User logged out successfully', 'success')
    return redirect(url_for('index'))

@app.route('/results', methods=['GET', 'POST'])
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 