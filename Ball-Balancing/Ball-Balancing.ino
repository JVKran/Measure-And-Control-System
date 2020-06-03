#include <SharpIR.h>
#include "ElevationController.hpp"
#include "BallController.hpp"

ElevationController motor(-25, 25);
SharpIR distanceSensor(SharpIR::GP2Y0A02YK0F, A0);
BallController controller(motor, distanceSensor);

void setup() {
	Serial.begin(9600);
	motor.begin(5);
	motor.setElevation(0);
}

void loop() {
	// distance = distanceSensor.getDistance();
	// if(distance >= 0 && distance <= 180){
	// 	servoMotor.write(distanceSensor.getDistance());
	// }
	// delay(100);
	for(;;){
		controller();
		//motor.test();
	}

}
