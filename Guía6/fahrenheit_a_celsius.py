#problema fahrenheit_a_celsius (in t: R) : R {
#requiere: {True}
#asegura: {res = ((t − 32) × 5)/9}
#}

def fahrenheit_a_celsius (t:float) -> float:
    return (((t-32) * 5 )/9)

print (fahrenheit_a_celsius (273))