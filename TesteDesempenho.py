import numpy as np
import matplotlib.pyplot as plt
import Classes
import Render as ren
import time as tm

#Codigo para gerar os tempos para analisar a perfomace do programa

if __name__ == '__main__':           

    objects = []
    list_objects = [
    { 'center': np.array([-0.2, 0, -1]), 'radius': 0.7, 'ambient': np.array([0.1, 0, 0]), 'diffuse': np.array([0.7, 0, 0]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5 },
    { 'center': np.array([0.1, -0.3, 0]), 'radius': 0.1, 'ambient': np.array([0.1, 0, 0.1]), 'diffuse': np.array([0.7, 0, 0.7]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5 },
    { 'center': np.array([-0.3, 0, 0]), 'radius': 0.15, 'ambient': np.array([0, 0.1, 0]), 'diffuse': np.array([0, 0.6, 0]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5 },
    { 'center': np.array([0, -9000, 0]), 'radius': 9000 - 0.7, 'ambient': np.array([0.1, 0.1, 0.1]), 'diffuse': np.array([0.6, 0.6, 0.6]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0 },
    ]

    for item in list_objects:
        obj = Classes.Sphere(item['radius'], item['center'], item['ambient'],item['diffuse'],item['specular'],item['shininess'],item['reflection'])
        objects.append(obj)

    light = Classes.Light(position=np.array([5, 5, 5]), ambient=np.array([1, 1, 1]) , diffuse= np.array([1, 1, 1]), specular=np.array([1, 1, 1]))
    
    light2 = Classes.Light(position=np.array([-5, 10, 10]), ambient=np.array([1, 1, 1]) , diffuse= np.array([1, 1, 1]), specular=np.array([1, 1, 1]))
    
    lights = [light]

    resolucoes = [ [640, 480], [1280, 720], [1920, 1080], [2560, 1440]]

    todos_tempos = []
    time_seq = []
    
    for res in resolucoes:
        width = res[0]
        height = res[1]
        
        Camera = Classes.camera(np.array([0, 0.1, 1]), width,height)
        Render_seq = ren.render_seq(Camera, lights , objects)
        Render_conc = ren.render_conc(Camera, lights , objects)
        times = []
        tempos = []
        seq_time = []
        
        for i in range(5):
            time, image = Render_seq.render()
            seq_time.append(time)
            #plt.imsave(str(tm.time()) + ".png", image)
            
        time_seq.append(np.mean(seq_time))
        
        for i in range(5):
            time, image = Render_conc.render("conc_image1", 2)
            times.append(time)
            #plt.imsave(str(tm.time()) + ".png", image)
        
        tempos.append(np.mean(times))
        times = []
        
        for i in range(5):
            time, image = Render_conc.render("conc_image1", 4)
            times.append(time)
            #plt.imsave(str(tm.time()) + ".png", image)
            
            
        tempos.append(np.mean(times))
        times = []
        
        for i in range(5):
            time, image = Render_conc.render("conc_image1", 6)
            times.append(time)
            #plt.imsave(str(tm.time()) + ".png", image)
            
        tempos.append(np.mean(times))
        times = []
        
        for i in range(5):
            time, image = Render_conc.render("conc_image1", 8)
            times.append(time)
            #plt.imsave(str(tm.time()) + ".png", image)
        
        tempos.append(np.mean(times))
        
        todos_tempos.append(tempos)
    
    
    qtd_processos = [2, 4, 6, 8]
    
    print(todos_tempos)
    print(time_seq)