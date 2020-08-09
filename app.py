import face_recognition
from flask import Flask,request,render_template,jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''        
    #Uploading file:
    image1 = request.files['image1']
    image2 = request.files['image2']
    
    try:
        known_image = face_recognition.load_image_file(image1)
        unknown_image = face_recognition.load_image_file(image2)
        
        biden_encoding = face_recognition.face_encodings(known_image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
        
        results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
        
        scores = face_recognition.face_distance([biden_encoding], unknown_encoding)
        
        scores = int(scores[0]*100)
        
        scores = 100-scores
        
    except:
        results = ["No Face Found"]
        scores = 0
    
    return render_template("resultpage.html",prediction_text = results,score = scores)

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For rendering results on HTML GUI
    '''        
    #Uploading file:
    image1 = request.files['image1']
    image2 = request.files['image2']
    
    try:
        known_image = face_recognition.load_image_file(image1)
        unknown_image = face_recognition.load_image_file(image2)
        
        biden_encoding = face_recognition.face_encodings(known_image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
        
        results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
        if results[0]:
            result = "Images are same..!"
        else:
            result = "Images are not same..!"
        
        scores = face_recognition.face_distance([biden_encoding], unknown_encoding)
        scores = int(scores[0]*100)
        scores = 100-scores
        
    except:
        result = "No Face Found"
        scores = 0
    
    return jsonify(prediction_text = result,score = scores)

if __name__ == "__main__":
    app.run(debug=True)
