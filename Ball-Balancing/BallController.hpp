#ifndef __BALL_CONTROLLER
#define __BALL_CONTROLLER

#include <Arduino.h>
#include <SharpIR.h>
#include "ElevationController.hpp"

class BallController{
	private:
		ElevationController motor;
		SharpIR sensor;

		int16_t error, errorSum, errorDiv, errorPrev, steerAction;
	public:
		BallController(ElevationController & motor, SharpIR & sensor);

		// Ku = 0.8 en Tu = 8
		// void operator()(const uint8_t setPoint = 20, const float Kp = 0.48, const float Ki = 0.12, const float Kd = 0.5);
		void operator()(const uint8_t setPoint = 20, const float Kp = 2, const float Ki = 0, const float Kd = 50);
};

#endif //__BALL_CONTROLLER