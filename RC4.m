key = 'Stream Key';

% KSA
S = 0:255;
j = 0;
for i = 1:256
    j = mod(j + S(i) + key(mod(i-1, length(key))+1), 256);
    S([i, j]) = S([j, i]);
end




i = 0;
j = 0;
% discard first entries
for iter = 1:1024
    i = mod(i + 1, 256);
    j = mod(j + S(i+1), 256);
    S([i+1, j+1]) = S([j+1, i+1]);
end

vals = 1:1000;
pp = zeros(1000, 256);
for iter = 1:1000
    i = mod(i + 1, 256);
    j = mod(j + S(i+1), 256);
    S([i+1, j+1]) = S([j+1, i+1]);
    vals(iter) = S(mod(S(i+1)+S(j+1),256)+1);
    pp(iter, :) = S(:);
end


% %
% 
% self.i = (self.i + 1) % 256
% 		self.j = (self.j + self.S[self.i]) % 256
% 		self.S[self.i], self.S[self.j] = self.S[self.j], self.S[self.i]
% 		return self.S[(self.S[self.i] + self.S[self.j]) % 256]

% def rc4_ksa(key):
% 	key_length = len(key)
% 	key = bytearray(key)
% 	S = list(range(256))
% 	j = 0
% 	for i in range(256):
% 		j = (j + S[i] + key[i % key_length]) % 256
% 		S[i], S[j] = S[j], S[i]
% 	return S
%