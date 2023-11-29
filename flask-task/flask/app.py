from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.route('/contact')
def view_contact():
    return 'This is the contact page'

@app.route('/products')
def view_products():
    return 'Its our first deployment, we dont have any products yet'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5003)
