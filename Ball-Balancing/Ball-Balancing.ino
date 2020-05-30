#include <Servo.h>
#include <SharpIR.h>

Servo servoMotor;
SharpIR distanceSensor(SharpIR::GP2Y0A02YK0F, A0);

uint8_t distance;

void setup() {
	servoMotor.attach(5);
}

void loop() {
	distance = distanceSensor.getDistance();
	if(distance >= 0 && distance <= 180){
		servoMotor.write(distanceSensor.getDistance());
	}
	delay(100);
}
