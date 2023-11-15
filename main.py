import os
import struct

import matplotlib.pyplot as plot

from config import BYTES_PER_SAMPLE

pcm_path = 'aud/1.pcm'
data: list[int] = []
with open(pcm_path, 'rb') as pcm:
    for f in range(0, os.path.getsize(pcm_path), BYTES_PER_SAMPLE):
        data.append(struct.unpack('<h', pcm.read(BYTES_PER_SAMPLE))[0])
plot.plot(data)
plot.show()
