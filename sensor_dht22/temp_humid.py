# Adafruit_DHT 모듈을 사용하기 위해서는 사전에 설치가 필요
# 터미널을 실행하여 아래 명령어를 입력하여 설치할 수 있음
# pip3 install Adafruit_DHT

import Adafruit_DHT as dht
import time

# 아래에서 DHT11 센서의 경우 dht.DHT11, DHT22 센서의 경우 dht.DHT22 
sensor = dht.DHT22

# 라즈베리 파이의 GPIO 21번 핀이 DHT 센서의 데이터 핀(2번 핀)에 연결된 상태인 경우
pin = 21

try:
    while True:
        # read_retry 함수는 2가지 값을 동시에 반환하는 함수. 첫번째 값이 습도, 두번째 값이 온도
        humid, temp = dht.read_retry(sensor, pin)

        if humid is not None and temp is not None:
            print("Temp=", round(temp,2), " Humid=", round(humid,2))
        else:
            print("Failed to get reading")
        time.sleep(0.5)
        
except KeyboardInterrupt:
    print("finished")
