from flask import *
import PyPDF2
from googletrans import Translator
import os
import pdftotext

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/', methods=['GET','POST'])
def convertor():
    return render_template('file.html')

@app.route('/success', methods=['GET','POST'])
def success():
    if request.method == 'POST':
        open('temp.txt','w').close()
        f = request.files['myfile']
        f.save(f.filename)
        #a = open(f.filename, 'rb')
        #pdfReader = PyPDF2.PdfFileReader(a)
        with open(f.filename, "rb") as a:
            pdf = pdftotext.PDF(a)
        with open('temp.txt', 'w') as t:
            t.write("\n\n".join(pdf))
        """Temptext=''
        for i in range(2):
            pageObj = pdfReader.getPage(i)
            Temptext += pageObj.extractText()
        #session['text'] = Temptext
        English_file = open('temp.txt','w')
        English_file.write(Temptext)
        English_file.close()
        #return render_template('success.html',name = Temptext)"""
        translator = Translator()
        #HindiText = translator.translate(session['text'],'hindi')
        Temptext=open('temp.txt','r').read()
        print(Temptext)
        HindiText = translator.translate(Temptext,'hindi')
        text = HindiText.text
        open('temp.txt','w').close()
        HindiTextFile = open('temp.txt','w')
        HindiTextFile.write(text)
        HindiTextFile.close()
        return send_file('temp.txt',as_attachment=True)
"""
@app.route('/hindi', methods = ['GET','POST'])
def hindi():
    translator = Translator()
    #HindiText = translator.translate(session['text'],'hindi')
    HindiText = translator.translate(t,'hindi')
    text = HindiText.text
    open('temp.txt','w').close()
    HindiTextFile = open('temp.txt','w')
    HindiTextFile.write(text)
    HindiTextFile.close()
    return send_file('temp.txt',as_attachment=True)"""
    
if __name__ == '__main__':
    app.run(debug=True)
