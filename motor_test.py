import RPi.GPIO as GPIO
from time import sleep

# Set GPIO mode to BOARD
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Motor class
class Motor():
    def __init__(self, EnaA, In1A, In2A, EnaB, In1B, In2B):
        # Pin assignments
        self.EnaA = EnaA
        self.In1A = In1A
        self.In2A = In2A
        self.EnaB = EnaB
        self.In1B = In1B
        self.In2B = In2B
        
        # Setup pins
        GPIO.setup(self.EnaA, GPIO.OUT)
        GPIO.setup(self.In1A, GPIO.OUT)
        GPIO.setup(self.In2A, GPIO.OUT)
        GPIO.setup(self.EnaB, GPIO.OUT)
        GPIO.setup(self.In1B, GPIO.OUT)
        GPIO.setup(self.In2B, GPIO.OUT)
        
        # Initialize PWM
        self.pwmA = GPIO.PWM(self.EnaA, 100)
        self.pwmB = GPIO.PWM(self.EnaB, 100)
        self.pwmA.start(0)
        self.pwmB.start(0)

    def move(self, speed=0.5, turn=0, t=0):
        # Convert speed and turn to percentage
        speed *= 100
        turn *= 60

        # Adjust speeds for turning
        leftSpeed = speed - turn
        rightSpeed = speed + turn

        # Boost one side and slow the other slightly for sharper turns
        if turn > 0:  # Right turn
            leftSpeed *= 1.4  # Slightly faster left motor
            rightSpeed *= 0.8  # Slightly slower right motor
        elif turn < 0:  # Left turn
            leftSpeed *= 0.8  # Slightly slower left motor
            rightSpeed *= 1.4  # Slightly faster right motor

        # Clamp speeds to valid range
        leftSpeed = max(min(leftSpeed, 100), -100)
        rightSpeed = max(min(rightSpeed, 100), -100)

        # Debug output
        print(f"LS = {leftSpeed} RS = {rightSpeed}")

        # Set PWM duty cycles
        self.pwmA.ChangeDutyCycle(abs(leftSpeed))
        self.pwmB.ChangeDutyCycle(abs(rightSpeed))

        # Set motor directions
        if leftSpeed > 0:
            GPIO.output(self.In1A, GPIO.HIGH)
            GPIO.output(self.In2A, GPIO.LOW)
        else:
            GPIO.output(self.In1A, GPIO.LOW)
            GPIO.output(self.In2A, GPIO.HIGH)

        if rightSpeed > 0:
            GPIO.output(self.In1B, GPIO.HIGH)
            GPIO.output(self.In2B, GPIO.LOW)
        else:
            GPIO.output(self.In1B, GPIO.LOW)
            GPIO.output(self.In2B, GPIO.HIGH)

        # Duration of movement
        sleep(t)

    def stop(self, t=0):
        # Stop both motors
        self.pwmA.ChangeDutyCycle(0)
        self.pwmB.ChangeDutyCycle(0)
        sleep(t)

# Main function
def main():
    # Instantiate motor object
    motor = Motor(32, 11, 13, 33, 15, 16)

    # Test movements
    motor.move(0.5, 0, 2)   # Move forward
    motor.stop(2)

    motor.move(-0.5, 0, 2)  # Move backward
    motor.stop(2)

    motor.move(0.8, 0.5, 2)  # Right turn with boosted left motor
    motor.stop(2)

    motor.move(0.8, -0.5, 2)  # Left turn with boosted right motor
    motor.stop(2)

# Run main
if __name__ == '__main__':
    main()
