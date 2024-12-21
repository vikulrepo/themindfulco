from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Here you can handle the form data, like sending an email
    return f"Thank you for reaching out, {name}. We will get back to you soon!"

if __name__ == '__main__':
    app.run(debug=True)
