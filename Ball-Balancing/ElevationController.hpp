#ifndef __ELEVATION_CONTROLLER
#define __ELEVATION_CONTROLLER

#include <Arduino.h>
#include <Servo.h>

class ElevationController {
	private:
		Servo servoMotor;

		int8_t minElevation, zeroPoint, maxElevation, currentElevation;
	public:
		ElevationController(const int8_t minElevation, const int8_t maxElevation, const int8_t zeroPoint = 90);
		void begin(const uint8_t servoPin);

		void setElevation(int16_t desiredElevation);

		void test();
};

#endif //__ELEVATION_CONTROLLER