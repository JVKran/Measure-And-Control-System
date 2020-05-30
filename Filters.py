from Signals import SineWave, SquareWave, Signal
import matplotlib.pyplot as plot
from scipy.fft import fft
import numpy as np
from copy import deepcopy as dc

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

	name = 'Moving Average'

	def __init__(self, coefficients = [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25]):
		self.coefficients = coefficients

	def apply(self, signalToFilter, showFilterResult = False):
		taps = len(self.coefficients)
		newAmplitude = [0 for i in range(len(signalToFilter.amplitude))]
		for i in range(len(signalToFilter.amplitude)):
			if i >= taps:
				for j in range(taps):
					newAmplitude[i] = newAmplitude[i] + (signalToFilter.amplitude[i - j] * self.coefficients[taps - j - 1])
			else:
				for j in range(taps - (taps - i)):
					newAmplitude[i] = newAmplitude[i] + (signalToFilter.amplitude[i - j] * self.coefficients[taps - j - 1])
		if showFilterResult:
			self.showResult(newAmplitude, 'Result of Moving Average', signalToFilter.amplitude)
		newSignal = Signal()
		newSignal.name = signalToFilter.name
		newSignal.time = dc(signalToFilter.time)
		newSignal.amplitude = dc(newAmplitude)
		newSignal.samplingFrequency = dc(signalToFilter.samplingFrequency)
		return newSignal

class FiniteImpulseResponse(Filter):

	name = 'Finite Impulse Response'

	def __init__(self, coefficients = [-0.5, 0.5]):
		self.coefficients = coefficients

	def apply(self, signalToFilter, showFilterResult = False):
		taps = len(self.coefficients)
		newAmplitude = [0 for i in range(len(signalToFilter.amplitude))]
		for i in range(len(signalToFilter.amplitude)):
			if i >= taps:
				for j in range(taps):
					newAmplitude[i] = newAmplitude[i] + (signalToFilter.amplitude[i - j] * self.coefficients[taps - j - 1])
			else:
				for j in range(taps - (taps - i)):
					newAmplitude[i] = newAmplitude[i] + (signalToFilter.amplitude[i - j] * self.coefficients[taps - j - 1])
		if showFilterResult:
			self.showResult(newAmplitude, 'Result of Finite Impulse Response', signalToFilter.amplitude)
		newSignal = Signal()
		newSignal.name = signalToFilter.name
		newSignal.time = dc(signalToFilter.time)
		newSignal.amplitude = dc(newAmplitude)
		newSignal.samplingFrequency = dc(signalToFilter.samplingFrequency)
		return newSignal

class Median(Filter):

	name = 'Median'

	def __init__(self, taps = 3):
		self.taps = taps

	def apply(self, signalToFilter, showFilterResult = False):
		newAmplitude = [0 for i in range(len(signalToFilter.amplitude))]
		for i in range(len(signalToFilter.amplitude)):
			subList = []
			if i >= self.taps:
				for j in range(self.taps):
					subList.append(signalToFilter.amplitude[i - j])
			else:
				for j in range(self.taps - (self.taps - i)):
					subList.append(signalToFilter.amplitude[i - j])
			subList.sort()
			if(len(subList) < self.taps):
				if(len(subList) != 0):
					newAmplitude[i] = newAmplitude[i] + subList[0]
			else:
				newAmplitude[i] = newAmplitude[i] + (subList[int(self.taps/2)])
		if showFilterResult:
			self.showResult(newAmplitude, 'Result of Median Filter', signalToFilter.amplitude)
		newSignal = Signal()
		newSignal.name = signalToFilter.name
		newSignal.time = dc(signalToFilter.time)
		newSignal.amplitude = dc(newAmplitude)
		newSignal.samplingFrequency = dc(signalToFilter.samplingFrequency)
		return newSignal

	def draw(self):
		return

class FastFourierTransform:

	def apply(self, signalToFilter, showFilterResult = False):
		# Use Fast Fourier Transform module from Scipy to apply the Fast Fourier Transform.
		fourierTransform = np.fft.fft(dc(signalToFilter.amplitude)) / len(signalToFilter.amplitude)
		fourierTransform = fourierTransform[range(int(len(signalToFilter.amplitude)/2))]
		
		tpCount = len(signalToFilter.amplitude)
		values = np.arange(int(tpCount / 2))
		timePeriod = tpCount / signalToFilter.samplingFrequency
		frequencies = values / timePeriod

		if showFilterResult:
			self.showResult(frequencies, abs(fourierTransform))
		return dc(frequencies), dc(abs(fourierTransform))

	def showResult(self, frequencies, fourierTransform):
		# Use Matplotlib to plot the difference between the signal in Time vs Frequency Domain.
		plot.plot(frequencies, fourierTransform)
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
