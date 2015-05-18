import hashlib

def rc4_ksa(key):
	key_length = len(key)
	key = bytearray(key)
	S = list(range(256))
	j = 0
	for i in range(256):
		j = (j + S[i] + key[i % key_length]) % 256
		S[i], S[j] = S[j], S[i]
	return S
	
class rc4_stream:
	def __init__(self, key, discard=1024):
		self.S0 = rc4_ksa(key) 
		self.S = list(self.S0)
		self.i = 0
		self.j = 0
		self.getNextN(discard) # throw out the first entries
		
	def reset(self, discard=1024):
		self.S = list(self.S0)
		self.i = 0
		self.j = 0
		self.getNextN(discard) # throw out the first entries
	
	def getNext(self):
		self.i = (self.i + 1) % 256
		self.j = (self.j + self.S[self.i]) % 256
		self.S[self.i], self.S[self.j] = self.S[self.j], self.S[self.i]
		return self.S[(self.S[self.i] + self.S[self.j]) % 256]
		
	def getNextN(self, n):
		return [self.getNext() for k in range(n)]
		
		
def generate_mac(message, stream, salt, static_key):
	hasher = hashlib.sha256()
	hasher.update(bytearray(message))
	hasher.update(bytearray(stream.getNext()))
	hasher.update(bytearray(static_key))
	return hasher.hexdigest()
		
stream_key = "streamkey"
static_key = "statickey"

stream = rc4_stream(stream_key)

print stream.S[0], stream.i, stream.j
print stream.getNext()
print stream.S[0], stream.i, stream.j
stream.reset()
print stream.S[0], stream.i, stream.j
print stream.getNext()
print stream.S[0], stream.i, stream.j
print stream.getNext()
stream.reset()
print stream.getNext()
stream.reset()


for i in range(5):
	print(generate_mac("hello world", stream, static_key))


stream.reset()	
for i in range(5):
	print(generate_mac("hello world", stream, static_key))

