from flask import Flask, render_template

# This is test comment
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Cal.html')  # Render the Cal.html file

@app.route('/test')
def test():
    return render_template('Test.html')  # Render the Test.html file

if __name__ == '__main__':
    app.run(debug=True)