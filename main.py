import sqlite3
from flask import Flask, render_template, request


app = Flask(__name__)

app.static_folder = 'static'

data = []

def veriAl():
    global data
    with sqlite3.connect("testdb.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM project")
        data = cur.fetchall()
        for i in data:
            print(i)


def veriEkle(project_name, project_description):
    with sqlite3.connect("testdb.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO project (project_name, project_description) VALUES (?,?)", (project_name, project_description))
        con.commit()
        print("Veri eklendi " + str(project_name) + str(project_description))


def veriSil(project_name):
    with sqlite3.connect("testdb.db") as con:
        cur = con.cursor()
        delete_project = "DELETE FROM project WHERE project_name = ?"
        cur.execute(delete_project, (project_name,))
        con.commit()
        print("Veri silindi " + str(project_name))


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/terrorism-analysis")
def terror_analysis():
    return render_template("terroranalysis.html")

@app.route("/covid-analysis")
def covid_analysis():
    return render_template("covidanalysis.html")


@app.route("/rental-house-analysis")
def rental_house_analysis():
    return render_template("rentalhouseanalysis.html")

@app.route("/co2-emission-analysis")
def co2_emission_analysis():
    return render_template("co2emissionanalysis.html")

@app.route("/project-request", methods=['GET', 'POST'] )
def project_request():
    
    if request.method == 'POST':
        name = request.form['project_name']
        description = request.form['project_description']
        veriEkle(name, description)
    veriAl()
    return render_template("project_request.html", projects = data)

@app.route("/delete-request", methods=['GET', 'POST'] )
def delete_request():

    if request.method == 'POST':
        delete_name = request.form['del_project_name']
        veriSil(delete_name)
    veriAl()
    return render_template("delete_request.html", projects = data)


if __name__ == "__main__":
    app.run(debug=True)
