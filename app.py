from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello this is Whale Coffee Home Page'

@app.route('/test')
def test():
    return 'test'

if __name__=="__main__":
    app.run()