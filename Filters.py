from Signals import SineWave, SquareWave
import matplotlib.pyplot as plot
from scipy.fft import fft

class Filter:

	def draw(self):
		# Use Matplotlib to plot the filter coefficients.
		plot.plot(self.coefficients)
		plot.title('Filter Coefficients')
		plot.show()

	def showResult(self, filteredSignal, plotTitle, orignalSignal):
		# Use Matplotlib to plot the difference between the original and the filtered signal
		# for a side by side comparison.
		plot.figure(figsize=(12, 4))
		plot.subplot(1, 2, 1)
		plot.plot(orignalSignal)
		plot.title('Orignal')
		plot.xlabel('Time')
		plot.ylabel('Amplitude')
		plot.grid(True, which='both')
		plot.axhline(y=0, color='k')
		plot.subplot(1, 2, 2)
		plot.plot(filteredSignal)
		plot.title(plotTitle)
		plot.xlabel('Time')
		plot.ylabel('Amplitude')
		plot.grid(True, which='both')
		plot.axhline(y=0, color='k')
		plot.show()

class MovingAverage(Filter):

	def __init__(self, coefficients = [0.25, 0.25, 0.25, 0.25]):
		self.coefficients = coefficients

	def apply(self, signalToFilter, showFilterResult = True):
		taps = len(self.coefficients)
		newSignal = [0 for i in range(len(signalToFilter))]
		for i in range(len(signalToFilter)):
			if i >= taps:
				for j in range(taps):
					newSignal[i] = newSignal[i] + (signalToFilter[i - j] * self.coefficients[taps - j - 1])
			else:
				for j in range(taps - (taps - i)):
					newSignal[i] = newSignal[i] + (signalToFilter[i - j] * self.coefficients[taps - j - 1])
		if showFilterResult:
			self.showResult(newSignal, 'Result of Moving Average', signalToFilter)
		return newSignal

class FiniteImpulseResponse(Filter):

	def __init__(self, coefficients = [-0.5, 0.5]):
		self.coefficients = coefficients

	def apply(self, signalToFilter, showFilterResult = True):
		taps = len(self.coefficients)
		newSignal = [0 for i in range(len(signalToFilter))]
		for i in range(len(signalToFilter)):
			if i >= taps:
				for j in range(taps):
					newSignal[i] = newSignal[i] + (signalToFilter[i - j] * self.coefficients[taps - j - 1])
			else:
				for j in range(taps - (taps - i)):
					newSignal[i] = newSignal[i] + (signalToFilter[i - j] * self.coefficients[taps - j - 1])
		if showFilterResult:
			self.showResult(newSignal, 'Result of Finite Impulse Response', signalToFilter)
		return newSignal

class Median(Filter):

	def __init__(self, taps = 3):
		self.taps = taps

	def apply(self, signalToFilter, showFilterResult = True):
		newSignal = [0 for i in range(len(signalToFilter))]
		for i in range(len(signalToFilter)):
			subList = []
			if i >= self.taps:
				for j in range(self.taps):
					subList.append(signalToFilter[i - j])
			else:
				for j in range(self.taps - (self.taps - i)):
					subList.append(signalToFilter[i - j])
			subList.sort()
			if(len(subList) < self.taps):
				if(len(subList) != 0):
					newSignal[i] = newSignal[i] + subList[0]
			else:
				newSignal[i] = newSignal[i] + (subList[int(self.taps/2)])
		if showFilterResult:
			self.showResult(newSignal, 'Result of Median Filter', signalToFilter)
		return newSignal

	def draw(self):
		return

class FastFourierTransform:

	def apply(self, signalToFilter, showFilterResult = True):
		# Use Fast Fourier Transform module from Scipy to apply the Fast Fourier Transform.
		frequencyDomain = fft(signalToFilter)
		if showFilterResult:
			self.showResult(frequencyDomain, signalToFilter)
		return frequencyDomain

	def showResult(self, frequencyDomain, orignalSignal):
		# Use Matplotlib to plot the difference between the signal in Time vs Frequency Domain.
		plot.figure(figsize=(12, 4))
		plot.subplot(1, 2, 1)
		plot.plot(orignalSignal)
		plot.title('Time Domain')
		plot.xlabel('Time')
		plot.ylabel('Amplitude')
		plot.grid(True, which='both')
		plot.axhline(y=0, color='k')
		plot.subplot(1, 2, 2)
		plot.plot(frequencyDomain)
		plot.title('Frequency Domain')
		plot.xlabel('Frequency')
		plot.ylabel('Amplitude')
		plot.grid(True, which='both')
		plot.axhline(y=0, color='k')
		plot.show()

	def draw(self):
		return

if __name__ == "__main__":
	sine = SineWave(50)
	square = SquareWave()
	movFilter = MovingAverage()
	firFilter = FiniteImpulseResponse()
	medFilter = Median(3)
	fftFilter = FastFourierTransform()

	square.draw()
	sine.draw()

	movFilter.apply(sine.getSignal())
	movFilter.apply(square.getSignal())

	firFilter.apply(sine.getSignal())
	firFilter.apply(square.getSignal())

	medFilter.apply(sine.getSignal())
	medFilter.apply(square.getSignal())

	fftFilter.apply(sine.getSignal())
	fftFilter.apply(square.getSignal())
