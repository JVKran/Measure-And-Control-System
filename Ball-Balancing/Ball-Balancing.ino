#include "ElevationController.hpp"
#include "BallController.hpp"
#include "DistanceSensor.hpp"

ElevationController motor(-25, 25);
DistanceSensor sensor(A0);
BallController controller(motor, sensor);

void setup() {
	Serial.begin(9600);
	motor.begin(5);
}

void loop() {
	controller();
}
