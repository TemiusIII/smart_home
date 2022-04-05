from wit import Wit

client = Wit('FWPSOGS7KEV4MO4G32CU5ROCLMERI5EM')
with open('myspeech.ogg', 'rb') as f:
    print(f)
    resp = client.post_speech(f, content_type='audio/ogg')

print('Yay, got Wit.ai response: ' + str(resp))