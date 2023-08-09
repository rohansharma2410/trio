from flask import Flask, request, jsonify
import impl
app = Flask(__name__)

@app.route('/appointment', methods=['GET'])
def receive_input():
   args = request.args
   realtime= impl.predict(args.get("name"),args.get("age"),args.get("sex"),args.get("disease"))


   return str(realtime)

if __name__ == '__main__':
    app.run(debug=True)
