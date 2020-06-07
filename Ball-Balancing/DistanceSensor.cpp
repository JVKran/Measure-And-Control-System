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
	// Poll sensor max once per 5ms to allow signal to stabilize for ADC.
	if(millis() - lastMeasurement > 5){
		delay(5);
	} else {
		delay(millis() - lastMeasurement);
	}
	uint8_t distance = sensor.getDistance();
	lastMeasurement = millis();

	meanFilter.addSample(distance);
	uint8_t mean = meanFilter.getMean();
	//medianFilter.addSample(distance);
	//uint8_t median = medianFilter.getMedian();

	// Serial.print("Median:");
	// Serial.print(median);
	// Serial.print(" ");
	// Serial.print("Mean:");
	// Serial.println(mean);

	return mean;
}