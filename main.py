from flask import Flask, render_template_string, session
from datetime import datetime
import os
import random
import string
import requests

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.debug = True

# 🔐 Approval config
APPROVAL_URL = "https://raw.githubusercontent.com/TOKEN-CHAKER/approved.json/main/ap koproved.json"
OWNER_CONTACT = '6387071869'

# 🔑 Generate unique user key
def generate_user_key():
    parts = [''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) for _ in range(30)]
    return 'AJEET-UPDATED-' + '-'.join(parts)

# ✅ Check if key is approved
def is_key_approved(key):
    try:
        res = requests.get(APPROVAL_URL)
        if res.status_code == 200:
            approved = res.json().get("approved", [])
            return key in approved
    except Exception as e:
        print(f"[❌ ERROR] While checking approval: {e}")
    return False

# 🔐 Approval check before every request
@app.before_request
def approval_required():
    if 'approved' not in session:
        if 'user_key' not in session:
            session['user_key'] = generate_user_key()
        key = session['user_key']
        if is_key_approved(key):
            session['approved'] = True
        else:
            return render_template_string('''
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Waleed Updated - Approval Required</title>
                    <style>
                        body {
                            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
                            color: #fff;
                            text-align: center;
                            padding: 50px 20px;
                            margin: 0;
                        }
                        .container {
                            max-width: 700px;
                            margin: 0 auto;
                            background: rgba(255, 255, 255, 0.05);
                            backdrop-filter: blur(10px);
                            border-radius: 15px;
                            padding: 30px;
                            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
                            border: 1px solid rgba(255, 255, 255, 0.1);
                        }
                        h2 {
                            color: #e94560;
                            font-size: 28px;
                            margin-bottom: 20px;
                            text-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
                        }
                        p {
                            font-size: 16px;
                            margin-bottom: 20px;
                            color: #b8b8d1;
                        }
                        textarea {
                            width: 100%;
                            padding: 12px;
                            background: rgba(0, 0, 0, 0.2);
                            border: 1px solid #e94560;
                            border-radius: 8px;
                            color: #fff;
                            font-size: 14px;
                            margin-bottom: 20px;
                            resize: none;
                        }
                        .btn {
                            display: inline-block;
                            padding: 14px 30px;
                            background: linear-gradient(45deg, #e94560, #ff6b6b);
                            color: white;
                            text-decoration: none;
                            border-radius: 8px;
                            font-weight: bold;
                            font-size: 16px;
                            transition: all 0.3s ease;
                            box-shadow: 0 4px 15px rgba(233, 69, 96, 0.4);
                            border: none;
                            cursor: pointer;
                        }
                        .btn:hover {
                            transform: translateY(-3px);
                            box-shadow: 0 6px 20px rgba(233, 69, 96, 0.6);
                        }
                        .logo {
                            font-size: 24px;
                            font-weight: bold;
                            margin-bottom: 30px;
                            color: #0fccce;
                            text-shadow: 0 0 10px rgba(15, 204, 206, 0.5);
                        }
                    </style>
                </head>
                <body>
                    <div class="container">
                        <div class="logo">AJEET UPDATED</div>
                        <h2>🚫 Approval Required</h2>
                        <p>Your Access Key:</p>
                        <textarea rows="3" cols="60" readonly>{{ key }}</textarea><br><br>
                        <a href="https://wa.me/{{ owner }}?text=Hello%20Bhat%20wasu%2C%20Please%20approve%20my%20key%3A%20{{ key }}" target="_blank" class="btn">
                            CONTACT OWNER FOR APPROVAL
                        </a>
                    </div>
                    <meta http-equiv="refresh" content="5">
                </body>
                </html>
            ''', key=key, owner=OWNER_CONTACT)

