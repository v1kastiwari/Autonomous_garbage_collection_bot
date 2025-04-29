#include <Servo.h>

// Default servo positions
int frontBackPos = 170;
int heightPos = 40;
int gripPos = 130;
int rotationPos = 10;

// Create Servo objects
Servo ServoH;     // Height servo
Servo ServoFB;    // Front-back servo
Servo ServoGRIP;  // Grip servo
Servo ServoR;     // Rotation servo

// Servo control pins
const int ServoFBPin = 9;    // Front-back servo
const int ServoHPin = 10;    // Height servo
const int ServoGRIPPin = 11; // Grip servo
const int ServoRPin = 6;     // Rotation servo

// Ultrasonic sensor pins
const int trigPin = 7;
const int echoPin = 8;

// Color sensor pins
const int s0 = 4, s1 = 5, s2 = 2, s3 = 3, outPin = 12, ledPin = 13;

// Adjustable smoothing delays (in milliseconds)
const int heightSmoothingDelay = 15;
const int frontBackSmoothingDelay = 10;
const int gripSmoothingDelay = 5;
const int rotationSmoothingDelay = 15;

// Distance threshold for detecting bins
const int distanceThreshold = 20;

void setup() {
  // Attach servos to pins
  ServoFB.attach(ServoFBPin);
  ServoH.attach(ServoHPin);
  ServoGRIP.attach(ServoGRIPPin);
  ServoR.attach(ServoRPin);

  // Initialize servos to starting positions
  ServoR.write(rotationPos);
  delay(1000);
  ServoGRIP.write(gripPos);
  delay(1000);
  ServoFB.write(frontBackPos);
  delay(1000);
  ServoH.write(heightPos);
  delay(1500);

  // Ultrasonic sensor setup
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // Color sensor setup
  pinMode(s0, OUTPUT);
  pinMode(s1, OUTPUT);
  pinMode(s2, OUTPUT);
  pinMode(s3, OUTPUT);
  pinMode(outPin, INPUT);
  pinMode(ledPin, OUTPUT);

  // Set frequency scaling to 20%
  digitalWrite(s0, HIGH);
  digitalWrite(s1, LOW);

  Serial.begin(9600);
}

void loop() {
  delay(500);
  
  liftObject();
  // Reduced delay to 200ms for faster loop iteration
  delay(200);  // Shortened delay
}

void liftObject() {
  // Step 1: Get distance from ultrasonic sensor
  int distance = getUltrasonicDistance();
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  // Check if the distance is below the threshold (bin detection)
  if (distance < distanceThreshold) {
    Serial.println("Bin detected!");

    // Step 2: Identify bin color
    String color = getColor();
    Serial.println("Detected color: " + color); // Print the detected color

    // Step 3: Pick and place the bin based on color
    pickAndPlace(color);
  } else {
    Serial.println("No bin detected.");
  }
}

// Function to get distance from ultrasonic sensor
int getUltrasonicDistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);  // Duration of pulse for triggering the ultrasonic sensor
  digitalWrite(trigPin, LOW);
  long duration = pulseIn(echoPin, HIGH);
  int distance = duration * 0.034 / 2;
  return distance;
}

// Function to detect color using color sensor
String getColor() {
  // Turn on the LED for color detection
  digitalWrite(ledPin, HIGH);

  // Read Red
  digitalWrite(s2, LOW);
  digitalWrite(s3, LOW);
  delay(100);
  int redFrequency = pulseIn(outPin, LOW);

  // Read Green
  digitalWrite(s2, HIGH);
  digitalWrite(s3, HIGH);
  delay(100);
  int greenFrequency = pulseIn(outPin, LOW);

  // Read Blue
  digitalWrite(s2, LOW);
  digitalWrite(s3, HIGH);
  delay(100);
  int blueFrequency = pulseIn(outPin, LOW);

  // Turn off the LED
  digitalWrite(ledPin, LOW);

  // Print color frequencies
  Serial.print("Red: ");
  Serial.print(redFrequency);
  Serial.print(" | Green: ");
  Serial.print(greenFrequency);
  Serial.print(" | Blue: ");
  Serial.println(blueFrequency);

  // Determine color
  if (redFrequency < greenFrequency && redFrequency < blueFrequency) {
    return "RED";
  } else if (greenFrequency < redFrequency && greenFrequency < blueFrequency) {
    return "GREEN";
  } else if (blueFrequency < redFrequency && blueFrequency < greenFrequency) {
    return "BLUE";
  } else {
    return "UNKNOWN";
  }
}

// Function to pick and place a bin based on color
void pickAndPlace(String color) {
  // Step 1: Open grip
  Serial.println("Opening grip...");
  gripPos = 130;
  moveServo(ServoGRIP, gripPos);
  delay(1000);  // Wait for grip to open

  // Step 2: Lower height to pick up
  Serial.println("Lowering height to pick up...");
  heightPos = 140;
  moveServo(ServoH, heightPos);
  delay(1000);  // Wait for servo to reach position

  // Step 3: Close grip to grab bin
  Serial.println("Closing grip to grab bin...");
  gripPos = 30;
  moveServo(ServoGRIP, gripPos);
  delay(1000);  // Wait for grip to close

  // Step 4: Raise height to move the bin
  Serial.println("Raising height...");
  heightPos = 30;
  moveServo(ServoH, heightPos);
  delay(1000);  // Wait for servo to reach position

  // Step 5: Rotate based on detected color
  int rotationTarget;
  if (color == "RED") {
    rotationTarget = 140;  // Rotate to position for red
    Serial.println("Rotating to red position...");
  } else if (color == "GREEN") {
    rotationTarget = 150;  // Rotate to position for green
    Serial.println("Rotating to green position...");
  } else if (color == "BLUE") {
    rotationTarget = 160;  // Rotate to position for blue
    Serial.println("Rotating to blue position...");
  } else {
    rotationTarget = 150;  // Default to position for red if color is unknown
  }

  // Perform the rotation
  rotationPos = rotationTarget;
  moveServo(ServoR, rotationPos);
  delay(1000);  // Wait for rotation to complete

  // Step 6: Open grip to release bin
  Serial.println("Opening grip to release bin...");
  gripPos = 130;
  moveServo(ServoGRIP, gripPos);
  delay(1000);  // Wait for grip to open

  // Step 7: Return to default position
  Serial.println("Returning to default position...");
  rotationPos = 10;
  moveServo(ServoR, rotationPos);
  heightPos = 40;
  moveServo(ServoH, heightPos);
  delay(1000);  // Wait for servos to return to default positions

  Serial.println("Pick and place complete.");
}

// Function to move a servo smoothly
void moveServo(Servo &servo, int target) {
  int currentPos = servo.read();
  while (currentPos != target) {
    if (currentPos < target) currentPos++;
    else if (currentPos > target) currentPos--;
    servo.write(currentPos);
    delay(10);
  }
}
