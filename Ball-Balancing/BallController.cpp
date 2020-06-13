#include "BallController.hpp"

BallController::BallController(ElevationController & motor, DistanceSensor & sensor):
	motor(motor),
	sensor(sensor)
{}

void BallController::operator()(const uint8_t setPoint, const float Kp, const float Ki, const float Kd){
	distance = sensor.getDistance();
	error = distance - setPoint;
    errorSum += error;
    if(Ki * errorSum > 3 or Ki * errorSum < 3){
        errorSum = 3 / Ki;
    }
    if(millis() - lastUpdate > dt){
        lastUpdate = millis();
    	errorDiv = (error - errorPrev);    
    	errorPrev = error;
    }
    steerAction = (Kp * error) + (Kd * errorDiv) + (Ki * errorSum);
    motor.setElevation(steerAction);
}