from Signals import SineWave, SquareWave
from Filters import MovingAverage, FiniteImpulseResponse, Median, FastFourierTransform
import matplotlib.pyplot as plot

class ShowFilterImpactTime:
	movFilter = MovingAverage()
	firFilter = FiniteImpulseResponse()
	medFilter = Median(3)

	def showResult(self, signal):
		self.movFilter.apply(signal.getSignal())
		self.firFilter.apply(signal.getSignal())
		self.medFilter.apply(signal.getSignal())


class ShowFilterImpactFrequency:
	movFilter = MovingAverage()
	firFilter = FiniteImpulseResponse()
	medFilter = Median()
	fftFilter = FastFourierTransform()

	def calculateResult(self, signal):
		originalFrequencyResponse = self.fftFilter.apply(signal.getSignal(), False)
		filteredFrequencyResponse = self.fftFilter.apply(self.movFilter.apply(signal.getSignal(), False), False)
		self.showResult(originalFrequencyResponse, filteredFrequencyResponse, 'Moving Average Filtered Frequency Response')

		filteredFrequencyResponse = self.fftFilter.apply(self.firFilter.apply(signal.getSignal(), False), False)
		self.showResult(originalFrequencyResponse, filteredFrequencyResponse, 'Finite Impulse Response Filtered Frequency Response')

		filteredFrequencyResponse = self.fftFilter.apply(self.medFilter.apply(signal.getSignal(), False), False)
		self.showResult(originalFrequencyResponse, filteredFrequencyResponse, 'Median Filtered Frequency Response')

	def showResult(self, original, filtered, plotTitle):
		plot.figure(figsize=(12, 4))
		plot.subplot(1, 2, 1)
		plot.plot(original)
		plot.title('Oringal Frequency Response')
		plot.xlabel('Frequency')
		plot.ylabel('Amplitude')
		plot.grid(True, which='both')
		plot.axhline(y=0, color='k')
		plot.subplot(1, 2, 2)
		plot.plot(filtered)
		plot.title(plotTitle)
		plot.xlabel('Frequency')
		plot.ylabel('Amplitude')
		plot.grid(True, which='both')
		plot.axhline(y=0, color='k')
		plot.show()

if __name__ == "__main__":
	sine = SineWave(50)
	square = SquareWave()

	timeEffect = ShowFilterImpactTime()
	timeEffect.showResult(sine)
	timeEffect.showResult(square)

	frequencyEffect = ShowFilterImpactFrequency()
	frequencyEffect.calculateResult(sine)
	frequencyEffect.calculateResult(square)