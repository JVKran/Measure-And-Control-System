#ifndef __BALL_CONTROLLER
#define __BALL_CONTROLLER

#include <Arduino.h>
#include <SharpIR.h>
#include "ElevationController.hpp"
#include "DistanceSensor.hpp"

class BallController{
	private:
		ElevationController motor;
		DistanceSensor sensor;
		uint8_t distance;

		unsigned long long lastUpdate = 0;
		uint8_t dt = 50;

		int16_t error, errorDiv, errorPrev, steerAction;
		int32_t errorSum;
	public:
		BallController(ElevationController & motor, DistanceSensor & sensor);

		// Ku = 0.8 en Tu = 8
		// void operator()(const uint8_t setPoint = 40, const float Kp = 0.48, const float Ki = 0.12, const float Kd = 0.5);
		void operator()(const uint8_t setPoint = 30, const float Kp = 3, const float Kd = 1);
};

#endif //__BALL_CONTROLLER