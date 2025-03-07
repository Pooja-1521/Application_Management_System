from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="mydbapp1.cwh6k06kydx8.us-east-1.rds.amazonaws.com",
    user="admin",
    password= "pooja123#",
    database= "temp"
)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phoneno = request.form.get('phoneno')
        linkedin = request.form.get('linkedin')
        github = request.form.get('github')
        resume = request.form.get('resume')


        cursor = db.cursor()
        sql = "INSERT INTO users (name, email, phoneno, linkedin, github, resume) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (name, email, phoneno, linkedin, github, resume))
        db.commit()
        cursor.close()

        return redirect(url_for('verify'))  # Redirect to view page after submission
@app.route('/success')
def verify():
    return render_template("success.html")


@app.route('/view')
def view_data():
    cursor = db.cursor(dictionary=True)  # Use dictionary=True to fetch column names
    cursor.execute("SELECT * FROM users")  # Replace with your table name
    data = cursor.fetchall()
    cursor.close()
    
    return render_template("view.html", data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



