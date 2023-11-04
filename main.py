import os
import struct

from config import BITS_PER_SAMPLE

pcm_path = 'aud/aud.pcm'
data: list[int] = []
with open(pcm_path, 'rb') as pcm:
    for f in range(0, os.path.getsize(pcm_path), BITS_PER_SAMPLE):
        data.append(struct.unpack('<H', pcm.read(BITS_PER_SAMPLE))[0])
        # if len(data) > 1000: break
        if data[int(f / BITS_PER_SAMPLE)] != 0: break
print(data)
print('RECORD_DEVICE_KICKSTART(2):', (len(data) - BITS_PER_SAMPLE) * 2, 'bytes')
