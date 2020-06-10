#include "BallController.hpp"

BallController::BallController(ElevationController & motor, DistanceSensor & sensor):
	motor(motor),
	sensor(sensor)
{}

void BallController::operator()(const uint8_t setPoint, const float Kp, const float Kd){
	distance = sensor.getDistance();
	error = distance - setPoint;
    if(millis() - lastUpdate > dt){
        lastUpdate = millis();
    	errorDiv = (error - errorPrev);    
    	errorPrev = error;
    }
    steerAction = (Kp * error) + (Kd * errorDiv);
    motor.setElevation(steerAction);
    Serial.print("Steer-Action:");
    Serial.print(steerAction);
    Serial.print(" ");
    Serial.print("P-Action:");
    Serial.print(Kp * error);
    Serial.print(" ");
    Serial.print("D-Action:");
	Serial.println(Kd * errorDiv);
}