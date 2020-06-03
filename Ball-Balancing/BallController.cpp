#include "BallController.hpp"

BallController::BallController(ElevationController & motor, SharpIR & sensor):
	motor(motor),
	sensor(sensor)
{}

void BallController::operator()(const uint8_t setPoint, const float Kp, const float Ki, const float Kd){
	error = sensor.getDistance() - setPoint;			// 50 - 200 = 150
    errorSum += error;
    errorDiv = (error - errorPrev);
    steerAction = (Kp * error) + (Ki * errorSum) + (Kd * errorDiv);
    Serial.println(steerAction);
    motor.setElevation(steerAction);
    errorPrev = error;
}