import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as mp
import time



def normalize(vector):

    return vector / np.linalg.norm(vector)   
 
def nearest_object(objects, origin, direction):
    distances = [obj.intersect(origin, direction) for obj in objects]
    
    nearest_object = None
    min_dist = np.inf
    for index, distance in enumerate(distances):
        if distance and distance < min_dist:
            min_dist = distance
            nearest_object = objects[index]
    return nearest_object, min_dist

def reflected(vector, axis):
    return vector - 2 * np.dot(vector, axis) * axis

def calculate_color(objects, origin, direction, camera, max_depth, lights):
    color = np.zeros((3)) 
    reflection = 1
    
    for k in range(max_depth):
        object, min_distance = nearest_object(objects, origin, direction)
        if object is None:
            break
        
        intersection = origin + min_distance * direction
        normal_to_surface = normalize(intersection - object.center)
        shifted_point = intersection + 1e-5 * normal_to_surface
        
        for light in lights:
            inter_light_point = normalize(light.position - shifted_point)
            is_shadowed = False
            for o in objects:
                if o.intersect(shifted_point, inter_light_point):
                    is_shadowed = True
                    break
            
            if is_shadowed:
                continue
            
            intersection_to_light = normalize(light.position - shifted_point)

            _, min_distance = nearest_object(objects, shifted_point, intersection_to_light)
            intersection_to_light_distance = np.linalg.norm(light.position - intersection)
            is_shadowed = min_distance < intersection_to_light_distance
            
            # RGB
            illumination = np.zeros((3))

            # ambiant
            illumination += object.ambient * light.ambient

            # diffuse
            illumination += object.diffuse * light.diffuse * np.dot(intersection_to_light, normal_to_surface)

            # specular
            intersection_to_camera = normalize(camera - intersection)
            H = normalize(intersection_to_light + intersection_to_camera)
            illumination += object.specular * light.specular * np.dot(normal_to_surface, H) ** (object.shininess / 4)
            
            # reflection
            color += reflection * illumination
           
        reflection *= object.reflection

        origin = shifted_point
        direction = reflected(direction, normal_to_surface)
            
    return color

def worker(screen, camera, objects, lights, size, idProcess, xVector, yVector, return_dict, extra = 0):
    image = np.zeros((size + extra, screen.width, 3))
    
    
    
    for i in range(size + extra):
        for j in range(screen.width):
            pixel = screen.topLeft + xVector * j + yVector * (i + ((size) * idProcess))
            direction = normalize(pixel - camera.position)
            origin = camera.position
            color = calculate_color(objects, origin, direction, camera.position, 3, lights)
            image[i][j] = np.clip(color, 0, 1)
            
    return_dict[idProcess] = image
            
class render_seq:
    def __init__(self, camera, lights, objects):
        self.camera = camera
        self.lights = lights
        self.objects = objects
    
    def render(self):
        screen = self.camera.screen
        image = np.zeros((screen.height, screen.width, 3))
        
        xVector = (screen.topRight - screen.topLeft) * (1 / screen.width)
        yVector = (screen.bottomLeft - screen.topLeft) * (1 / screen.height)
        
        start = time.time()
        for i in range(screen.height):
            for j in range(screen.width):
                pixel = screen.topLeft + xVector * j + yVector * i
                direction = normalize(pixel - self.camera.position)
                origin = self.camera.position
                color = calculate_color(self.objects, origin, direction, self.camera.position, 3, self.lights)
                image[i][j] = np.clip(color, 0, 1)
        
        end = time.time()
        total = end - start
        
        return total, image

class render_conc:
    def __init__(self, camera, lights, objects):
        self.camera = camera
        self.lights = lights
        self.objects = objects
    
    def join_image(self, dict):
        n = len(dict)
        img = []
        
        for i in range(n):
            img.append(dict.get(i))
          
        image = np.concatenate(img, axis=0)
                    
        return image
    
    def render(self, numProcess):
        screen = self.camera.screen
        
        xVector = (screen.topRight - screen.topLeft) * (1 / screen.width)
        yVector = (screen.bottomLeft - screen.topLeft) * (1 / screen.height)
        
        start = time.time()
        manager = mp.Manager()
        return_dict = manager.dict()
        jobs = []
        size = int(screen.height / numProcess) 
        
        
        for i in range(numProcess):
            if ((i+1) == numProcess):
                p = mp.Process(target=worker, args=(screen, self.camera, self.objects, self.lights, size, i, xVector, yVector, return_dict, (screen.height % numProcess)))
            else:
                p = mp.Process(target=worker, args=(screen, self.camera, self.objects, self.lights, size, i, xVector, yVector, return_dict))
            jobs.append(p)
            p.start()
        
        
        for proc in jobs:
            proc.join()  
        
        image = self.join_image(return_dict)
        
        end = time.time()
        
        total = end - start
        
        return total, image