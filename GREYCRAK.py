# RENDER - OFFENSIVE SECURITY SOLUTIONS - "GREYCRAK"
# MADE BY: "Grey."
#
# // ! All other sellers have scammed / are trying to rat you.
#
# // : BTC : 3Mf37GhjYfrjTG59hmT3rAe5ntWDCgeDVg 
#=====================================================================================================

import os
import pickle
import hashlib
import binascii
import multiprocessing
from ellipticcurve.privateKey import PrivateKey

DATABASE = r'database/Database/'

def generate_private_key():
	"""
	Generate's a random 32-byte hex integer which acts as a private key.
	"""
	return binascii.hexlify(os.urandom(32)).decode('utf-8').upper()

def private_key_to_public_key(private_key):
	"""
	Accept a hex private key and converts it to its respective public key.
	Because converting a private key to a public key requires SECP256k1 ECDSA
	signing, this is usually the worst part.
	"""
	pk = PrivateKey().fromString(bytes.fromhex(private_key))
	return '04' + pk.publicKey().toString().hex().upper()

def public_key_to_address(public_key):
	"""
	Accept a public key and convert it to its resepective P2PKH wallet address.

	"""
	output = []
	alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
	var = hashlib.new('ripemd160')
	encoding = binascii.unhexlify(public_key.encode())
	var.update(hashlib.sha256(encoding).digest())
	var_encoded = ('00' + var.hexdigest()).encode()
	digest = hashlib.sha256(binascii.unhexlify(var_encoded)).digest()
	var_hex = '00' + var.hexdigest() + hashlib.sha256(digest).hexdigest()[0:8]
	count = [char != '0' for char in var_hex].index(True) // 2
	n = int(var_hex, 16)
	while n > 0:
		n, remainder = divmod(n, 58)
		output.append(alphabet[remainder])
	for i in range(count): output.append(alphabet[0])
	return ''.join(output[::-1])

def process(private_key, public_key, address, database):
	"""
	Accept an address to the database. If the address is found in the
	database, then it is assumed to have a balance and the wallet data is
	written to the hard drive. If not, its considered invalid.
	"""
	if address in database[0] or \
	   address in database[1] or \
	   address in database[2] or \
	   address in database[3]:
		with open('GREYCRAK.txt', 'a') as file:
			file.write('hex private key: ' + str(private_key) + '\n' +
				   'WIF private key: ' + str(private_key_to_WIF(private_key)) + '\n' +
			      	   'public key: ' + str(public_key) + '\n' +
			           'address: ' + str(address) + '\n\n')
	else:
		print(str(address))

def private_key_to_WIF(private_key):
	"""
	Convert the hex private key into Wallet Import Format for easier wallet
	importing. Only called if valid.
	"""  #Made by Grey
	digest = hashlib.sha256(binascii.unhexlify('80' + private_key)).hexdigest()
	var = hashlib.sha256(binascii.unhexlify(digest)).hexdigest()
	var = binascii.unhexlify('80' + private_key + var[0:8])
	alphabet = chars = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
	value = pad = 0
	result = ''
	for i, c in enumerate(var[::-1]): value += 256**i * c
	while value >= len(alphabet):
		div, mod = divmod(value, len(alphabet))
		result, value = chars[mod] + result, div
	result = chars[value] + result
	for c in var:
		if c == 0: pad += 1
		else: break
	return chars[0] * pad + result

def main(database):
	"""
	Uses multiprocessing and to make a loop
	"""
	while True:
		private_key = generate_private_key()
		public_key = private_key_to_public_key(private_key)
		address = public_key_to_address(public_key)
		process(private_key, public_key, address, database)



if __name__ == '__main__':
	"""
	Initialize the multiprocessing to target the main
	function with cpu_count() and its concurrent processes.
	"""
	database = [set() for _ in range(4)]
	count = len(os.listdir(DATABASE))
	half = count // 2
	quarter = half // 2
	for c, p in enumerate(os.listdir(DATABASE)):
		print('\rreading database: ' + str(c + 1) + '/' + str(count), end = ' ')
		with open(DATABASE + p, 'rb') as file:
			if c < half:
				if c < quarter: database[0] = database[0] | pickle.load(file)
				else: database[1] = database[1] | pickle.load(file)
			else:
				if c < half + quarter: database[2] = database[2] | pickle.load(file)
				else: database[3] = database[3] | pickle.load(file)
	print('DONE')

	# To verify the database size, remove the # from the line below
	#print('database size: ' + str(sum(len(i) for i in database))); quit()

	for cpu in range(multiprocessing.cpu_count()):
		multiprocessing.Process(target = main, args = (database, )).start()
