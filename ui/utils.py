import random

def generate_random_color():
    r = random.randint(50, 255) 
    g = random.randint(50, 255)  
    b = random.randint(0, 255) 
    return (r, g, b)
