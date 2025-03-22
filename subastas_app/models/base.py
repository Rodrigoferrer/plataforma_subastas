
from datetime import uuid, uuid4

"""
Class Base,
father class,
all models inherits from it

"""


class Base:
    def __init__(self):
        self.uuid = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self) -> Dict[str, Any]:
        """Convierte la instancia a un diccionario para serialización"""
        return {
            'uuid': self.uuid,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
