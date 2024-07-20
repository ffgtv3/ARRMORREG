from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        amount = request.form.get('amount')
        name = request.form.get('name')
        agree = request.form.get('agree')

        if agree == 'yes':
            # Перенаправление на указанный сайт
            return redirect('https://example.com')  # Замените на ваш URL
        else:
            # Перенаправление на страницу с сообщением об отказе
            return redirect(url_for('denied'))

    return render_template('index.html')

@app.route('/denied')
def denied():
    return "Вы отказались от согласия и были перенаправлены."

if __name__ == '__main__':
    app.run(debug=True)
