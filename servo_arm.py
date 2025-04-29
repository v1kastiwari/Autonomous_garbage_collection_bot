import RPi.GPIO as GPIO
import time

# Setup GPIO in BOARD mode
GPIO.setmode(GPIO.BOARD)

# Define the servo control pin
SERVO_PIN = 19

# Set up the servo pin as an output
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Set PWM frequency to 50 Hz (common for servos)
pwm = GPIO.PWM(SERVO_PIN, 50)

# Start PWM with 0 duty cycle (servo stationary)
pwm.start(0)

def set_angle(angle):
    """
    Set the servo motor to the specified angle.
    :param angle: Desired angle (0 to 180 degrees)
    """
    # Convert angle to duty cycle
    duty_cycle = 2 + (angle / 18)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)  # Allow servo to reach the position
    pwm.ChangeDutyCycle(0)  # Stop sending signal to reduce jitter

try:
    while True:
        # # Example: Sweep servo from 0 to 180 degrees and back
        # for angle in range(0, 91, 10):
        #     set_angle(angle)
        #     print(angle)
        #     # time.sleep(0.15)  # Add 1-second delay during the sweep
        # for angle in range(80, -1, -10):
        #     set_angle(angle)
        #     print(angle)
        #     # time.sleep(0.1)  # Add 1-second delay during the sweep
        set_angle(90)

except KeyboardInterrupt:
    print("\nExiting gracefully...")

finally:
    pwm.stop()
    GPIO.cleanup()
