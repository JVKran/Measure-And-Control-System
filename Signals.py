import numpy as np
from scipy import signal
import matplotlib.pyplot as plot

class SineWave:

	def __init__(self, intervalEnd = 10, stepSize = 0.1):
		self.time = np.arange(0, intervalEnd, stepSize)
		self.amplitude = np.sin(self.time)

	def draw(self):
		plot.plot(self.time, self.amplitude)
		plot.title('Sine Wave')
		plot.xlabel('Time')
		plot.ylabel('Amplitude')
		plot.grid(True, which='both')
		plot.axhline(y=0, color='k')
		plot.show()

	def getSignal(self):
		return self.amplitude

class SquareWave:

	def __init__(self, frequency = 5, intervalEnd = 10, samplingRate = 1000):
		self.time = np.linspace(0, intervalEnd, samplingRate, endpoint = True)
		self.amplitude = signal.square(2 * np.pi * frequency * self.time)

	def draw(self):
		plot.plot(self.time, self.amplitude)
		plot.title('Square Wave')
		plot.xlabel('Time')
		plot.ylabel('Amplitude')
		plot.grid(True, which='both')
		plot.axhline(y=0, color='k')
		plot.show()

	def getSignal(self):
		return self.amplitude

if __name__ == "__main__":
	wave = SineWave(50)
	wave.draw()

	newWave = SquareWave(1)
	newWave.draw()