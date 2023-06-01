from flask import Flask, render_template, request,flash
from flask_cors import CORS
import numpy as np
import pickle


app = Flask(__name__)
CORS(app)
model = pickle.load(open('Kidney_24.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

# 'sg', 'dm', 'htn', 'hemo', 'al', 'appet', 'pc', 'pe', 'rc', 'sc', 'bgr',
#        'bu', 'bp', 'rbc', 'ane', 'sod', 'age', 'su', 'pcc', 'cad', 'wc', 'pot',
#        'ba'

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        sg = float(request.form['sg'])
        htn = float(request.form['htn'])
        hemo = float(request.form['hemo'])
        dm = float(request.form['dm'])
        al = float(request.form['al'])
        appet = float(request.form['appet'])
        rc = float(request.form['rc'])
        pc = float(request.form['pc'])

        pe = float(request.form['pe'])
        sc = float(request.form['sc'])
        bgr = float(request.form['bgr'])
        bu = float(request.form['bu'])
        bp = float(request.form['bp'])
        rbc = float(request.form['rbc'])
        ane = float(request.form['ane'])
        sod = float(request.form['sod'])

        age = float(request.form['age'])
        su = float(request.form['su'])
        pcc = float(request.form['pcc'])
        cad = float(request.form['cad'])
        wc = float(request.form['wc'])
        pot = float(request.form['pot'])
        ba = float(request.form['ba'])
        pcv = float(request.form['pcv'])

        values = np.array([[age, bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sod,pot,hemo,pcv,wc,rc,htn,dm,cad,appet,pe,ane]])
        prediction = model.predict(values)
        # if 0 == prediction[0]:
        #   print(prediction[0])
        #   flash('disease detected')
        #   if int(bp) >= 60 and int(appet) == 0 and float(hemo) < 9.9:
        #      return "stage4"
        #     #   return render_template('stage4.html')
        #   elif int(bp) >= 60 and int(appet) == 0:
        #      return "stage3"
        #     #   return render_template('stage3.html')
        #   elif int(appet) == 0:
        #      return "stage2"
        #     #   return render_template('stage2.html')
        #   elif int(bp) >= 60:
        #       return "stage1"
        #     #   return render_template('stage1.html')
        # else:
        #   flash('you dont have disease , u can eat everything ')

        return render_template('result.html', prediction=prediction,bp=bp,hemo=hemo,appet=appet)


if __name__ == "__main__":
    app.run(debug=True)

