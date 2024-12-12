from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app, origins="*")

@app.route('/analyze-symptoms', methods=['POST'])
def analyze_symptoms():
    data = request.json
    selected_symptoms = data.get('symptoms', [])
    Disease = []
    Remedy = []

    if 'Symptom 1' in selected_symptoms and 'Symptom 2' in selected_symptoms and 'Symptom 3' in selected_symptoms and 'Symptom 4' in selected_symptoms:
        Disease.append('ANTHRACNOSE')
        Remedy.append('Spray Carbondazin (0.1%) or Difolatan (0.2%)')
    if 'Symptom 1' in selected_symptoms and 'Symptom 5' in selected_symptoms and 'Symptom 6' in selected_symptoms and 'Symptom 7' in selected_symptoms:
        Disease.append('TWIG BLIGHT OR DIPLODIA')
        Remedy.append('Prune the dead twigs and spray with Benomyl (2.5g/ litre of water)')
    if 'Symptom 1' in selected_symptoms and 'Symptom 4' in selected_symptoms and 'Symptom 6' in selected_symptoms and 'Symptom 8' in selected_symptoms and 'Symptom 9' in selected_symptoms and 'Symptom 10' in selected_symptoms:
        Disease.append('POWDERY MILDEW')
        Remedy.append('Spray Wettable Sulphur (1.5kg/200 litres of water)')
    if 'Symptom 11' in selected_symptoms and 'Symptom 12' in selected_symptoms:
        Disease.append('ANTHRACNOSE')
        Remedy.append('Spray Copper Oxychloride (0.1%) or Difolatan (0.2%)')
    if 'Symptom 13' in selected_symptoms and 'Symptom 14' in selected_symptoms and 'Symptom 15' in selected_symptoms and 'Symptom 16' in selected_symptoms:
        Disease.append('STYLER END ROT')
        Remedy.append('Spray Copper Oxychloride (0.3%)')
    if 'Symptom 17' in selected_symptoms and 'Symptom 18' in selected_symptoms and 'Symptom 19' in selected_symptoms and 'Symptom 20' in selected_symptoms:
        Disease.append('GUAVA WILT')
        Remedy.append('Spray Bavistin (0.1%) around the roots and leaves at an interval of 15 days')
    if 'Symptom 21' in selected_symptoms and 'Symptom 22' in selected_symptoms and 'Symptom 23' in selected_symptoms and 'Symptom 24' in selected_symptoms:
        Disease.append('CAPSULE ROT')
        Remedy.append('Remove and burn the infected plants, spray Bordeaux mixture (1%) monthly')
    if 'Symptom 22' in selected_symptoms and 'Symptom 25' in selected_symptoms and 'Symptom 26' in selected_symptoms and 'Symptom 27' in selected_symptoms:
        Disease.append('CLUMP ROT')
        Remedy.append('Remove the infected plants, spray Copper oxychloride (0.25%) in the nursery beds')

    if not Disease:
        Disease.append('NO DISEASE FOUND BASED ON YOUR INPUT')
        Remedy.append('No remedy recommended')

    return jsonify({'Disease': Disease, 'Remedy': Remedy})

if __name__ == '__main__':
    app.run(debug=True)
