

from flask import Flask, render_template

app = Flask(__name__)

club = {
    "name": "Футбольный клуб Феникс",
    "president": "Михаил Зыков",
    "coach": "Михаил Зыков",
    "star_player": "Михаил Зыков",
    "players": [
        "Иван Петров",
        "Алексей Смирнов",
        "Дмитрий Кузнецов",
        "Сергей Иванов",
        "Максим Попов",
        "Андрей Соколов",
        "Никита Волков",
        "Вова Федоров",
        "Артем Лебедев",
        "Роман Павлов"
    ],
    "creator": "Зыков Михаил"
}

@app.route("/")
def home():
    return render_template("index.html", club=club)

@app.route("/team")
def team():
    return render_template("team.html", club=club)

@app.route("/about")
def about():
    return render_template("about.html", club=club)

if __name__ == "__main__":
    app.run(debug=True)

import os

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)

import psycopg
import os

DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg.connect(DATABASE_URL)

from supabase import create_client
import os

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

def upload_file(file):
    supabase.storage.from_("images").upload(file.filename, file)

from flask import request, session, redirect

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        if request.form['password'] == os.getenv("ADMIN_PASSWORD"):
            session['admin'] = True
            return redirect('/admin/dashboard')
    return render_template('admin.html')

