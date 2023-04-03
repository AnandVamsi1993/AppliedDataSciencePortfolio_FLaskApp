from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/GraduateStudiesOverview')
def overview():
    return render_template('overview.html')

@app.route('/GraduateStudiesOverview/NFLProject')
def nfl():
    return render_template('NFL_Project.html')

@app.route('/ResearchProject')
def ResearchProject():
    return render_template('ResearchProject.html')

@app.route("/GraduateStudiesOverview/StudenthostelAccomodation")
def StudentHostel():
    return render_template('StudentHostel.html')

@app.route("/GraduateStudiesOverview/NLPProject")
def NLPProject():
    return render_template('NLPProject.html')

@app.route("/GraduateStudiesOverview/Blogpost")
def Blogpost():
    return render_template('Blogpost.html')

if __name__ == "__main__":
    app.run(debug = False, host = '0.0.0.0')