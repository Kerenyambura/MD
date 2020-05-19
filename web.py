from flask import Flask,render_template,url_for,request,redirect



app=Flask(__name__)

@app.route('/')
def web():
    return '<h1> My first website</h1>'


@app.route('/home')
def home():
    return render_template ('home.html')

@app.route('/about')
def about():
    return render_template('aboutus.html')

@app.route('/services')
def services():
    return render_template('service.html')

@app.route('/ourwork')
def ourwork():
    return render_template('portfolio.html')

@app.route('/contactus')
def contactus():
    return render_template('contact.html')


















if __name__ == '__main__':
    app.run()