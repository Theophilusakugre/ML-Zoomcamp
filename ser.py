import bentoml
import numpy as np
from bentoml.io import JSON
from bentoml.io import NumpyNdarray
#from pydantic import BaseModel
#class UserProfile(BaseModel):
 #   name :str
 #   age : int
  #  country : str
   # rating :float
    


model_ref= bentoml.sklearn.get("mlzoomcamp_homework:jsi67fslz6txydu5")
#dv=model_ref.custom_objects['dictVectorizer']

model_runner=model_ref.to_runner()

svc = bentoml.Service("credit_risk_classifier",runners=[model_runner])
@svc.api(input=NumpyNdarray(shape=(-1,4),enforce_shape=True,dtype=np.float32),output=JSON())
def classify(vector):
    #application_data=CreditApplication.dict()
    #vector = dv.transform(application_data)
    prediction=model_runner.predict.run(vector)
    print(prediction)

    result=prediction[0]
    if result >0.5:
        return {'status':'Declined'}
    elif result>0.23:
        return {'status':'Maybe'}
    else:
        return {"status":"Approved"}
