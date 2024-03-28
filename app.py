from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

def estimate_people_with_initials(initials):
    global_population = 7.9e9  # Global population

    # Assuming you have loaded your frequencies from JSON as before
    frequencies = {
        "A": 0.08, "B": 0.05, "C": 0.06,  # Include all your mappings here
    }

    # Ensure the initials are uppercase and validate them
    initials = [i.strip().upper() for i in initials]
    valid_initials = [i for i in initials if i in frequencies]

    # Calculate the frequency for each valid initial
    estimated_freqs = [frequencies.get(initial, 0.01) for initial in valid_initials]
    estimated_people = global_population * sum(estimated_freqs) / len(estimated_freqs)

    # Calculate the percentage of the global population
    percentage = (sum(estimated_freqs) / len(estimated_freqs)) * 100

    # Detailed response
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
    return render_template('index.html')

@app.route('/estimate', methods=['POST'])
def estimate():
    data = request.json
    initials = data.get('initials', [])
    result = estimate_people_with_initials(initials)
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
