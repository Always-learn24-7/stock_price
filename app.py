from flask import Flask, render_template,request, jsonify
import json
import core
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/price', methods=['POST'])
def get_price():
    #print("Getting Price")
    rf=request.form
    # print(rf)
    for key in rf.keys():
        data=key
        # print(data)
        data_dic=json.loads(data)
        # print(data_dic.keys())
        company_name = data_dic['company_name']
        # print(type(company_name[0]))
        Price=core.price(company_name[0])
        # print(Price)
    resp_dic={'price':Price}
    resp = jsonify(resp_dic)
    resp.headers['Access-Control-Allow-Origin']='*'
    return resp

if __name__ == "__main__":
    app.run(debug=True)