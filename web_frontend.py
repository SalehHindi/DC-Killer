'''
This is the front end to the program.
It will be how the user interacts with the program and selects
menu items that they like and want to be notified
'''

import web_scraper
from flask import *
#from flask_bootstrap import Bootstrap

app = Flask(__name__)
#Bootstrap(app)

@app.route("/Haverford/")
def hello_monkey():
    """Respond to incoming calls with a simple text message."""

    return render_template('base.html', title='Home',)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)