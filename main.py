from flask import Flask, request, redirect, render_template


app = Flask(__name__)


@app.route('/')
def front():
    return render_template('front.html')


@app.route('/ussr')
def ussr():
    return render_template('soviet.html')

@app.route('/germany')
def germany():
    return render_template('germany.html')

    
if __name__ == '__main__':
    app.run(debug=True)