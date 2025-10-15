import numpy as np

def surface_area(pi_app): 
    a = 6378.137 # in km
    c = 6356.752314245 # in km
    e = np.sqrt(1-c**2/a**2)
    s = 2*pi_app*a**2*(1+(1-e**2)/e*np.arctanh(e))
    return s
myresult = surface_area(3.14)