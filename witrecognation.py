import sounddevice as sd
from scipy.io.wavfile import write
import soundfile as sf
from wit import Wit

fs = 44100
seconds = 10
client = Wit('XXXXXXXX')


myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()
print("приветолцвоагцрашщоцшщощ")
write('output.wav', fs, myrecording)

data, samplerate = sf.read('output.wav')
sf.write('schitat.ogg', data, samplerate)


with open('schitat.ogg', 'rb') as f:
    print(f)
    resp = client.post_speech(f, content_type='audio/ogg')

print(resp)