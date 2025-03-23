from models.base import Base as Base
from datetime import datetime

class Usuario(Base):
    def __init__(self, documento: str, correo: str, password: str, fecha_nac: int, direccion: str,estado_abono: bool=False, estado_verificacion: bool=False, celular: str = None, rut=None):
        super().__init__()
        self.documento = documento
        self.fecha_nac = fecha_nac
        self.direccion = direccion
        self.rut = rut
        self.celular = celular
        self.correo = correo
        # self.autenticacion = Autenticacion(self, password)
        self.estado_verificacion = estado_verificacion
        self.estado_abono = estado_abono
    
    def tiene_verificacion(self) -> bool:
        """Verifica si el usuario está verificado"""
        # return self.estado_verificacion is not None and self.estado_verificacion.verificado
    
    def tiene_abono_activo(self) -> bool:
        """Verifica si el usuario tiene un abono activo"""
        # return self.estado_abono is not None and self.estado_abono.es_valido()
    
    def iniciar_verificacion(self, **documentos):
        """Inicia el proceso de verificación del usuario"""
        # self.estado_verificacion = EstadoVerificacion(self, **documentos)
        # return self.estado_verificacion
    
    def abonar(self, plan: str, monto: float, dias: int = 30):
        """Abona al usuario con un plan específico"""
        # if not self.estado_abono:
        #     self.estado_abono = EstadoAbono(self, plan, monto, dias)
        # else:
        #     self.estado_abono.monto_abonado += monto
        #     self.estado_abono.activar(dias)
        # return self.estado_abono
