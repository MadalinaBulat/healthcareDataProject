from flask import Flask, send_file, jsonify
import matplotlib
matplotlib.use('Agg')  # Set the non-interactive backend
import matplotlib.pyplot as plt
import pandas as pd
import io
import os

app = Flask(__name__)

# Load the dataset
df = pd.read_csv("healthcare_dataset.csv")

# Function to generate an age distribution histogram
@app.route('/age-distribution')
def generate_age_histogram():
    plt.figure(figsize=(10, 6))
    plt.hist(df['Age'], bins=10, color='skyblue', edgecolor='black')
    plt.title("Age Distribution of Patients")
    plt.xlabel("Age")
    plt.ylabel("Number of Patients")
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')

# Function to generate a gender distribution pie chart
@app.route('/gender-distribution')
def generate_gender_pie():
    gender_counts = df['Gender'].value_counts()
    plt.figure(figsize=(8, 8))
    gender_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['lightblue', 'lightpink'])
    plt.title("Gender Distribution of Patients")
    plt.ylabel("")  # Hides the default ylabel

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')

# Function to generate a blood type frequency bar chart
@app.route('/blood-type-frequency')
def generate_blood_type_bar():
    blood_type_counts = df['Blood Type'].value_counts()
    plt.figure(figsize=(10, 6))
    blood_type_counts.plot(kind='bar', color='purple')
    plt.title("Blood Type Frequency")
    plt.xlabel("Blood Type")
    plt.ylabel("Number of Patients")

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')

# Function to generate a medical condition breakdown bar chart
@app.route('/medical-condition-breakdown')
def generate_medical_condition_bar():
    condition_counts = df['Medical Condition'].value_counts()
    plt.figure(figsize=(10, 6))
    condition_counts.plot(kind='bar', color='orange')
    plt.title("Medical Condition Breakdown")
    plt.xlabel("Condition")
    plt.ylabel("Number of Patients")

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')

# Function to generate a billing amount distribution histogram
@app.route('/billing-amount-distribution')
def generate_billing_amount_histogram():
    plt.figure(figsize=(10, 6))
    plt.hist(df['Billing Amount'], bins=10, color='green', edgecolor='black')
    plt.title("Billing Amount Distribution")
    plt.xlabel("Billing Amount ($)")
    plt.ylabel("Number of Patients")

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')

# Home route to list available endpoints
@app.route('/')
def home():
    return jsonify({
        'endpoints': {
            '/age-distribution': 'Generates an age distribution histogram',
            '/gender-distribution': 'Generates a gender distribution pie chart',
            '/blood-type-frequency': 'Generates a blood type frequency bar chart',
            '/medical-condition-breakdown': 'Generates a medical condition breakdown bar chart',
            '/billing-amount-distribution': 'Generates a billing amount distribution histogram'
        }
    })

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))  
    app.run(host='0.0.0.0', port=port, debug=True)

