# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .CardanoPoolParametersType import CardanoPoolParametersType

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
        EnumTypeCardanoCertificateType = Literal[0, 1, 2, 3]
    except ImportError:
        pass


class CardanoTxCertificateType(p.MessageType):

    def __init__(
        self,
        *,
        type: EnumTypeCardanoCertificateType,
        path: Optional[List[int]] = None,
        pool: Optional[bytes] = None,
        pool_parameters: Optional[CardanoPoolParametersType] = None,
    ) -> None:
        self.path = path if path is not None else []
        self.type = type
        self.pool = pool
        self.pool_parameters = pool_parameters

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('type', p.EnumType("CardanoCertificateType", (0, 1, 2, 3)), p.FLAG_REQUIRED),
            2: ('path', p.UVarintType, p.FLAG_REPEATED),
            3: ('pool', p.BytesType, None),
            4: ('pool_parameters', CardanoPoolParametersType, None),
        }
