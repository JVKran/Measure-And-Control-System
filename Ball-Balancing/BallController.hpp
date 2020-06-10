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
		uint16_t dt = 188;

		int16_t error, errorDiv, errorPrev, steerAction;
		int32_t errorSum;
	public:
		BallController(ElevationController & motor, DistanceSensor & sensor);

		// Ku = 0.8 en Tu = 8
		// void operator()(const uint8_t setPoint = 40, const float Kp = 0.48, const float Ki = 0.12, const float Kd = 0.5);
		// Bij p van 0.27/0.28 zijn de oscillaties stabiel met een periodetijd van gemiddeld 15.7 seconde.
		// Kp = 0.8 * 0.27 = 0.22
		// Kd = 0.27 * 15.7 / 10 = 0.42
		void operator()(const uint8_t setPoint = 40, const float Kp = 0.22, const float Kd = 3);
};

#endif //__BALL_CONTROLLER