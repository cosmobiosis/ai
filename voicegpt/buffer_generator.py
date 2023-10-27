import numpy as np
import uuid
from typing import Type

class BufferGenerator:
    def __init__(self):
        pass

    def generator_for_one_trunk(self, binary_buffer):
        """Generator that wraps binary buffer in a generator
            Args:
                binary_buffer: bytestring
            Returns:
                yielded binary_buffer: yielded bytestring
        """
        yield binary_buffer