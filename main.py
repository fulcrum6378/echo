import os
import struct

import matplotlib.pyplot as plot

from config import BYTES_PER_SAMPLE

pcm_path = 'aud/aud.pcm'
data: list[int] = []
with open(pcm_path, 'rb') as pcm:
    pcm.seek(384)
    for f in range(384, os.path.getsize(pcm_path), BYTES_PER_SAMPLE):
        data.append(struct.unpack('<h', pcm.read(BYTES_PER_SAMPLE))[0])
    # the initial noise isn't from the kickstart buffer! it's longer than that
    # the kickstart buffer is all zeroes, but these are loud numbers!
plot.plot(data)
plot.show()
