# encoding: utf-8
"""

"""
__author__ = 'Richard Smith'
__date__ = '29 Mar 2019'
__copyright__ = 'Copyright 2018 United Kingdom Research and Innovation'
__license__ = 'BSD - see LICENSE file in top-level package directory'
__contact__ = 'richard.d.smith@stfc.ac.uk'

import os
from pydub import AudioSegment
from random import randint
from math import floor
from pydub.exceptions import CouldntDecodeError


# Segement length in miliseconds
seg_size = 4000

# List files
files = os.listdir('input')

# loop files
for file in files:

    # Get filename
    filename, ext = os.path.splitext(file)[0:2]

    # Load song
    try:
        song = AudioSegment.from_file(f'input/{file}', format=ext[1:])
    except CouldntDecodeError:
        print(f'Error Decoding {file}')
        print('Ignoring...')
        continue

    # Select a random segment
    number_of_segs = floor(len(song)/seg_size)

    rand_seg_int = randint(1,number_of_segs-1)

    chunk = song[rand_seg_int*seg_size:(rand_seg_int+1)*seg_size]

    silence = AudioSegment.silent(duration=seg_size)

    output = chunk + silence

    # Export to file
    with open(f'output/{filename}_clip.mp3', 'wb') as writer:
        output.export(writer, format='mp3')
