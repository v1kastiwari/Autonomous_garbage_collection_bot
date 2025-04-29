#ultrasonic.py
import RPi.GPIO as GPIO
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)

# Set GPIO Pins
GPIO_TRIGGER = 3  # Trigger pin
GPIO_ECHO = 5     # Echo pin

# Set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def measure_distance():
    # Send a 10�s pulse to trigger the sensor
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)  # 10�s delay
    GPIO.output(GPIO_TRIGGER, False)
    
    # Record the time of signal sent and received
    start_time = time.time()
    stop_time = time.time()
    
    # Wait for the echo to start
    while GPIO.input(GPIO_ECHO) == 0:
        start_time = time.time()
    
    # Wait for the echo to end
    while GPIO.input(GPIO_ECHO) == 1:
        stop_time = time.time()
    
    # Time difference between start and stop
    elapsed_time = stop_time - start_time
    
    # Calculate distance (sound speed = 34300 cm/s)
    distance = (elapsed_time * 34300) / 2
    
    return distance

if __name__ == '__main__':
    try:
        while True:
            dist = measure_distance()
            print(f"Measured Distance: {dist:.2f} cm")
            time.sleep(1)  # Wait for 1 second before next measurement

    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
