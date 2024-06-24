import numpy as np
import matplotlib.pyplot as plt
import Classes
import Render as ren
import time as tm


def aceleracao(times, seq):
    aceler = []
    
    for t in times:
        aceler.append(seq / t)
        
    return aceler
    
def eficacia(ace, n_proc):
    efi = []

    for a in ace:
        efi.append(a / n_proc)
        
    return efi   


def bar_tempos(times, seq_time):
    processos = ["Sequencial", "2 Processos", "4 Processos", "6 Processos", "8 Processos"]
    color = ['b', 'r', 'g', 'm', 'y']
    resolucoes = ["640x480", "1280x720", "1920x1080", "2560x1440"]
    
    
    
    for i, t in enumerate(times):
        t.insert(0, seq_time[i])
        plt.figure(figsize=(10, 6))
        plt.bar(processos, t, color=color[i])

        # Adicionar título e rótulos
        plt.title('Comparação de Tempos Medidos ' + resolucoes[i])
        plt.xlabel('Processos')
        plt.ylabel('Tempo Medido (s)')

        plt.savefig('graficos/'+ resolucoes[i]+'.png')
    
def grafico_acel(times, time_seq, n_proce, num_processos):
    
    color = ['b', 'r', 'g', 'm', 'y']
    resolucoes = ["640x480", "1280x720", "1920x1080", "2560x1440"]
    
    
    plt.figure(figsize=(14, 6))
    for i, t in enumerate(times):
        acele = aceleracao(t, time_seq[i])
        
        
        plt.plot(num_processos, acele, marker='o', linestyle='-', color=color[i], label=resolucoes[i])
        
    
    

    plt.title('Aceleração vs. Número de Processos')
    plt.xlabel('Número de Processos')
    plt.ylabel('Aceleração')
    plt.legend()
    plt.grid(True)

    
    plt.tight_layout()

    
    plt.savefig('graficos/aceleração.png')
    
    
def grafico_efic(times, time_seq, n_proce, num_processos):
    
    color = ['b', 'r', 'g', 'm', 'y']
    resolucoes = ["640x480", "1280x720", "1920x1080", "2560x1440"]
    
    
    plt.figure(figsize=(14, 6))
    
    for i, t in enumerate(times):
        acele = aceleracao(t, time_seq[i])
        efic = eficacia(acele, n_proce)
        
        plt.plot(num_processos, efic, marker='o', linestyle='-', color=color[i], label=resolucoes[i])
        
    
    
    plt.title('Eficiência vs. Número de Processos')
    plt.xlabel('Número de Processos')
    plt.ylabel('Eficiência')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    
    plt.savefig('graficos/eficiencia.png')
    


if __name__ == '__main__':           

    
    #Tempos coletados ao rodar o programa
    todos_tempos =[[21.493437719345092, 12.656458282470703, 9.302990579605103, 7.687714099884033], [58.21717023849487, 31.312203693389893, 23.5157377243042, 19.69504084587097], [129.54552440643312, 69.4279420375824, 52.14641647338867, 43.875870656967166],[248.41698060035705, 132.5807737827301, 99.64001355171203, 83.57987804412842]]
    time_seq = [28.524275827407838, 80.55799536705017, 182.72899947166442, 344.2727399349213]
    qtd_processos = qtd_processos = [2, 4, 6, 8]
    
    grafico_acel(todos_tempos, time_seq, 6, qtd_processos)
    grafico_efic(todos_tempos, time_seq, 6, qtd_processos)
    bar_tempos(todos_tempos, time_seq)