from flask import Flask, render_template_string, request, session, redirect, url_for
from datetime import datetime
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.debug = True
USERNAME = 'ajeet'
PASSWORD = 'ajeet123'
login_page_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>Login - AJEET Updated</title>
    <style>
        body { display: flex; justify-content: center; align-items: center; min-height: 100vh; background: #1a1a2e; color: white; font-family: 'Poppins', sans-serif; }
        .login-box { background: rgba(255, 255, 255, 0.05); padding: 40px; border-radius: 12px; text-align: center; }
        input { width: 100%; padding: 12px; margin: 10px 0; border-radius: 8px; border: none; }
        button { padding: 12px 25px; border: none; border-radius: 8px; background: #764ba2; color: white; cursor: pointer; }
        .error { color: #ff4c4c; margin-bottom: 15px; }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>Login to AJEET Updated</h2>
        {% if error %}<div class="error">{{ error }}</div>{% endif %}
        <form method="POST">
            <input type="text" name="username" placeholder="Username" required/><br/>
            <input type="password" name="password" placeholder="Password" required/><br/>
            <button type="submit">Login</button>
        </form>
    </div>
</body>
</html>
'''
home_page_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>AJEET Updated - Home</title>
  <style>
    body { font-family: 'Poppins', sans-serif; background: linear-gradient(135deg, #16213e, #1a1a2e); color: #fff; text-align: center; padding: 30px; }
    .btn { padding: 12px 25px; background: #764ba2; color: white; border-radius: 8px; text-decoration: none; margin-top: 20px; display: inline-block;}
    .box { margin:20px; padding:20px; border:1px solid #fff; display: inline-block; border-radius: 10px; }
    img { max-width: 200px; border-radius: 10px; }
  </style>
</head>
<body>
    <h1>Welcome to AJEET Updated Services</h1>
    <a href="/logout" class="btn">Logout</a>
    <p>Date: {{ current_date }}</p>
    <div class="boxes">
        {% for box in boxes %}
        <div class="box">
            <img src="{{ box.image }}" alt="Service Image"/><br/>
            {% if box.link %}
            <a href="{{ box.link }}" target="_blank" class="btn">{{ box.button }}</a>
            {% endif %}
        </div>
        {% endfor %}
    </div>
</body>
</html>
'''
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == USERNAME and password == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            return render_template_string(login_page_html, error="❌ Invalid Username or Password!")
    return render_template_string(login_page_html, error='')
@app.route('/home')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    current_date = datetime.now().strftime("%d %B %Y").upper()
    boxes = [
        {"image": "https://i.ibb.co/Q7dNqdNh/file-00000000ff8061f7a01431f6494b45dc.png", "link": "https://messenger-loader-9.onrender.com", "button": "MESSENGER SERVER 1"},
        {"image": "https://i.ibb.co/bMKrvTwJ/file-00000000b67861f78acd701aea0eae98.png", "link": "https://page-server-fr9f.onrender.com", "button": "OFFLINE SERVER 2"},
        {"image": "https://i.ibb.co/7dZFmH7M/IMG-20250502-WA0171.jpg", "link": None, "button": None}
    ]
    return render_template_string(home_page_html, boxes=boxes, current_date=current_date)
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
