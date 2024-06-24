import numpy as np
import matplotlib.pyplot as plt
import Classes
import Render as ren
            
if __name__ == '__main__':           

    objects = []
    list_objects = [
    { 'center': np.array([-0.2, 0, -1]), 'radius': 0.1, 'ambient': np.array([0.1, 0, 0]), 'diffuse': np.array([0.7, 0, 0]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5 },
    { 'center': np.array([0.1, 0, 0]), 'radius': 0.1, 'ambient': np.array([0.1, 0, 0.1]), 'diffuse': np.array([0.7, 0, 0.7]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5 },
    { 'center': np.array([-0.3, 0, 0]), 'radius': 0.1, 'ambient': np.array([0, 0.1, 0]), 'diffuse': np.array([0, 0.6, 0]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5 },
    { 'center': np.array([-0.5, 0, -1]), 'radius': 0.1, 'ambient': np.array([0.1, 0, 0]), 'diffuse': np.array([0.7, 0, 0]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5 },
    { 'center': np.array([0.3, 0, 0]), 'radius': 0.1, 'ambient': np.array([0.1, 0, 0.1]), 'diffuse': np.array([0.7, 0, 0.7]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5 },
    { 'center': np.array([-0.8, 0, 0]), 'radius': 0.1, 'ambient': np.array([0, 0.1, 0]), 'diffuse': np.array([0, 0.6, 0]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5 },    
    { 'center': np.array([0.1, 0.2, -0.5]), 'radius': 0.1, 'ambient': np.array([0.05, 0.01, 0.1]), 'diffuse': np.array([0.4, 0.1, 0.6]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5 },
    { 'center': np.array([-0.4, 0.3, 0.2]), 'radius': 0.1, 'ambient': np.array([0.05, 0.1, 0.02]), 'diffuse': np.array([0.3, 0.5, 0.2]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5 },
    { 'center': np.array([0.2, -0.2, -0.3]), 'radius': 0.1, 'ambient': np.array([0.1, 0.05, 0.02]), 'diffuse': np.array([0.6, 0.2, 0.1]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5 },
    { 'center': np.array([-0.6, 0.1, -0.4]), 'radius': 0.1, 'ambient': np.array([0.02, 0.05, 0.1]), 'diffuse': np.array([0.2, 0.4, 0.5]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5 },
    { 'center': np.array([0.3, -0.1, 0.3]), 'radius': 0.1, 'ambient': np.array([0.1, 0.05, 0.05]), 'diffuse': np.array([0.5, 0.3, 0.2]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5 },
    { 'center': np.array([-0.5, -0.2, 0.1]), 'radius': 0.1, 'ambient': np.array([0.02, 0.1, 0.1]), 'diffuse': np.array([0.1, 0.6, 0.7]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5 },
    { 'center': np.array([0.4, 0.1, -0.6]), 'radius': 0.1, 'ambient': np.array([0.1, 0.05, 0.05]), 'diffuse': np.array([0.7, 0.2, 0.4]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5 },
    { 'center': np.array([-0.3, 0.4, 0.2]), 'radius': 0.1, 'ambient': np.array([0.05, 0.1, 0.1]), 'diffuse': np.array([0.3, 0.4, 0.7]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5 },
    { 'center': np.array([0.2, -0.4, 0.5]), 'radius': 0.1, 'ambient': np.array([0.05, 0.05, 0.1]), 'diffuse': np.array([0.2, 0.3, 0.6]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5 },
    { 'center': np.array([-0.2, 0.5, -0.1]), 'radius': 0.1, 'ambient': np.array([0.1, 0.1, 0.05]), 'diffuse': np.array([0.6, 0.5, 0.1]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5 },
    { 'center': np.array([0, -9000, 0]), 'radius': 9000 - 0.7, 'ambient': np.array([0.1, 0.1, 0.1]), 'diffuse': np.array([0.6, 0.6, 0.6]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0 },
    ]

    for item in list_objects:
        obj = Classes.Sphere(item['radius'], item['center'], item['ambient'],item['diffuse'],item['specular'],item['shininess'],item['reflection'])
        objects.append(obj)

    Camera = Classes.camera(np.array([0, 0.1, 1]), 1920,1080)

    light = Classes.Light(position=np.array([5, 5, 5]), ambient=np.array([1, 1, 1]) , diffuse= np.array([1, 1, 1]), specular=np.array([1, 1, 1]))
    
    light2 = Classes.Light(position=np.array([-5, 10, 10]), ambient=np.array([1, 1, 1]) , diffuse= np.array([1, 1, 1]), specular=np.array([1, 1, 1]))
    
    lights = [light]

    #Render sequencial
    #Render = ren.render_seq(Camera, lights , objects)
    #t, image = Render.render()
    
    #Render Concorrente
    Render = ren.render_conc(Camera, lights , objects)
    t, image = Render.render(8)
    
    plt.imsave("Res1080.png", image)