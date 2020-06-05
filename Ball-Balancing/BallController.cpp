#include "BallController.hpp"

BallController::BallController(ElevationController & motor, DistanceSensor & sensor):
	motor(motor),
	sensor(sensor)
{}

void BallController::operator()(const uint8_t setPoint, const float Kp, const float Ki, const float Kd){
	error = sensor.getDistance() - setPoint;			// 50 - 200 = 150
    //errorSum += error;
    if(millis() - lastUpdate > dt){
    	lastUpdate = millis();
	    errorDiv = (error - errorPrev);
	    errorPrev = error;
    }

    steerAction = (Kp * error) + (Ki * errorSum) - (Kd * errorDiv);
 //    Serial.print(Kp * error);
 //    Serial.print(" ");
	// Serial.println(Kd * errorDiv);
	Serial.println(Kd * errorDiv);
    motor.setElevation(steerAction);
}