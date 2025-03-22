
from models.usuario import Usuario as Usuario

class Subastador(Usuario):
    def __init__(self, documento: str, correo: str, password: str, 
                 matricula: str = None, razon_social: str = None, **kwargs):
        super().__init__(documento, correo, password, **kwargs)
        self.matricula = matricula
        self.razon_social = razon_social
        self.matricula_activa = False
    
    def validar_matricula(self) -> bool:
        """Valida si la matrícula del subastador está activa"""
        # Aquí iría la lógica de validación
        return self.matricula_activa
    
    def activar_matricula(self):
        """Activa la matrícula del subastador"""
        self.matricula_activa = True