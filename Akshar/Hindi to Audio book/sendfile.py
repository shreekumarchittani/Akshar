from flask import *
from gtts import gTTS
import os
from googletrans import Translator

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def init():
    return render_template('upload.html')

@app.route('/convertToMP3',methods=['POST'])
def convertToMP3():
	if request.method == 'POST':
    	#f = open('/home/shree/Desktop/Projects/MiniSendFile/convertedTextfile.txt','r')
		f = request.files['myfile']
		f.save(f.filename)
		print('endter')
		mytext=open(f.filename,'r').read()
		"""filename = secure_filename(f.filename)
		f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
		mytext = f.read()
		translator = Translator()"""
		language = 'hi'
		myobj = gTTS(text=mytext, lang=language, slow=False)
		myobj.save("mp3file.mp3")
		return send_file('mp3file.mp3',as_attachment=True)
if __name__ == '__main__':
    app.run()
