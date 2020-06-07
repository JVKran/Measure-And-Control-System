#ifndef __DISTANCE_SENSOR
#define __DISTANCE_SENSOR

#include <Arduino.h>
#include <SharpIR.h>

void swap(uint8_t *xp, uint8_t *yp);
void bubbleSort(uint8_t arr[], uint8_t n);

template <int N>
class MedianFilter {
	private:
		uint8_t samples[N] = {};
		uint8_t index = 0;
	public:
		void addSample(const uint8_t sample){
			if(index == N){
				index = 0;
			}
			samples[index++] = sample;
		}

		uint8_t getMedian(){
			bubbleSort(samples, N);
			return samples[(N - 1) / 2];
		}
};

template <int N>
class MeanFilter {
	private:
		uint8_t samples[N] = {};
		uint8_t index = 0;
	public:
		uint16_t sum(const uint8_t samples[]){
			uint16_t counter = 0;
			for(uint8_t index = 0; index < N; index++){
				counter += samples[index];
			}
			return counter;
		}

		void addSample(const uint8_t sample){
			if(index == N){
				index = 0;
			}
			samples[index++] = sample;
		}

		uint8_t getMean(){
			return sum(samples) / N;
		}
};

class DistanceSensor {
	private:
		// MedianFilter<50> medianFilter;
		MeanFilter<50> meanFilter;

		SharpIR sensor;
		unsigned long long int lastMeasurement = 0;
	public:
		DistanceSensor(const uint8_t distancePin = A0);
		uint8_t getDistance();
};

#endif //__DISTANCE_SENSOR