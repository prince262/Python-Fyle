
import psycopg2
from flask import Flask, request
app = Flask(__name__)
conn = psycopg2.connect(database="test", user = "princepansheriya", password = "prince", host = "127.0.0.1", port = "5432")

print ("Opened database successfully")
cur = conn.cursor()
@app.route('/api/branches/autocomplete')
def hello():
    args = request.args
    print(args['q'])
    # query = 'SELECT * from branches where branch="RTGS-HO"'
    s = ""
    s += "SELECT * from branches "
    s += "WHERE"
    s += "("
    s += " branch = '" + args['q'] + "'"
    s += ")"
    print(s)  
    cur.execute(s)
    rows = cur.fetchall()
    json_data = {}
    json_data['banks'] = []
    for x in rows:
        print(x)
        json_data['banks'].append(list(x))
    print(json_data)
    return json_data


if __name__ == '__main__':
    app.run(host='localhost', port=3000)
