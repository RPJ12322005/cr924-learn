from flask import Flask, render_template, jsonify
app = Flask(__name__)

#class Thing:
  #def __init__(self, text,color):
 #   self.text = text
 #   self.color = color

 
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/text', methods=['GET'])
def getText():
   return "is this working"

   
@app.route("/thing",methods=['GET'])
def getThing():
 ##  newThing = Thing("Plants That I Have!","#50c878")
   
   newThing = {
        "text": "Plants That I Have!!",
        "color": "#50c878"
    }

   return jsonify(newThing)




if __name__ == '__main__':
   app.run()
