# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class StellarSignedTx(p.MessageType):
    MESSAGE_WIRE_TYPE = 230

    def __init__(
        self,
        *,
        public_key: bytes,
        signature: bytes,
    ) -> None:
        self.public_key = public_key
        self.signature = signature

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('public_key', p.BytesType, p.FLAG_REQUIRED),
            2: ('signature', p.BytesType, p.FLAG_REQUIRED),
        }
