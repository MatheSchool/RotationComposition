import numpy as np
import math


a = np.matrix([[math.sqrt(3)/2, -1/2], [1/2, math.sqrt(3)/2]]);
b = np.matrix([[math.sqrt(2)/2, math.sqrt(2)/2], [-math.sqrt(2)/2, math.sqrt(2)/2]]);

print (a);
print (b);

print (a*b);
print (b*a);

da = np.linalg.det(a);

print(da);

db = np.linalg.det(b);

print(db);

dab = np.linalg.det(a * b);

print(dab);

dba = np.linalg.det(b * a);

print (dba);