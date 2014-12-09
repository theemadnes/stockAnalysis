# basic machine learning tutorial 

import matplotlib
import matplotlib.pyplot as plt 
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
import time

date,bid,ask = np.loadtxt('GBPUSD/GBPUSD1d.txt', unpack = True, delimiter=',', converters={0:mdates.strpdate2num('%Y%m%d%H%M%S')})

# can't use dictionary because can't use array as key
patternArray = []
performanceArray = []

def percentChange(startPoint, currentPoint):
	return ((float(currentPoint) - startPoint)/abs(startPoint))*100.00

def patternStorage():
	patterStartTime = time.time()

	avgLine = ((bid+ask)/2) # list of averages between bid & ask
	x = len(avgLine) - 30 # setting an index that is ~30 less than newest item

	y = 11 

	while y < x:
		pattern = []
		# calculate percent change for 10 ticks
		p1 = percentChange(avgLine[y-10], avgLine[y-9])
		p2 = percentChange(avgLine[y-10], avgLine[y-8])
		p3 = percentChange(avgLine[y-10], avgLine[y-7])
		p4 = percentChange(avgLine[y-10], avgLine[y-6])
		p5 = percentChange(avgLine[y-10], avgLine[y-5])
		p6 = percentChange(avgLine[y-10], avgLine[y-4])
		p7 = percentChange(avgLine[y-10], avgLine[y-3])
		p8 = percentChange(avgLine[y-10], avgLine[y-2])
		p9 = percentChange(avgLine[y-10], avgLine[y-1])
		p10 = percentChange(avgLine[y-10], avgLine[y])

		outcomeRange = avgLine[y+20:y+30] # create list of 10 items 20-30 ticks in the future
		currentPoint = avgLine[y]

		try: 
			avgOutcome = reduce(lambda x,y: x+y, outcomeRange) / len(outcomeRange) # get average price in the future over the 10 points		

		except Exception as e:
			print str(e)
			avgOutcome = 0

		futureOutcome = percentChange(currentPoint, avgOutcome)
		pattern.append(p1)
		pattern.append(p2)
		pattern.append(p3)
		pattern.append(p4)
		pattern.append(p5)
		pattern.append(p6)
		pattern.append(p7)
		pattern.append(p8)
		pattern.append(p9)
		pattern.append(p10)

		patternArray.append(pattern)
		performanceArray.append(futureOutcome)

		y += 1

	patternEndTime = time.time()
	print len(patternArray)
	print len(performanceArray)
	print 'Pattern storage took: ' + str(patternEndTime - patterStartTime) + ' seconds'


def graphRawFX():
	

	fig  = plt.figure(figsize=(10,7))
	ax1 = plt.subplot2grid((40,40), (0,0), rowspan=40, colspan=40)

	ax1.plot(date,bid)
	ax1.plot(date,ask)
	plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)

	ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))

	for label in ax1.xaxis.get_ticklabels():
		label.set_rotation(45)

	ax1_2 = ax1.twinx()
	ax1_2.fill_between(date, 0, (ask-bid), facecolor='g', alpha=.3)

	
	plt.subplots_adjust(bottom=.23)

	plt.grid(True)
	plt.show()

patternStorage()