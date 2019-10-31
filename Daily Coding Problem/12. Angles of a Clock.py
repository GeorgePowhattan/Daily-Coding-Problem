'''Hi, here's your problem today. This problem was recently asked by Microsoft:

Given a time in the format of hour and minute, calculate the angle of the hour and minute hand on a clock.'''

def calcAngle(h, m):
    if h > 12 or m > 60 or h < 0 or m < 0:
        print('Invalid time format')
    angle = abs((h+m/60) - (m/60)*12) / 12*360 
    return min(angle, 360-angle)

print (calcAngle(3, 30))
# 75
print (calcAngle(12, 30))
# 165