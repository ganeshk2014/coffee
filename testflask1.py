#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask
import pickle
app = Flask(__name__)
@app.route('/croute/<int:i1>/<int:i2>/<int:i3>')
def croute(i1,i2,i3):
    model=pickle.load(open('coffee.pkl','rb'))
    out=model.predict([[i1,i2,i3]])
    return str(out[0])
    
if __name__ =='__main__':
    app.run(debug=True)


# In[ ]:




