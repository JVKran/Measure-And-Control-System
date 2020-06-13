#include "DistanceSensor.hpp"

void swap(uint8_t *xp, uint8_t *yp)  {  
    uint8_t temp = *xp;  
    *xp = *yp;  
    *yp = temp;  
}  

void bubbleSort(uint8_t arr[], uint8_t n)  {  
    uint8_t i, j;  
    for (i = 0; i < n-1; i++)      
    for (j = 0; j < n-i-1; j++)  
        if (arr[j] > arr[j+1])  
            swap(&arr[j], &arr[j+1]);  
}

DistanceSensor::DistanceSensor(const uint8_t distancePin):
	distancePin(distancePin)
{}

uint8_t DistanceSensor::measureDistance(){
	uint8_t distance = 9462 / (analogRead(distancePin) - 16.92);

	if(distance > 150) return 150;
	else if(distance < 20) return 20;
	else return distance;
}

uint8_t DistanceSensor::getDistance(){
	// Sampling rate of sensor is 20ms.
	if(millis() - lastMeasurement > 20){
		delay(20);
	} else {
		delay(millis() - lastMeasurement);
	}
	uint8_t distance = measureDistance();
	lastMeasurement = millis();

	meanFilter.addSample(distance);
	return meanFilter.getMean();
}