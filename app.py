from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model, scaler, and label encoder
model = joblib.load('commitment_model.pkl')
scaler = joblib.load('scaler.pkl')
label_encoder = joblib.load('label_encoder.pkl')

@app.route('/')
def home():
    # Pass an empty dictionary for form_data on the first load
    return render_template('index.html', form_data={})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve data from form submission
        data = [float(x) for x in request.form.values()]
        
        # Scale data using the loaded scaler
        scaled_data = scaler.transform([data])

        # Make prediction
        prediction = model.predict(scaled_data)
        disease_name = label_encoder.inverse_transform(prediction)[0]

        # Prepare data to pass back to the form to retain values
        form_data = {key: value for key, value in request.form.items()}

        return render_template(
            'index.html',
            prediction_text=f'Result: {disease_name}',
            form_data=form_data
        )
    except Exception as e:
        return render_template(
            'index.html',
            prediction_text=f'Error: {str(e)}',
            form_data=request.form
        )

if __name__ == '__main__':
    app.run(debug=True)
