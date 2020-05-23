from Signals import SineWave, SquareWave
import matplotlib.pyplot as plot

class MovingAverage:

	def __init__(self, coefficients = [0.25, 0.25, 0.25, 0.25]):
		self.coefficients = coefficients

	def applyFilter(self, signalToFilter):
		taps = len(self.coefficients)
		newSignal = [0 for i in range(len(signalToFilter))]
		for i in range(len(signalToFilter)):
			if i >= taps:
				for j in range(taps):
					newSignal[i] = newSignal[i] + (signalToFilter[i - j] * self.coefficients[taps - j - 1])
			else:
				for j in range(taps - i):
					newSignal[i] = newSignal[i] + (signalToFilter[i - j] * self.coefficients[taps - j - 1])
		return newSignal

if __name__ == "__main__":
	# signal = SineWave(50)
	signal = SquareWave()
	filter = MovingAverage()


	plot.plot(filter.applyFilter(signal.getSignal()))
	plot.show()