import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 976000

lightChannel = 0

def readChannel(channel):
	adc = spi.xfer2([1, (8 + channel) << 4, 0])
	adcOut = ((adc[1] & 3) << 8) + adc[2]
	return adcOut
	
def convert2volts(data, places):
	volts = (data * 3.3) / float(1023)
	volts = round(volts, places)
	return volts
	
try:
	while True:
		lightLevel = readChannel(lightChannel)
		lightVolts = convert2volts(lightLevel, 2)

		print("-------------------------------------")
		print("Light: %d (%f V)" %(lightLevel, lightVolts))
		
		time.sleep(0.5)
		
except KeyboardInterrupt:
	print("Finished")
	spi.close()
	
