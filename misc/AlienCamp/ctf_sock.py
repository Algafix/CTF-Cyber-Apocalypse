
import socket

HOST = '159.65.24.118'
PORT = 30478   	  

emoji_val = {}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	
	s.connect((HOST, PORT))
	data = s.recv(1024)

	##### Select emoji translation #####

	s.send(b'1\n')
	data = s.recv(1024).decode('utf-8').split(' ')

	##### The first emoji comes in the first packet #####
	arrow = data.index('->')
	emoji = data[arrow-1][-1]
	value = data[arrow+1]
	
	emoji_val[emoji] = value

	##### Get the rest of the emojis #####

	data = s.recv(1024).decode('utf-8').split(' ')
	
	window = 0
	while True:
		try:
			arrow = data.index('->', window)
			emoji_val[data[arrow-1]] = data[arrow+1]
			window = arrow+1

		except ValueError:
			break
	
	##### Start with the operations #####
	
	s.send(b'2\n')

	for i in range(500):

		data = s.recv(1024)

		exp_list = data.decode('utf-8').split(':\n\n')[1].split('  =')[0].split(' ')

		# Transform emojis to values
		for i, value in enumerate(exp_list):
			if value in emoji_val.keys():
				exp_list[i] = emoji_val[value]

		result = eval(''.join(exp_list))
		
		s.send(str(result).encode()+b'\n')

	data = s.recv(1024)
	print(data.decode('utf-8'))


# Time: 0.04
# Correct! ✔
# Congratulations! 🎉
# You are one of us now! 😎!
# Here is a 🎁 for you: CHTB{3v3n_4l13n5_u53_3m0j15_t0_c0mmun1c4t3}		


