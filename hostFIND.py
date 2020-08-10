import json, socket, sys, os

try:
	import requests
except:
	os.system('pip install requests;python run.py')

d = '\033[0;90m'
r = '\033[0;31m'
g = '\033[0;92m'
p = '\033[0;35m'
c = '\033[0;96m'
w = '\033[0;37m'

print(f'\n\n{c} {code by : Miyandi1997}\n')
print(f'\n\n{c} {host finder }\n')


if len(sys.argv) < 2:
	print(f'  {w}- Usage: python {sys.argv[0]} <hostname>\n           python {sys.argv[0]} ruangguru.com\n')

else:
	nyA = 'https://api.indoxploit.or.id/domain/'
	nyB = sys.argv[1]
	nyC = requests.get(nyA+nyB)
	nyD = json.loads(nyC.text)
	nyE = 0

	try:
		for i in nyD["data"]["subdomains"]:
			nyE +=1
			try:
				nyF = socket.gethostbyname(i)
				print(f'{w}{str(nyE)}}} {p}{str(i)} {g}{str(nyF)}')
			except socket.gaierror:
				print(f'{w}{str(nyE)}}} {p}{str(i)}')

	except TypeError:
		try:
			nyF = socket.gethostbyname(nyB)
			print(f'{w}1}} {p}{str(nyB)} {g}{str(nyF)}\n')
		except socket.gaierror:
			print(f'{w}1}} {p}{str(nyB)}')
