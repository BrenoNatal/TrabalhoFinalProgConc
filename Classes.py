import numpy as np

class screen:
    def __init__(self, topLeft, topRight, bottomLeft, width, height):
        self.topLeft = topLeft
        self.topRight= topRight
        self.bottomLeft = bottomLeft
        self.width = width
        self.height = height
    
class camera:
    def __init__(self, position, width, height):
        self.position = position
        self.width = width
        self.height = height
        ratio = width / height
        self.screen = screen(np.array([-1, 1 / ratio, 0]), np.array([1, 1 / ratio, 0]), np.array([-1, -1 / ratio, 0]), width, height)
        
class Light:
    def __init__(self, position, ambient, diffuse, specular):
        self.position = position
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular   
        
class Sphere:
    def __init__(self, radius, center, ambient, diffuse, specular, shininess, reflection):
        self.radius = radius
        self.center = center
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess
        self.reflection = reflection
    
    #Funcao para calcular a interseccao entre o objeto e um de luz dado a origem do raio e direcao dele
    def intersect(self,origin, direction):
        b = 2 * np.dot(direction, origin - self.center)
        c = np.linalg.norm(origin - self.center) ** 2 - self.radius ** 2
        delta = b ** 2 - 4 * c
        if delta > 0:
            t1 = (-b + np.sqrt(delta)) / 2
            t2 = (-b - np.sqrt(delta)) / 2
            if t1 > 0 and t2 > 0:
                return min(t1, t2)
        return None
    
        
