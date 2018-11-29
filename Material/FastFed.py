import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import matplotlib.mlab as mlab
from scipy.stats import pearsonr, f_oneway

df = pd.read_csv('MeanBasic_features_Localization_10.csv')

channel = 3
df = df[df.Channel == channel]
df.Label.replace(['ibs','ibd','health','test'],[-1.0,0.0,1.0,2],inplace = True)
#print(df[df.Label == 'health'][df.Phase == 1])

def plotpack_separate(i):
	fig = plt.figure(figsize = (6,4))
	#print(pearsonr(df[df.Phase == 2][~pd.isnull(df[i])][i],df[df.Phase == 2][~pd.isnull(df[i])].Label))
	print(f_oneway(df[~pd.isnull(df[i])][df.Label == 1][df.Phase == 1][i], 
					df[~pd.isnull(df[i])][df.Label == -1][df.Phase == 1][i],
					df[~pd.isnull(df[i])][df.Label == 1][df.Phase == 2][i], 
					df[~pd.isnull(df[i])][df.Label == -1][df.Phase == 2][i]))
	(mu, sigma) = norm.fit(df[~pd.isnull(df[i])][df.Label == 1][df.Phase == 1][i])
	bins = np.histogram(df[~pd.isnull(df[i])][df.Label == 1][df.Phase == 1][i],30)[1]
	y = mlab.normpdf(bins, mu, sigma)
	plt.plot(bins, y,'k-',linewidth=2, label = 'health - fasting')
	(mu, sigma) = norm.fit(df[~pd.isnull(df[i])][df.Label == 1][df.Phase == 2][i])
	bins = np.histogram(df[~pd.isnull(df[i])][df.Label == 1][df.Phase == 2][i],30)[1]
	y = mlab.normpdf(bins, mu, sigma)
	plt.plot(bins, y,'k--',linewidth=2, label = 'health - fed')
	(mu, sigma) = norm.fit(df[~pd.isnull(df[i])][df.Label == -1][df.Phase == 1][i])
	bins = np.histogram(df[~pd.isnull(df[i])][df.Label == -1][df.Phase == 1][i],30)[1]
	y = mlab.normpdf(bins, mu, sigma)
	plt.plot(bins, y,'r-',linewidth=2, label = 'ibs - fasting')
	(mu, sigma) = norm.fit(df[~pd.isnull(df[i])][df.Label == -1][df.Phase == 2][i])
	bins = np.histogram(df[~pd.isnull(df[i])][df.Label == -1][df.Phase == 2][i],30)[1]
	y = mlab.normpdf(bins, mu, sigma)
	plt.plot(bins, y,'r--',linewidth=2, label = 'ibs - fed')
	plt.legend()
	plt.title(str(i))
	fig.tight_layout()
	#plt.savefig('Amplitude_C3',dpi=600)
	plt.show()

def plotpack_whole(i):
	fig = plt.figure(figsize = (6,4))
	(mu, sigma) = norm.fit(df[df.Phase == 1][i])
	bins = np.histogram(df[df.Phase == 1][i],30)[1]
	y = mlab.normpdf(bins, mu, sigma)
	plt.plot(bins, y,'k-',linewidth=2, label = 'fasting')
	(mu, sigma) = norm.fit(df[df.Phase == 2][i])
	bins = np.histogram(df[df.Phase == 2][i],30)[1]
	y = mlab.normpdf(bins, mu, sigma)
	plt.plot(bins, y,'r-',linewidth=2, label = 'fed')
	plt.legend()
	plt.title(str(i))
	fig.tight_layout()
	#plt.savefig('Amplitude_C3_com',dpi=600)
	plt.show()
	
for fea in df.columns[6:]:
	if 'SpectrumKurtosis' in fea:
		if 1:
			print(fea)
			plotpack_separate(fea)
			#plotpack_whole(fea)
		#except:
		#	pass