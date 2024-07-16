from flask import Flask, render_template, redirect, url_for
from werkzeug.security import generate_password_hash
from flask_wtf.csrf import CSRFProtect

from homework.flask3.form import RegistrationForm
from homework.flask3.models import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = '2305f468abbecee0be153cb7a2f29b633d55ca74afaadf59e7f305eaf0b03417'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../../instance/mydatabase.db'
db.init_app(app)

@app.route('/register/', methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
      hashed_password = generate_password_hash(form.password.data)  # Хэширование пароля перед сохранением в базе данных
      new_user = User(first_name=form.first_name.data,
                      last_name=form.last_name.data,
                      email=form.email.data,
                      password_hash=hashed_password)
      db.session.add(new_user)  # Добавление нового пользователя в сессию базы данных
      db.session.commit()        # Сохранение изменений в базе данных
      return redirect(url_for('success'))
  return render_template('register.html', form=form)

# Маршрут для отображения страницы успешной регистрации
@app.route('/success')
def success():
   return "Регистрация прошла успешно!"

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


if __name__ == '__main__':
    app.run(debug=True)


