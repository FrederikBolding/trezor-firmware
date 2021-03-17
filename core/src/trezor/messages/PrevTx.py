# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class PrevTx(p.MessageType):

    def __init__(
        self,
        *,
        version: int,
        lock_time: int,
        inputs_count: int,
        outputs_count: int,
        extra_data_len: int = 0,
        expiry: Optional[int] = None,
        version_group_id: Optional[int] = None,
        timestamp: Optional[int] = None,
        branch_id: Optional[int] = None,
    ) -> None:
        self.version = version
        self.lock_time = lock_time
        self.inputs_count = inputs_count
        self.outputs_count = outputs_count
        self.extra_data_len = extra_data_len
        self.expiry = expiry
        self.version_group_id = version_group_id
        self.timestamp = timestamp
        self.branch_id = branch_id

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('version', p.UVarintType, p.FLAG_REQUIRED),
            4: ('lock_time', p.UVarintType, p.FLAG_REQUIRED),
            6: ('inputs_count', p.UVarintType, p.FLAG_REQUIRED),
            7: ('outputs_count', p.UVarintType, p.FLAG_REQUIRED),
            9: ('extra_data_len', p.UVarintType, 0),  # default=0
            10: ('expiry', p.UVarintType, None),
            12: ('version_group_id', p.UVarintType, None),
            13: ('timestamp', p.UVarintType, None),
            14: ('branch_id', p.UVarintType, None),
        }
