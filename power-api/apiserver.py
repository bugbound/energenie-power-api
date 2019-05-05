# power api by michael minchinton
# curl --data '{"socket": 1, "power": true}' -H "Content-Type: application/json" http://host:7000/api/power -X POST
# curl --data '{"socket": 1, "power": true}' -H "Content-Type: application/json" http://192.168.0.1:7000/api/power -X POST

from flask import Flask, request
import RPi.GPIO as GPIO
import time

# set the pins numbering mode
GPIO.setmode(GPIO.BOARD)

# Select the GPIO pins used for the encoder K0-K3 data inputs
GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

# Select the signal to select ASK/FSK
GPIO.setup(18, GPIO.OUT)

# Select the signal used to enable/disable the modulator
GPIO.setup(22, GPIO.OUT)

# Disable the modulator by setting CE pin lo
GPIO.output (22, False)

# Set the modulator to ASK for On Off Keying 
# by setting MODSEL pin lo
GPIO.output (18, False)

# Initialise K0-K3 inputs of the encoder to 0000
GPIO.output (11, False)
GPIO.output (15, False)
GPIO.output (16, False)
GPIO.output (13, False)

application = Flask(__name__)


@application.route("/")
def hello():
    return "<h1 style='color:red'>power-api</h1><a href=/api/power>power api</a>"
    
@application.route("/api/power", methods=['POST'])
def powerapi():
	jsonin = request.json
	socket = jsonin['socket']
	power = jsonin['power']
	
	
	if socket == 1 and power == True:
		socket_one_on()
		
	if socket == 1 and power == False:
		socket_one_off()
    
	if socket == 2 and power == True:
		socket_two_on()
		
	if socket == 2 and power == False:
		socket_two_off()
    
	if socket == 3 and power == True:
		socket_three_on()
		
	if socket == 3 and power == False:
		socket_three_off()
    
	if socket == 4 and power == True:
		socket_four_on()
		
	if socket == 4 and power == False:
		socket_four_off()
    
	return "OK"

###SOCKET ONE###
def socket_one_on():
	print "sending code 1111 socket 1 on"
	GPIO.output (11, True)
	GPIO.output (15, True)
	GPIO.output (16, True)
	GPIO.output (13, True)
	settle()

def socket_one_off():
	print "sending code 0111 socket 1 off"
	GPIO.output (11, True)
	GPIO.output (15, True)
	GPIO.output (16, True)
	GPIO.output (13, False)
	settle()


###SOCKET TWO###
def socket_two_on():
	print "sending code 1110 socket 2 on"
	GPIO.output (11, False)
	GPIO.output (15, True)
	GPIO.output (16, True)
	GPIO.output (13, True)
	settle()

def socket_two_off():
	print "sending code 0110 socket 2 off"
	GPIO.output (11, False)
	GPIO.output (15, True)
	GPIO.output (16, True)
	GPIO.output (13, False)
	settle()


###SOCKET THREE###
def socket_three_on():
	print "sending code 1101 socket 3 on"
	GPIO.output (11, True)
	GPIO.output (15, False)
	GPIO.output (16, True)
	GPIO.output (13, True)
	settle()

def socket_three_off():
	print "sending code 0101 socket 3 off"
	GPIO.output (11, True)
	GPIO.output (15, False)
	GPIO.output (16, True)
	GPIO.output (13, False)
	settle()


###SOCKET FOUR###
def socket_four_on():
	print "sending code 1100 socket 4 on"
	GPIO.output (11, False)
	GPIO.output (15, False)
	GPIO.output (16, True)
	GPIO.output (13, True)
	settle()

def socket_four_off():
	print "sending code 0100 socket 4 off"
	GPIO.output (11, False)
	GPIO.output (15, False)
	GPIO.output (16, True)
	GPIO.output (13, False)
	settle()



def settle():
	# let it settle, encoder requires this
	time.sleep(0.1)	
	# Enable the modulator
	GPIO.output (22, True)
	# keep enabled for a period
	time.sleep(0.25)
	# Disable the modulator
	GPIO.output (22, False)
