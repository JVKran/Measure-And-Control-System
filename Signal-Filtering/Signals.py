# Importing modules
import numpy as np
from scipy import signal
import matplotlib.pyplot as plot
from copy import deepcopy as dc

class Signal:

	def getSignal(self):
		return self.amplitude

class SineWave(Signal):

	name = 'Sinewave'

	def __init__(self, signalFrequency = 4, intervalEnd = 10, samplingFrequency = 100):
		self.samplingFrequency = dc(samplingFrequency)
		# Use Numpy to create a list of length intervalEnd / stepSize.
		self.time = np.arange(0, intervalEnd, 1 / self.samplingFrequency)
		# Use Numpy to create a sinewave based on above created list.
		self.amplitude = np.sin(2 * np.pi * signalFrequency * self.time)

	def draw(self):
		# Use Matplotlib to plot the Sinewave.
		plot.plot(self.time, self.amplitude)
		plot.title('Sine Wave')
		plot.xlabel('Time')
		plot.ylabel('Amplitude')
		plot.grid(True, which='both')
		plot.axhline(y=0, color='k')
		plot.show()

	def __add__(self, other):
		newSine = SineWave()
		newSine.samplingFrequency = self.samplingFrequency
		newSine.time = self.time
		newSine.amplitude = self.amplitude + other.amplitude
		return newSine

class SquareWave(Signal):

	name = 'Squarewave'

	def __init__(self, signalFrequency = 1, intervalEnd = 10, samplingFrequency = 100):
		self.samplingFrequency = samplingFrequency
		# Use Numpy to create a list of length intervalEnd with steps equal to intervalEnd / samplingRate.
		self.time = np.arange(0, intervalEnd, 1 / self.samplingFrequency)
		# Use Signal module from Scipy to create a squarewave signal.
		self.amplitude = signal.square(2 * np.pi * signalFrequency * self.time)

	def draw(self):
		# Use Matplotlib to plot the Squarewave.
		plot.plot(self.time, self.amplitude)
		plot.title('Square Wave')
		plot.xlabel('Time')
		plot.ylabel('Amplitude')
		plot.grid(True, which='both')
		plot.axhline(y=0, color='k')
		plot.show()

	def __add__(self, other):
		newSquare = SquareWave()
		newSquare.samplingFrequency = self.samplingFrequency
		newSquare.time = self.time
		newSquare.amplitude = self.amplitude + other.amplitude
		return newSquare

if __name__ == "__main__":
	wave = SineWave(1)
	wave.draw()

	newWave = SquareWave(1)
	newWave.draw()
