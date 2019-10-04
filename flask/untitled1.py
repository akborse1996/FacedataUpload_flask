# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 16:38:33 2019

@author: amol.borse
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 12:25:50 2019

@author: amol.borse
"""
from flask import Flask

app=Flask(_name_)
@app.rout('/')

from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator
cluster = Cluster('couchbase://localhost:8091')
authenticator = PasswordAuthenticator('Admin', 'Amol@1996')
cluster.authenticate(authenticator)
cb = cluster.open_bucket('MyBucket')


rv = cb.get('11', quiet=True)
if rv.success:
    print(rv.value)    
else:
    print ("Item not found")
    
    cb.upsert('C1', {'DateTime': '2019-10-3', 'DockingID': 'C1', 'Client Name':'pear',
                     'Client ID':'Jon','Customer name':'Alex','Customer ID':'asas','Expression':'smile','Probability':8.5})
    cb.upsert('C2', {'DateTime': '2019-10-3', 'DockingID': 'C1', 'Client Name':'pear',
                     'Client ID':'Jon','Customer name':'Alex','Customer ID':'asas','Expression':'smile','Probability':9.4})
    cb.upsert('C3', {'DateTime': '2019-10-3', 'DockingID': 'C1', 'Client Name':'pear',
                     'Client ID':'Jon','Customer name':'Amo','Customer ID':'asas','Expression':'normal','Probability':4.5})
   