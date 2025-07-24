class MotherBoard:
    def __init__(self, model):
        self._model = model

class Gpu:
    def __init__(self, model):
        self._gpu = model

class Pc:
    def __init__(self, version):
        self._version = version
        self._motherboard = None
        self._gpu = None

    @property
    def motherboard(self):
        return self._motherboard
    
    @motherboard.setter
    def motherboard(self, new_mb):
        self._motherboard = new_mb

    @property
    def gpu(self):
        return self._gpu
    
    @gpu.setter
    def gpu(self, new_gpu):
        self._gpu = new_gpu

    def info(self):
        print(f'Pc {self._version}, Placa Mae: {self._motherboard._model}, Placa de video {self._gpu._gpu}')

pc1 = Pc("Dell")
pc1.motherboard = MotherBoard("Asus")
pc1.gpu = Gpu("RTX 3060ti")
pc1.info()

pc2 = Pc("Asus")
pc2.motherboard = MotherBoard("Asus")
pc2.gpu = Gpu("RTX 3050")
pc2.info()
