#include "ElevationController.hpp"

ElevationController::ElevationController(const int8_t minElevation, const int8_t maxElevation, const int8_t zeroPoint):
	minElevation(minElevation),
	zeroPoint(zeroPoint),
	maxElevation(maxElevation)
{}

void ElevationController::begin(const uint8_t servoPin){
	servoMotor.attach(servoPin);
	servoMotor.write(zeroPoint);
}

void ElevationController::setElevation(int16_t desiredElevation){
	if (desiredElevation < minElevation){
		desiredElevation = minElevation;
	} else if (desiredElevation > maxElevation){
		desiredElevation = maxElevation;
	}
	if(currentElevation != desiredElevation){
		currentElevation = zeroPoint + desiredElevation;
		servoMotor.write(currentElevation);
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
