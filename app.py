from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def calculate_estimated_people(initials):
    global_population = 7.9e9  # Global population
    
    # Simulated frequencies for each initial for demonstration purposes
    frequencies = {
        'A': 0.08, 'B': 0.07, 'C': 0.06, 'D': 0.05, 'E': 0.04,
        'F': 0.03, 'G': 0.05, 'H': 0.04, 'I': 0.03, 'J': 0.07,
        'K': 0.05, 'L': 0.04, 'M': 0.06, 'N': 0.03, 'O': 0.02,
        'P': 0.04, 'Q': 0.01, 'R': 0.05, 'S': 0.06, 'T': 0.05,
        'U': 0.02, 'V': 0.03, 'W': 0.04, 'X': 0.01, 'Y': 0.02, 'Z': 0.01,
    }
    
    # Calculate the average frequency of the initials provided
    avg_frequency = sum(frequencies.get(initial, 0.01) for initial in initials) / len(initials)
    
    # Estimate the number of people with these initials
    estimated_people = avg_frequency * global_population
    
    return estimated_people

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/estimate', methods=['POST'])
def estimate():
    data = request.json
    initials = data.get('initials', [])
    
    estimated_people = calculate_estimated_people(initials)
    percentage = estimated_people / 7.9e9 * 100
    
    result = (
        f"Based on the provided initials {''.join(initials)}, our refined estimate suggests that "
        f"approximately {estimated_people:,.0f} people, or about {percentage:.4f}% of the global "
        f"population, might share these initials. Remember, this model uses a simplified "
        f"estimation process and should be taken as an engaging way to consider initials' uniqueness!"
    )
    
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)