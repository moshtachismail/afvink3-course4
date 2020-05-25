from flask import Flask, render_template, request
import mysql.connector
app = Flask(__name__)

@app.route('/')
def hello_world():
    search= request.args.get('search', '')
    all_rows= conn(search)
    rijen = dik(all_rows, search)
    return render_template("kans2.html",rijen=rijen)


def conn(search):
    connectie = mysql.connector.connect(host="ensembldb.ensembl.org",
                                        user="anonymous",
                                        database="homo_sapiens_core_95_38")

    cursor = connectie.cursor()
    query = "select description from gene where description like \'%{}%\'limit 50 " \
            .format(search)
    cursor.execute(query)

    all_rows = cursor.fetchall()
    return all_rows

def dik(all_rows, search):
    rijen = []
    for x in all_rows:
        for c in x:
            print(x)
            b = c.replace(search, '<b>' + search + '</b>')
            rijen.append(b)

    return rijen


if __name__ == '__main__':
    app.run()
