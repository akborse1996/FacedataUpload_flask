from flask import Flask,render_template

from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator
cluster = Cluster('couchbase://localhost:8091')
authenticator = PasswordAuthenticator('Admin', 'Amol@1996')
cluster.authenticate(authenticator)
cb = cluster.open_bucket('MyBucket')
app = Flask(__name__,template_folder='template')

@app.route("/")
def index():
    
    cb.upsert('12', {'DockingID': 'C2', 'ClientName':'pear',
                     'ClientID':'Jon2','CustomerName':'Alex2','CustomerID':'asas1902','Expression':'Smile2','Probability':8.6,'DateTime': '2019-10-03T15:10:05.999'})
    cb.upsert('13', {'DockingID': 'C3', 'ClientName':'pear',
                     'ClientID':'Jon2','CustomerName':'Alex2','CustomerID':'asas1902','Expression':'Smile2','Probability':8.7,'DateTime': '2019-10-03T15:10:05.99'})
  
# OperationResult<RC=0x0, Key=u'u:king_arthur', CAS=0xb1da029b0000>
   
    
# {u'interests': [u'Holy Grail', u'African Swallows'], u'name': u'Arthur', u'email': u'kingarthur@couchbase.com'}
## The CREATE PRIMARY INDEX step is only needed the first time you run this script
    from couchbase.n1ql import N1QLQuery
    row_iter = cb.n1ql_query(N1QLQuery('SELECT DockingID,ClientName,ClientID,CustomerName,CustomerID,Expression,Probability,DateTime FROM MyBucket' ))
    l=[]
    for row in row_iter: 
        l.append(row)
        print(l)
    
    return render_template('data.html',result=l)

if __name__ == "__main__":
	app.run(debug=True)
    

