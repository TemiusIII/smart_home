from wit import Wit

client = Wit('XXXXXXXX')
with open('myspeech.ogg', 'rb') as f:
    print(f)
    resp = client.post_speech(f, content_type='audio/ogg')

print('Yay, got Wit.ai response: ' + str(resp))
