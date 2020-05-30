from Signals import SineWave, SquareWave
from Filters import MovingAverage, FiniteImpulseResponse, Median, FastFourierTransform
import matplotlib.pyplot as plot

class Measurements:

	fftFilter = FastFourierTransform()

	def show(self, signal, filter):
		plot.figure(figsize=(9, 5), num='Unfiltered ' + signal.name)
		plot.subplot(1, 2, 1)
		plot.suptitle('Unfiltered ' + signal.name, fontsize=16)
		plot.plot(signal.amplitude)
		plot.title('Time Domain') 
		plot.xlabel('Time')
		plot.ylabel('Amplitude')
		plot.grid(True, which='both')
		plot.axhline(y=0, color='k')
		plot.subplot(1, 2, 2)
		self.fftFilter.apply(signal, True)
		plot.show()
		plot.figure(figsize=(9, 5), num=filter.name +' Filtered ' + signal.name)
		plot.suptitle(filter.name +' Filtered '  + signal.name, fontsize=16)
		plot.subplot(1, 2, 1)
		plot.plot(filter.apply(signal).amplitude)
		plot.title('Time Domain')
		plot.xlabel('Time')
		plot.ylabel('Amplitude')
		plot.grid(True, which='both')
		plot.axhline(y=0, color='k')
		plot.subplot(1, 2, 2)
		filteredSignal = filter.apply(signal)
		self.fftFilter.apply(filteredSignal, True)
		plot.show()


if __name__ == "__main__":
	sineOneHz = SineWave(signalFrequency = 1)
	sineFiveHz = SineWave(signalFrequency = 5)
	sineSevenHz = SineWave(signalFrequency = 7)
	combinedSine = SineWave()
	combinedSine = sineOneHz + sineFiveHz + sineSevenHz
	
	squareOneHz = SquareWave(signalFrequency = 1)
	squareFiveHz = SquareWave(signalFrequency = 5)
	squareSevenHz = SquareWave(signalFrequency = 7)
	combinedSquare = SquareWave()
	combinedSquare = squareOneHz + squareFiveHz + squareSevenHz

	measurements = Measurements()
	movFilter = MovingAverage()
	firFilter = FiniteImpulseResponse()
	medFilter = Median()
	fftFilter = FastFourierTransform()

	measurements.show(sineOneHz, movFilter)
	measurements.show(sineOneHz, firFilter)
	measurements.show(sineOneHz, medFilter)

	measurements.show(squareOneHz, movFilter)
	measurements.show(squareOneHz, firFilter)
	measurements.show(squareOneHz, medFilter)

	measurements.show(combinedSine, movFilter)
	measurements.show(combinedSine, firFilter)
	measurements.show(combinedSine, medFilter)

	measurements.show(combinedSquare, movFilter)
	measurements.show(combinedSquare, firFilter)
	measurements.show(combinedSquare, medFilter)
