import numpy as np
from flask import Flask, request, render_template
import pickle
app = Flask(__name__, template_folder="templates")
model = pickle.load(open('model.pkl', 'rb'))
model1 = pickle.load(open('model1.pkl', 'rb'))


@app.route('/')
def h():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET'])
def predict():
    # Get all form parameters
    cgpa = request.args.get('cgpa')
    projects = request.args.get('projects')
    workshops = request.args.get('workshops')
    mini_projects = request.args.get('mini_projects')
    skills = request.args.get('skills')
    communication_skills = request.args.get('communication_skills')
    internship = request.args.get('internship')
    hackathon = request.args.get('hackathon')
    tw_percentage = request.args.get('tw_percentage')
    te_percentage = request.args.get('te_percentage')
    backlogs = request.args.get('backlogs')
    name = request.args.get('name')

    # Handle empty values with default 0
    if cgpa == '' or cgpa is None:
        cgpa = '0'
    if projects == '' or projects is None:
        projects = '0'
    if workshops == '' or workshops is None:
        workshops = '0'
    if mini_projects == '' or mini_projects is None:
        mini_projects = '0'
    if skills == '' or skills is None:
        skills = '0'
    if communication_skills == '' or communication_skills is None:
        communication_skills = "0"
    if internship == '' or internship is None:
        internship = '0'
    if hackathon == '' or hackathon is None:
        hackathon = '0'
    if tw_percentage == '' or tw_percentage is None:
        tw_percentage = '0'
    if te_percentage == '' or te_percentage is None:
        te_percentage = '0'
    if backlogs == '' or backlogs is None:
        backlogs = '0'

    # Count skills (comma-separated)
    s = 1
    if skills:
        for i in skills:
            if i == ',':
                s = s + 1

    # Convert to appropriate types
    internship = int(internship)
    hackathon = int(hackathon)

    # Features for placement prediction (12 features matching training)
    # Order: CGPA, Major Projects, Workshops, Mini Projects, Skills, Communication Skills,
    #        Internship, Hackathon, 12th %, 10th %, backlogs, (extra 0 for unused column)
    arr = np.array([[float(cgpa), int(projects), int(workshops), int(mini_projects),
                     s, float(communication_skills), internship, hackathon,
                     float(tw_percentage), float(te_percentage), int(backlogs), 0]])
    output = model.predict(arr)

    # Determine placement status (1 = Placed, 0 = NotPlaced) for salary model
    if output[0] == 'Placed':
        p = 1  # Encoded as 1 for "Placed"
    else:
        p = 0  # Encoded as 0 for "NotPlaced"

    # Features for salary prediction (12 features including PlacementStatus)
    # Order: CGPA, Major Projects, Workshops, Mini Projects, Skills, Communication Skills,
    #        Internship, Hackathon, 12th %, 10th %, backlogs, PlacementStatus
    arr1 = np.array([[float(cgpa), int(projects), int(workshops), int(mini_projects),
                      s, float(communication_skills), internship, hackathon,
                      float(tw_percentage), float(te_percentage), int(backlogs), p]])
    salary = model1.predict(arr1)
    salary_value = abs(int(round(salary[0])))

    # Format salary with commas
    k = str(salary_value)
    l = len(k)
    if l == 6:
        k = k[0] + ',' + k[1:3] + ',' + k[3:]
    elif l == 7:
        k = k[0:2] + ',' + k[2:5] + ',' + k[5:]

    if output[0] == 'Placed':
        out = f'Congratulations {name}!! You have high chances of getting placed!!!'
        out2 = f'Your Expected Salary will be INR {k} per annum'
        return render_template('out.html', output=out, output2=out2)
    else:
        out = f'Sorry {name}!! You have low chances of getting placed. All the best!!!!'
        out2 = 'Improve your skills...'
        return render_template('out.html', output=out, output2=out2)


if __name__ == "__main__":
    app.run(debug=True)
