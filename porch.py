from neopixels import *
import sys
from flask import Flask, render_template, request

app = Flask(__name__)

routines = {
   'noir' : {'func' : noir, 'name' : 'Noir (all off)', 'state' : 1},
   'rain' : {'func': rain, 'name' : 'Rainbow Slide', 'state' : 0},
   'green' : {'func': green, 'name' : 'Green Mumble', 'state' : 0},
   'pink' : {'func': pink, 'name' : 'Pink Bunnies', 'state' : 0},
   }

@app.route('/', methods=["GET"])
def index():
    print('------- STARTING INDEX() --------', file=sys.stderr)
    noir()
    templateData = {
      'routines' : routines
      }

    for routine in routines:
      routines[routine]['state'] = 0

    picked = request.args.get('options', default = 'rain')

    print('picked == ', picked, file=sys.stderr)

    routines[picked]['state'] = 1

    if picked == 'noir':
      noir()
      return render_template('index.html', **templateData, picked = 'options')

    while routines[picked]['state'] == 1:
      print('while picked == ', picked, file=sys.stderr)

      routines[picked]['func']()

      print('while2 picked == ', picked, file=sys.stderr)

    noir()
    return render_template('index.html', **templateData)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
