#includes
import numpy as np
from matplotlib import pyplot as plt
from scipy import signal
from scipy.io import wavfile

#Function to open the .wav file and extract its sampling frequency, array of samples
def DTFT(wav_file, newsamplingrate):
    #read wav file, print sampling rate and number of samples
    sampling_rate, samples = wavfile.read(wav_file)
    print("Original Sampling Rate:", sampling_rate)
    print("Number of Samples:", len(samples))

    #modify the sample rate
    if newsamplingrate < sampling_rate:
        sample_factor = int(sampling_rate / newsamplingrate)
        #slicing array
        newsamples = samples[::sample_factor]
    else:
        #no downsampling needed
        newsamples = samples

    #update sampling rate
    fsample = newsamplingrate

    #Discrete Time function of song
    num_samples = len(newsamples)
    taxis = np.linspace(0, num_samples / sampling_rate, num_samples)

    #DTFT of the samples in .wav file
    Xomega = np.fft.fft(newsamples)
    #|Xomega| = absolute value of Xomega
    Xomega_magnitude = np.abs(Xomega)
    #Freqeuncy axis: array of floats of frequency
    faxis = np.fft.fftfreq(len(newsamples), d = 1/fsample)

    #plotting x[n] with respect to its samples (integers)
    plt.figure(figsize=(20, 12))
    plt.plot(taxis, newsamples, label='Digital samples of song')
    plt.title('Samples of Song')
    plt.xlabel('Samples [n]')
    plt.ylabel('Magnitude x[n]')
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.autoscale()

    #plotting the DTFT of x[n] in frequency domainn
    plt.figure(figsize = (20, 12))
    plt.plot(faxis, Xomega_magnitude, label = 'Frequencies in .wav file')
    plt.title('Frequency Spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('|X(omega)|')
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.autoscale()

#python thinks 1 \t is tab, use raw string
DTFT(r"C:\Users\ducvi\PycharmProjects\S&S 1.94\.venv\thuong em.wav", 1000)