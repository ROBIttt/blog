from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Тимчасове сховище для постів у пам'яті програми
posts = [
    {
        "id": 1,
        "author": "Богдан",
        "title": "Мій перший допис у блозі",
        "content": "завтра треба в школу",
        "date": "20.09.1999, 15:00"
    },
    {
        "id": 2,
        "author": "Анонім",
        "title": "Супер крутий заговолок",
        "content": "я незнаю що тут писати, але я напишу щось дуже цікаве і захоплююче, щоб привернути увагу читачів. Можливо, це буде історія про пригоди в далекій галактиці або про неймовірні відкриття в науці. Головне, щоб це було захоплююче і залишило слід у серцях тих, хто читає.",
        "date": "51.08.2026, 23:59"
    }
]

@app.route('/')
def index():
    return render_template('index.html', posts=reversed(posts))

@app.route('/add', methods=['POST'])
def add_post():
    # Отримуємо дані з форми
    author = request.form.get('author') or 'Анонім'
    title = request.form.get('title')
    content = request.form.get('content')
    
    if title and content:
        new_post = {
            "id": len(posts) + 1,
            "author": author.strip(),
            "title": title.strip(),
            "content": content.strip(),
            "date": datetime.now().strftime("%d.%m.%Y, %H:%M")
        }
        posts.append(new_post)
        
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)