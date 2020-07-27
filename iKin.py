import math

def calcAngle(ctheta):
    res1 = math.atan2(math.sqrt(1-math.pow(ctheta,2)), ctheta)
    res2 = math.atan2(math.sqrt(1-math.pow(ctheta,2))*(-1), ctheta) 
        
    return (res1, res2)
def calcAngle2(ctheta2,stheta2) :
    ctheta1 = (px * (l1 + l2 * ctheta2) + (py *l2 *stheta2)) / (px**2 + py**2)
    stheta1 = (py * (l1 + l2 * ctheta2) -  (px *l2 *(stheta2))) / (px**2 + py**2)
    return math.atan2(stheta1,ctheta1)

px = float(input("px:"))
py = float(input("py:"))
l1 = float(input("l1:"))
l2 = float(input("l2:"))
        
ctheta2 = (px**2 + py**2 - l1**2 - l2**2) / (2 *l1 * l2)
stheta2 = math.sqrt(1-math.pow(ctheta2, 2))

theta2a,theta2b = calcAngle(ctheta2)
theta1a = calcAngle2(ctheta2,stheta2)
theta1b = calcAngle2(ctheta2,-stheta2)
        
        
print("theta1: {} and {}".format(math.degrees(theta1a),math.degrees(theta1b)))
print("theta2: {} and {}".format(math.degrees(theta2a),math.degrees(theta2b)))