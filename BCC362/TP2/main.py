#fron internet

import time
import random
from multiprocessing import Process, Value, Array

class Processo(Process):
    def __init__(self, process_id, num_processos, lider):
        super(Processo, self).__init__()
        self.process_id = process_id  # Renomeando o atributo para process_id
        self.num_processos = num_processos
        self.lider = lider
        self.status = Value('i', 1)
        self.coordenador = Value('i', -1)
        self.ultima_resposta = Value('d', time.time())
        
    def run(self):
        while self.status.value == 1:
            if self.coordenador.value == -1:
                self.realizar_eleicao()
            elif time.time() - self.ultima_resposta.value > 3:
                print("Processo {} está inativo. Iniciando nova eleição.".format(self.process_id))
                self.coordenador.value = -1

    def realizar_eleicao(self):
        for i in range(self.process_id + 1, self.num_processos):
            if self.status.value == 0:
                return
            print("Processo {} enviou mensagem eleição para processo {}.".format(self.process_id, i))
            self.ultima_resposta.value = time.time()
            if random.random() < 0.5:
                print("Processo {} respondeu ao processo {}.".format(i, self.process_id))
                self.coordenador.value = i

        if self.coordenador.value == -1:
            self.eleger_coordenador()
    
    def eleger_coordenador(self):
        self.coordenador.value = self.process_id
        print("Processo {} se elegeu como coordenador.".format(self.process_id))
        for i in range(self.num_processos):
            if i != self.process_id:
                print("Processo {} enviou mensagem coord para processo {}.".format(self.process_id, i))
                self.ultima_resposta.value = time.time()
        
    def encerrar(self):
        self.status.value = 0
        self.join()

if __name__ == "__main__":
    num_processos = 5
    lider = random.randint(0, num_processos-1)
    processos = []
    
    for i in range(num_processos):
        p = Processo(i, num_processos, lider)
        p.start()
        processos.append(p)

    time.sleep(10)

    for p in processos:
        p.encerrar()
