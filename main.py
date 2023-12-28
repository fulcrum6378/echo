import os
import struct

import matplotlib.pyplot as plot

from config import BYTES_PER_SAMPLE

pcm_path = 'aud/1.pcm'
data: list[int] = []
decreasing = False
prv: int = 0
waves: list[list[int]] = []
this_wave: list[int] = []
wavelengths: dict[int, int] = {}
with open(pcm_path, 'rb') as pcm:
    for f in range(0, os.path.getsize(pcm_path), BYTES_PER_SAMPLE):
        value: int = struct.unpack('<h', pcm.read(BYTES_PER_SAMPLE))[0]
        if not decreasing and value < prv:
            decreasing = True
        elif decreasing and value > prv:
            waves.append(this_wave)
            wavelength = len(this_wave)
            if wavelength not in wavelengths:
                wavelengths[wavelength] = 1
            else:
                wavelengths[wavelength] += 1
            this_wave = []
            decreasing = False
        prv = value
        data.append(value)
        this_wave.append(value)
plot.plot(data)
plot.show()
print('Total', len(data), 'samples.')
print('Total', len(waves), 'waves.')
print('Wavelengths:', wavelengths)
# {2: 8247,
#  3: 19306,
#  4: 5555,
#  5: 1592,
#  6: 358,
#  7: 79,
#  8: 19,
#  9: 7,
#  10: 2,
#  11: 1,
#  1385: 1}

# analyse waves
for w in waves:
    pass
