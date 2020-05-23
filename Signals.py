import numpy as np
from scipy import signal
import matplotlib.pyplot as plot

class Signal:

	def getSignal(self):
		return self.amplitude

class SineWave(Signal):

	def __init__(self, intervalEnd = 10, stepSize = 0.1):
		# Use Numpy to create a list of length intervalEnd / stepSize.
		self.time = np.arange(0, intervalEnd, stepSize)
		# Use Numpy to create a sinewave based on above created list.
		self.amplitude = np.sin(self.time)

	def draw(self):
		# Use Matplotlib to plot the Sinewave.
		plot.plot(self.time, self.amplitude)
		plot.title('Sine Wave')
		plot.xlabel('Time')
		plot.ylabel('Amplitude')
		plot.grid(True, which='both')
		plot.axhline(y=0, color='k')
		plot.show()

class SquareWave(Signal):

	def __init__(self, frequency = 5, intervalEnd = 10, samplingRate = 1000):
		# Use Numpy to create a list of length intervalEnd with steps equal to intervalEnd / samplingRate.
		self.time = np.linspace(0, intervalEnd, samplingRate, endpoint = True)
		# Use Signal module from Scipy to create a squarewave signal.
		self.amplitude = signal.square(2 * np.pi * frequency * self.time)

	def draw(self):
		# Use Matplotlib to plot the Squarewave.
		plot.plot(self.time, self.amplitude)
		plot.title('Square Wave')
		plot.xlabel('Time')
		plot.ylabel('Amplitude')
		plot.grid(True, which='both')
		plot.axhline(y=0, color='k')
		plot.show()

if __name__ == "__main__":
	wave = SineWave(50)
	wave.draw()

	newWave = SquareWave(1)
	newWave.draw()
