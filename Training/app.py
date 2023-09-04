import os
from flask import Flask
from flask import render_template
import socket
import random
import os

app = Flask(__name__)

color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40"
}

#Usage: docker run -d -e color=blue -p 80:80 imagename
color = os.environ.get('APP_COLOR') or random.choice(["red","green","blue","blue2","darkblue","pink"])

@app.route("/")
def main():
    #return 'Hello'
    print(color)
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[color])

@app.route('/color/<new_color>')
def new_color(new_color):
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[new_color])

@app.route('/devops')
def devops():
    contents = 'DevOps is a set of practices, tools, and a cultural philosophy that automate and integrate the processes between software development and IT teams.'
    return render_template('hello.html', name=socket.gethostname(), contents=contents, color=color_codes[color])

javed_color = os.getenv("javed_color", "red")
@app.route('/javed')
def javed():
    contents = 'Why dont scientists trust atoms? Because they make up everything!'
    return render_template('hello.html', name=socket.gethostname(), contents=contents, color=color_codes[javed_color])

@app.route('/shu')
def shu():
    contents = "when all else fails,there's always delusion"
    return render_template('hello.html', name=socket.gethostname(), contents=contents, color=color_codes[color])
   
@app.route('/ramya')
def ramya():
    contents = 'All my life I thought air was free until I bought a bag of chips!!'
    return render_template('hello.html', name=socket.gethostname(), contents=contents, color=color_codes[color])

@app.route('/shamani')
def shamani():
    contents = "If you are the smartest person in the room, then you are in the wrong room."
    return render_template('hello.html', name=socket.gethostname(), contents=contents, color=color_codes[color])

@app.route('/swarna')
def swarna():
    contents = 'The only thing worse than being talked about is not being talked about!!'
    return render_template('hello.html', name=socket.gethostname(), contents=contents, color=color_codes[color])


@app.route('/sthita')
def sthita():
    contents = 'What is army members first drink? WARter'
    return render_template('hello.html', name=socket.gethostname(), contents=contents, color=color_codes[color])

@app.route('/anisha')
def anisha():
    contents = 'Love is the one thing that transcends time and space.'
    return render_template('hello.html', name=socket.gethostname(), contents=contents, color=color_codes[color])

@app.route('/poushali')
def poushali():
    contents = 'I used to think I was indecisive. But now I am not so sure.'
    return render_template('hello.html', name=socket.gethostname(), contents=contents, color=color_codes[color])

@app.route('/animesh')
def animesh():
    contents = 'You\'re like my pole star. When I\'m lost in darkness, I know you\'ll guide me through'
    return render_template('hello.html', name=socket.gethostname(), contents=contents, color=color_codes[color])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80")