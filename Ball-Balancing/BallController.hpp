#ifndef __BALL_CONTROLLER
#define __BALL_CONTROLLER

#include <Arduino.h>
#include "ElevationController.hpp"
#include "DistanceSensor.hpp"

class BallController {
	private:
		ElevationController motor;
		DistanceSensor sensor;
		uint8_t distance;

		unsigned long long lastUpdate = 0;
		uint16_t dt = 188;

		int16_t error, errorDiv, errorPrev, steerAction;
		int32_t errorSum;
	public:
		BallController(ElevationController & motor, DistanceSensor & sensor);

		void operator()(const uint8_t setPoint = 40, const float Kp = 0.22, const float Ki = 0.1, const float Kd = 4);
};

#endif //__BALL_CONTROLLER