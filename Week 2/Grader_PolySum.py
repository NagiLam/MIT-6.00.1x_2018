""" Week 2 - Polysum
A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is: 
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s. 
This function should sum the area and square of the perimeter of the regular polygon. 
The function returns the sum, rounded to 4 decimal places.

"""

def polysum(n, s):
    """
    This function sum the area and square of the perimeter of the regular polygon. 
    The function returns the sum, rounded to 4 decimal places.
    """
    import math
    
    area = ( 0.25*n*s**2 / (math.tan((math.pi) / n)) )
    sum = area + (s*n)**2
    
    return round(sum,4)
