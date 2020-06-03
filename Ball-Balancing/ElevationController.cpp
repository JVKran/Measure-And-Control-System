#include "ElevationController.hpp"

ElevationController::ElevationController(const int8_t minElevation, const int8_t maxElevation, const int8_t zeroPoint):
	minElevation(minElevation),
	zeroPoint(zeroPoint),
	maxElevation(maxElevation)
{}

void ElevationController::begin(const uint8_t servoPin){
	servoMotor.attach(servoPin);
	servoMotor.write(90);
}

void ElevationController::setElevation(const int8_t desiredElevation){
	if(desiredElevation >= minElevation && desiredElevation <= maxElevation){
		servoMotor.write(zeroPoint + desiredElevation);
	}
}

void ElevationController::test(){
	for(int8_t degree = -25; degree < 25; degree++){
		setElevation(degree);
		delay(200);
	}
	for(int8_t degree = 25; degree > -25; degree--){
		setElevation(degree);
		delay(200);
	}
}
