from threading import Lock
import time

class IServicioCorreo:
    def enviarCorreo(self, correo):
        pass

    def listarCorreos(self, inicio, fin):
        pass

    def descargarCorreo(self, infoCorreo):
        pass

class ServicioCorreo(IServicioCorreo):
    def enviarCorreo(self, correo):
        print(f"Enviando correo: {correo}")

    def listarCorreos(self, inicio, fin):
        print(f"Listando correos del {inicio} al {fin}")

    def descargarCorreo(self, infoCorreo):
        print(f"Descargando correo: {infoCorreo}")

class ServicioCorreoConReintentos(IServicioCorreo):
    def __init__(self, servicioCorreo):
        self.servicioCorreo = servicioCorreo

    def enviarCorreo(self, correo):
        for _ in range(3):
            try:
                self.servicioCorreo.enviarCorreo(correo)
                break
            except Exception:
                print("Error al enviar el correo. Reintentando...")

    def listarCorreos(self, inicio, fin):
        for _ in range(3):
            try:
                self.servicioCorreo.listarCorreos(inicio, fin)
                break
            except Exception:
                print("Error al listar los correos. Reintentando...")

    def descargarCorreo(self, infoCorreo):
        for _ in range(3):
            try:
                self.servicioCorreo.descargarCorreo(infoCorreo)
                break
            except Exception:
                print("Error al descargar el correo. Reintentando...")

class ServicioCorreoThreadSafe(IServicioCorreo):
    def __init__(self, servicioCorreo):
        self.servicioCorreo = servicioCorreo
        self.lock = Lock()

    def enviarCorreo(self, correo):
        with self.lock:
            self.servicioCorreo.enviarCorreo(correo)

    def listarCorreos(self, inicio, fin):
        with self.lock:
            self.servicioCorreo.listarCorreos(inicio, fin)

    def descargarCorreo(self, infoCorreo):
        with self.lock:
            self.servicioCorreo.descargarCorreo(infoCorreo)

class ServicioCorreoConLogging(IServicioCorreo):
    def __init__(self, servicioCorreo):
        self.servicioCorreo = servicioCorreo

    def enviarCorreo(self, correo):
        print("Iniciando envío de correo")
        self.servicioCorreo.enviarCorreo(correo)
        print("Correo enviado")

    def listarCorreos(self, inicio, fin):
        print("Iniciando listado de correos")
        self.servicioCorreo.listarCorreos(inicio, fin)
        print("Correos listados")

    def descargarCorreo(self, infoCorreo):
        print("Iniciando descarga de correo")
        self.servicioCorreo.descargarCorreo(infoCorreo)
        print("Correo descargado")

class ServicioCorreoConCache(IServicioCorreo):
    def __init__(self, servicioCorreo):
        self.servicioCorreo = servicioCorreo
        self.cache = {}

    def enviarCorreo(self, correo):
        self.servicioCorreo.enviarCorreo(correo)

    def listarCorreos(self, inicio, fin):
        if (inicio, fin) in self.cache:
            return self.cache[(inicio, fin)]
        else:
            correos = self.servicioCorreo.listarCorreos(inicio, fin)
            self.cache[(inicio, fin)] = correos
            return correos

    def descargarCorreo(self, infoCorreo):
        if infoCorreo in self.cache:
            return self.cache[infoCorreo]
        else:
            correo = self.servicioCorreo.descargarCorreo(infoCorreo)
            self.cache[infoCorreo] = correo
            return correo
