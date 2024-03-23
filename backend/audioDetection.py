from resemblyzer import VoiceEncoder, preprocess_wav
from pathlib import Path
import numpy as np

def audioDetection1():

    fpath = Path('null')
    wav = preprocess_wav(fpath)

    encoder = VoiceEncoder()
    embed = encoder.embed_utterance(wav)
    np.set_printoptions(precision=3, suppress=True)

    return (embed)
