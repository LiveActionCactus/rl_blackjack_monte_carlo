from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np


class Plotting:
	sv_useable_ace = defaultdict(list)
	sv_no_useable_ace = defaultdict(list)


	def __init__(self, state_values):
		self.state_values = state_values
		self.parse_useable_ace(state_values)
		self.plot_3d_bar_graph()


	def parse_useable_ace(self, state_values):
		for key, value in state_values.items():
			if key[2] == True:
				self.sv_useable_ace[key].append(value)
			else:
				self.sv_no_useable_ace[key].append(value)


	def plot_3d_bar_graph(self):
		xdata, ydata, zdata = self.extract_3d_data_from_dict(self.sv_no_useable_ace)
		bottom = np.zeros((len(zdata)))
		width = np.ones_like(zdata)
		depth = np.ones_like(zdata)


		fig = plt.figure(figsize=(8,3))
		ax1 = fig.add_subplot(121, projection='3d')
		ax1.bar3d(xdata, ydata, bottom, width, depth, zdata)

		## TODO: FIGURE OUT HOW TO PLOT A MESH LIKE IN CH 5.1
		# x, y = np.meshgrid(xdata, ydata)
		# R = np.sqrt(x**2 + y**2)
		# z = np.multiply(zdata, R)
		# ax1.plot_surface(x, y, z, lw=0.5, rstride=8, cstride=8, alpha=0.3)

		ax1.set(xlim=(4,21), ylim=(2,11), zlim=(-1,1))
		ax1.invert_yaxis()
		ax1.invert_xaxis()

		plt.show(block=True)


	def extract_3d_data_from_dict(self, dict_data):
		xdata = []
		ydata = []
		zdata = []
		for key, value in dict_data.items():
			if key[0] > 21:
				pass
			else:
				xdata.append(key[0])
				ydata.append(key[1])
				zdata.extend(value)

		return xdata, ydata, zdata