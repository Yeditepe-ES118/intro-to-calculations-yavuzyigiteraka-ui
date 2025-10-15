import numpy as np

def surface_area(pi_app): 
    a = 6378.137 # in km
    c = 6356.752314245 # in km
    e = np.sqrt(1-c**2/a**2)
    s = 2*pi_app*a**2*(1+(1-e**2)/e*np.arctanh(e))
    return s
myresult = surface_area(3.14)

def compute_error(pi_app1,pi_app2): 
    s_1 = surface_area(pi_app1)
    s_2 = surface_area(pi_app2)
    error = np.abs(s_1-s_2)/s_2*100 # in %
    return error
myresult = compute_error(3.14,3.1415)