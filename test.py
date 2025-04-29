import RPi.GPIO as GPIO
import time
# (32,11,13,33,15,16)
# Pin configuration
ENA = 32  # EnaA
IN1A = 11
IN2A = 13
ENB = 33  # EnaB
IN1B = 15
IN2B = 16

# GPIO setup
GPIO.setmode(GPIO.BOARD)  # Or GPIO.BCM if you're using BCM pin numbering
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1A, GPIO.OUT)
GPIO.setup(IN2A, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)
GPIO.setup(IN1B, GPIO.OUT)
GPIO.setup(IN2B, GPIO.OUT)

# Enable the motors
GPIO.output(ENA, GPIO.HIGH)
GPIO.output(ENB, GPIO.HIGH)

# Function to move forward
def move_forward():
    GPIO.output(IN1A, GPIO.HIGH)
    GPIO.output(IN2A, GPIO.LOW)
    GPIO.output(IN1B, GPIO.HIGH)
    GPIO.output(IN2B, GPIO.LOW)

# Function to move backward
def move_backward():
    GPIO.output(IN1A, GPIO.LOW)
    GPIO.output(IN2A, GPIO.HIGH)
    GPIO.output(IN1B, GPIO.LOW)
    GPIO.output(IN2B, GPIO.HIGH)

# Function to turn left
def turn_left():
    GPIO.output(IN1A, GPIO.LOW)
    GPIO.output(IN2A, GPIO.HIGH)
    GPIO.output(IN1B, GPIO.HIGH)
    GPIO.output(IN2B, GPIO.LOW)

# Function to turn right
def turn_right():
    GPIO.output(IN1A, GPIO.HIGH)
    GPIO.output(IN2A, GPIO.LOW)
    GPIO.output(IN1B, GPIO.LOW)
    GPIO.output(IN2B, GPIO.HIGH)

# Run the motors in the following order: forward, backward, left, right
def main():
    # Move forward
    print("Moving Forward")
    move_forward()
    time.sleep(2)  # Move forward for 2 seconds
    
    # Move backward
    print("Moving Backward")
    move_backward()
    time.sleep(2)  # Move backward for 2 seconds
    
    # Turn left
    print("Turning Left")
    turn_left()
    time.sleep(2)  # Turn left for 2 seconds
    
    # Turn right
    print("Turning Right")
    turn_right()
    time.sleep(2)  # Turn right for 2 seconds
    
    # Stop motors
    GPIO.output(ENA, GPIO.LOW)
    GPIO.output(ENB, GPIO.LOW)
    print("Stopping Motors")
    GPIO.cleanup()

if __name__ == '__main__':
    main()
