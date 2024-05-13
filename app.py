from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
from database import *
app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
from graphs_api import *

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

@app.route('/signup', methods=['GET', 'POST'])
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
    df = load_data('static/dataset.csv')
    fig1 = viz_employee_attrition(df, graph='pie')
    fig2 = viz_department(df, graph='funnel')
    fig3 = viz_travel(df, graph='pie')
    fig4 = viz_education_field(df, graph='violin')
    fig5 = viz_job_role(df, graph='box', color='MaritalStatus')
    fig6 = viz_job_satisfaction(df, graph='bar')
    
    return render_template('results.html', 
        fig1=fig1.to_html(), 
        fig2=fig2.to_html(),
        fig3=fig3.to_html(),
        fig4=fig4.to_html(),
        fig5=fig5.to_html(),
        fig6=fig6.to_html(),
        
    )

@app.route('/results/2', methods=['GET', 'POST'])
def results_2():
    df = load_data('static/dataset.csv')
    fig7 = viz_job_level(df, graph='bar')
    fig8 = viz_job_involvement(df, graph='bar')
    fig9 = viz_performance_rating(df, graph='bar')
    fig10 = viz_relationship_satisfaction(df, graph='bar')
    fig11 = viz_work_life_balance(df, graph='bar')
    fig12 = viz_environment_satisfaction(df, graph='bar')

    return render_template('results_2.html', 
        fig7=fig7.to_html(),
        fig8=fig8.to_html(),
        fig9=fig9.to_html(),
        fig10=fig10.to_html(),
        fig11=fig11.to_html(),
        fig12=fig12.to_html(),
    )
@app.route('/results/3', methods=['GET', 'POST'])
def results_3():
    df = load_data('static/dataset.csv')
    fig13 = viz_employee_distribution(df, graph='box')
    fig14 = viz_employee_income(df, graph='box')
    fig15 = viz_income(df, graph='strip')
    fig16 = viz_sunburst(df, path=['Department', 'JobRole','Attrition'], values='MonthlyIncome')
    fig17 = viz_employee_scatter(df, x='Age', y='MonthlyIncome', color='Attrition', size='TotalWorkingYears')
    
    
    return render_template('results_3.html', 
        fig13=fig13.to_html(),
        fig14=fig14.to_html(),
        fig15=fig15.to_html(),
        fig16=fig16.to_html(),
        fig17=fig17.to_html(),    
    )
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 