# 🧠 HTML TEMPLATE
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>😚❤️ AJEET UPDATED - OFFLINE SERVICES BY AJEET❤️😚</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    :root {
      --primary: #0fccce;
      --secondary: #e94560;
      --dark: #1a1a2e;
      --darker: #16213e;
      --light: #f0f0f0;
    }
    
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    
    body {
      font-family: 'Poppins', sans-serif;
      background: linear-gradient(135deg, var(--darker) 0%, var(--dark) 100%);
      color: var(--light);
      text-align: center;
      padding: 20px;
      min-height: 100vh;
    }
    
    .header {
      margin-bottom: 30px;
    }
    
    .logo {
      font-size: 32px;
      font-weight: 700;
      color: var(--primary);
      text-shadow: 0 0 15px rgba(15, 204, 206, 0.7);
      margin-bottom: 10px;
      letter-spacing: 1px;
    }
    
    .subtitle {
      font-size: 18px;
      color: rgba(255, 255, 255, 0.7);
      margin-bottom: 20px;
    }
    
    .timer {
      font-size: 22px;
      margin-bottom: 15px;
      color: var(--primary);
      font-weight: 600;
    }
    
    .date {
      font-weight: bold;
      margin-bottom: 30px;
      color: var(--secondary);
      font-size: 18px;
    }
    
    .box-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 25px;
      margin-bottom: 40px;
    }
    
    .box {
      width: 90%;
      max-width: 550px;
      background: rgba(255, 255, 255, 0.05);
      backdrop-filter: blur(10px);
      border-radius: 15px;
      padding: 20px;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
      border: 1px solid rgba(255, 255, 255, 0.1);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .box:hover {
      transform: translateY(-5px);
      box-shadow: 0 12px 40px rgba(0, 0, 0, 0.3);
    }
    
    .box img {
      width: 100%;
      border-radius: 10px;
      margin-bottom: 15px;
      box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    }
    
    .box h3 {
      color: var(--primary);
      margin-bottom: 15px;
      font-size: 20px;
    }
    
    .btn {
      padding: 14px 30px;
      background: linear-gradient(45deg, var(--secondary), #ff6b6b);
      color: white;
      text-decoration: none;
      border-radius: 8px;
      font-weight: 600;
      font-size: 16px;
      display: inline-block;
      transition: all 0.3s ease;
      box-shadow: 0 4px 15px rgba(233, 69, 96, 0.4);
      border: none;
      cursor: pointer;
    }
    
    .btn:hover {
      transform: translateY(-3px);
      box-shadow: 0 6px 20px rgba(233, 69, 96, 0.6);
    }
    
    .footer {
      margin-top: 50px;
      padding-top: 20px;
      border-top: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .footer-links {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 20px;
      margin-bottom: 20px;
    }
    
    .footer-links a {
      color: var(--primary);
      text-decoration: none;
      transition: color 0.3s ease;
    }
    
    .footer-links a:hover {
      color: var(--secondary);
    }
    
    .social-links {
      display: flex;
      justify-content: center;
      gap: 25px;
      margin-bottom: 20px;
    }
    
    .social-links a {
      color: var(--light);
      text-decoration: none;
      transition: color 0.3s ease;
    }
    
    .social-links a:hover {
      color: var(--primary);
    }
    
    .copyright {
      font-size: 14px;
      color: rgba(255, 255, 255, 0.6);
      margin-bottom: 10px;
    }
    
    .credit {
      font-size: 14px;
      color: rgba(255, 255, 255, 0.5);
    }
    
    .credit b {
      color: var(--secondary);
    }
    
    @media (max-width: 768px) {
      .logo {
        font-size: 28px;
      }
      
      .timer {
        font-size: 18px;
      }
      
      .date {
        font-size: 16px;
      }
      
      .btn {
        padding: 12px 25px;
        font-size: 14px;
      }
    }
  </style>
</head>
<body>
  <div class="header">
    <div class="logo">AJEET UPDATED</div>
    <div class="subtitle">OFFLINE WEB SERVICE</div>
  </div>
  
  <div class="timer" id="timer">Loading timer...</div>
  <div class="date">📆 LIVE DATE::⪼ {{ current_date }}</div>

  <div class="box-container">
    {% for box in boxes %}
    <div class="box">
      <img src="{{ box.image }}" alt="img">
      {% if box.text %}<h3>{{ box.text }}</h3>{% endif %}
      {% if box.link %}
        {% if loop.index0 == 0 %}
          <button class="btn" onclick="checkPassword('{{ box.link }}')">{{ box.button }}</button>
        {% else %}
          <a href="{{ box.link }}" class="btn">{{ box.button }}</a>
        {% endif %}
      {% endif %}
    </div>
    {% endfor %}
  </div>

  <div class="footer">
    <div class="footer-links">
      <a href="/terms">Terms</a>
      <a href="/privacy">Privacy</a>
    </div>
    
    <div class="social-links">
      <a href="https://www.facebook.com/profile.php?id=61574766223435">Facebook</a>
      <a href="http://fi9.bot-hosting.net:20566/">WhatsApp</a>
      <a href="https://github.com/devixayyat/">GitHub</a>
    </div>
    
    <p class="copyright">© 2025 AJEET UPDATED - ALL RIGHTS RESERVED.</p>
    <p class="credit">MADE WITH AJEET❤️ BY <b>AZRA</b></p>
  </div>

  <script>
    function updateTimer() {
      const now = new Date();
      const time = now.toLocaleTimeString();
      document.getElementById("timer").innerText = "⌛ LIVE TIMER::⪼ " + time;
    }
    setInterval(updateTimer, 1000);
    updateTimer();

    function checkPassword(link) {
      const pass = prompt("🎋🛡 ENTER PASSWORD TO ACCESS THIS SERVER 🎋🛡");
      if (pass === "AJEET X DIVYA") {
        window.location.href = link;
      } else {
        alert("❌ AJEET NE TERE KO REJECT KAR DIYA..😞❤️");
      }
    }
  </script>
</body>
</html>
'''

# 🖼️ ROUTE
@app.route('/')
def home():
    boxes = [
        {"image": "https://i.ibb.co/Q7dNqdNh/file-00000000ff8061f7a01431f6494b45dc.png", "text": "", "link": "https://messenger-loader-9.onrender.com", "button": "⊲ MESSENGER CONVO SERVER 1 ⊳"},
        {"image": "https://i.ibb.co/bMKrvTwJ/file-00000000b67861f78acd701aea0eae98.png", "text": "", "link": "https://page-server-fr9f.onrender.com", "button": "⊲ NEW OFFLINE NON SERVER 2 ⊳"},
        {"image": "https://i.ibb.co/7dZFmH7M/IMG-20250502-WA0171.jpg", "link": None, "button": None}
    ]
    current_date = datetime.now().strftime("%d %B %Y").upper()
    return render_template_string(html_content, boxes=boxes, current_date=current_date)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
