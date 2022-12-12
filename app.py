from flask import Flask, request, send_file, render_template
import json 
import os


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/class")
def pageclass():
    return render_template("index-with-class.html")

@app.route("/random")
def show_random_cat():
    # get random code from what's available
    code = "418"
    # look up that random code
    try:
        codetext, prompt = get_codetext_prompt(code)
    except KeyError:
        print("You get a 404, actually.")
        return render_template('404.html'), 404
    return render_template("cats.html", code=code, codetext=codetext, prompt=prompt)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    # note that we set the 404 status explicitly
    return render_template('500.html'), 500

@app.route("/1xx")
def shsow_class():
    # note that we set the 404 status explicitly
    return render_template("1xx.html")



@app.route('/<int:variable>', methods=['GET'])
def get_cat(variable):
    code = str(variable)
    codetext = str()
    prompt = str()
    try:
        codetext, prompt = get_codetext_prompt(code)
    except KeyError:
        print("You get a 404, actually.")
        return render_template('404.html'), 404
    return render_template("cats.html", code=code, codetext=codetext, prompt=prompt)

def get_codetext_prompt(code):
    f = open('data/prompts.json')
    data = json.load(f)
    codetext = data[code]['codetext']
    prompt = data[code]['prompt']
    # Closing file
    f.close()
    return codetext, prompt 

if __name__ == "__main__":
    app.directory='./'
    # app.run(host='127.0.0.1', port=5000)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
