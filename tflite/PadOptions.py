# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class PadOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsPadOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = PadOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def PadOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # PadOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def PadOptionsStart(builder): builder.StartObject(0)
def PadOptionsEnd(builder): return builder.EndObject()
