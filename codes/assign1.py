import numpy as np
#given two lines
a= np.array([[4,7],[2,-3]])
b=np.array([3,-1])
inv_a= np.linalg.inv(a)
X=inv_a.dot(b)
print("point of intersection is x:{} , y:{}".format(X[0],X[1]))
#As the line has equal intercepts
print("Req line equation passing through the point of intersection is  is x+y={}".format(X[0]+X[1]))
