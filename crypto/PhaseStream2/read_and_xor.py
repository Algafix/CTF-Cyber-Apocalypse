




for line in open('output.txt'):
	
	bytes_line = bytearray.fromhex(line.strip())
	
	for value in range(256):
		if (bytes_line[0] ^ value) == ord('C'):
			if (bytes_line[1] ^ value) == ord('H'):
				if (bytes_line[2] ^ value) == ord('T'):
					if (bytes_line[3] ^ value) == ord('B'):
						print(bytearray([c^value for c in bytes_line]))





