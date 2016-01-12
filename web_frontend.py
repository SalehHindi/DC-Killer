'''
This is the main program loop. This generates the front end and generates all URLS for the user to visit.
'''
# TODO: 2 Generate all food URLS once the database is done
#

import web_scraper
from flask import *
#from flask_bootstrap import Bootstrap

DC_menu=web_scraper.Webget()
DC_menu=DC_menu.format_to_HTML()

app = Flask(__name__)

@app.route("/Haverford/")
def hello_monkey():
    return render_template('index.html', title='Home', menu=DC_menu)

@app.route('/<letter>')
def test(letter):
    return render_template('index.html', title=c, menu=DC_menu)

'''This is how I will implement a new url for each food. For all foods that are available today, generate a URL for them
Maybe I'll generate for all foods period. I don't know yet. Also, the URL should be /Haverford/food because each
food will be unique to each location'''
for c in 'abcdef':
    with app.test_request_context():
        url_for('test', letter=c)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True)