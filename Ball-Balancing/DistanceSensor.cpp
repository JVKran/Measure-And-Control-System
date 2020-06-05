#include "DistanceSensor.hpp"

void swap(uint8_t *xp, uint8_t *yp)  {  
    uint8_t temp = *xp;  
    *xp = *yp;  
    *yp = temp;  
}  
  
// A function to implement bubble sort  
void bubbleSort(uint8_t arr[], uint8_t n)  {  
    uint8_t i, j;  
    for (i = 0; i < n-1; i++)      
      
    // Last i elements are already in place  
    for (j = 0; j < n-i-1; j++)  
        if (arr[j] > arr[j+1])  
            swap(&arr[j], &arr[j+1]);  
}

DistanceSensor::DistanceSensor(const uint8_t distancePin = A0):
	sensor(SharpIR::GP2Y0A02YK0F, distancePin)
{}

uint8_t DistanceSensor::getDistance(){
	uint8_t distance = sensor.getDistance();
	//Serial.println(distance);
	filter.addSample(distance);
	//Serial.println(filter.getMean());
	return filter.getMean();
}