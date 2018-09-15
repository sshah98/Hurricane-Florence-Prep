from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/map')
def map():
    return render_template('hurrycane_map.html')

if __name__ == '__main__':
    app.run(debug=True)