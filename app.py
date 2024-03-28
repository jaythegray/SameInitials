from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

def estimate_people_with_initials(initials):
    global_population = 7.9e9  # Global population
    # Example frequencies, replace with your actual frequencies loaded from a JSON file or defined directly
    frequencies = {
        "A": 0.08, "B": 0.05, "C": 0.06, "D": 0.04, "E": 0.03,
        "F": 0.02, "G": 0.03, "H": 0.03, "I": 0.02, "J": 0.07,
        "K": 0.04, "L": 0.04, "M": 0.07, "N": 0.03, "O": 0.02,
        "P": 0.03, "Q": 0.01, "R": 0.05, "S": 0.06, "T": 0.04,
        "U": 0.01, "V": 0.02, "W": 0.02, "X": 0.01, "Y": 0.02,
        "Z": 0.02
    }

    initials = [i.strip().upper() for i in initials if i.strip().upper() in frequencies.keys()]
    estimated_freqs = [frequencies.get(initial, 0.01) for initial in initials]
    estimated_people = global_population * sum(estimated_freqs) / len(estimated_freqs)
    percentage = (sum(estimated_freqs) / len(estimated_freqs)) * 100

    detailed_response = (
        f"Based on the provided initials {''.join(initials)}, our estimate suggests that "
        f"approximately {estimated_people:.0f} people, or about {percentage:.2f}% of the global "
        f"population, might share these initials. This estimate is derived from analyzing "
        f"the frequency of each initial letter in global naming conventions, adjusting for "
        f"the overall distribution of names. For initials considered 'common' (A, S, T, J, M), "
        f"a higher frequency is applied, while 'uncommon' or 'rare' initials (e.g., Q, X, Z) "
        f"reflect a lower estimated prevalence. The calculation assumes uniform distribution "
        f"and does not account for regional variations in naming practices, which can significantly "
        f"affect actual frequencies. It's a fun way to think about the uniqueness of one's initials "
        f"in the context of the global population!"
    )

    return detailed_response

@app.route('/')
def index():
    # Ensure that index.html is located within the 'templates' directory relative to this script
    return render_template('index.html')

@app.route('/estimate', methods=['POST'])
def estimate():
    data = request.json
    initials = data.get('initials', [])
    result = estimate_people_with_initials(initials)
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)