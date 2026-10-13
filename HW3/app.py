from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)
# 간단한 in-memory 데이터 저장소
todos = []
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        db.session.add(Todo(text=request.form['todo'],note=request.form['note']) )

        db.session.commit()
        return redirect(url_for('index'))
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@app.route('/delete/<int:id>')
def delete(id):
    todo = db.get_or_404(Todo, id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/toggle/<int:id>')
def toggle(id):
    todo = db.get_or_404(Todo, id)
    todo.done = not todo.done
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    todo = db.get_or_404(Todo, id)
    if request.method == 'POST':
        todo.text = request.form['todo']
        todo.note = request.form.get('note', '')

        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit.html', todo=todo)



class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, default=False)
    note = db.Column(db.String(200))
    def __repr__(self):
        return f'<Todo {self.id} {self.text} {self.note}>'

with app.app_context():
    db.create_all()



if __name__ == '__main__':
    app.run(debug=True)

