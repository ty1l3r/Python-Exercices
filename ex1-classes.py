import math

# Crée une classe Point qui a deux attributs, x et y, représentant les coordonnées d'un point dans l'espace. 
# Ajoute une méthode distance qui calcule la distance euclidienne entre deux points.


class Point:
    def __init__(self, a, b):
        self.point_a = a
        self.point_b = b
        
    def distance(self):
        #fonction math.isqrt(n)
        result = math.isqrt( ((2*self.point_a) - (self.point_a) **2) + ((self.point_b*2 - self.point_b) **2) )
        return result


#instance de la classe Point
ex1 = Point(6,7)
#appel de la méthode
distance_result = ex1.distance()
print(distance_result)
    