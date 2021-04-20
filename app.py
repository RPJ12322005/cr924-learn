from flask import Flask, render_template, jsonify,request
app = Flask(__name__)

#class Thing:
  #def __init__(self, text,color):
 #   self.text = text
 #   self.color = color

newThing = {
        "text": "Plants That I Have!!",
        "color": "#50c878"
    }      
 
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/text', methods=['GET'])
def getText():
   return "is this working"

   
@app.route("/thing",methods=['GET'])
def getThing():

   return jsonify(newThing)


@app.route("/testPost", methods=['POST'])
def postThing():
   data = request.json
   newThing['text'] = data['text']
   newThing['color'] = data['color']
   return jsonify(newThing)
  
  


if __name__ == '__main__':
   app.run()





