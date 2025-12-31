from flask import Flask, redirect, render_template, render_template, request, url_for

app =Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/success/<name>')
def success(name):
    return f'welcome {name}'

@app.route('/login', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))
    
if __name__ == "__main__":
    app.run(debug=True).
