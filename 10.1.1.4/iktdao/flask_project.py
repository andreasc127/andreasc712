from flask import Flask, request
import random
import webbrowser


app = Flask(__name__)

@app.route('/')

def index():
    value = random.randint(49, 4698)
    if value <= 4670:
        webbrowser.open('https://andreasc127.github.io/andreasc712/10.1.1.4/iktdao/node/'+f'{value}'+'.html')
        return 'https://andreasc127.github.io/andreasc712/10.1.1.4/iktdao/node/'+f'{value}'+'.html'
    else:
        webbrowser.open('https://andreasc127.github.io/andreasc712/10.1.1.4/iktdao/node/'+f'{value}'+'.htm')
        return 'https://andreasc127.github.io/andreasc712/10.1.1.4/iktdao/node/'+f'{value}'+'.htm'






if __name__ == "__main__":
    app.run()


