Introduction:
This report documents a thorough investigation into signal processing techniques, focusing on signal generation, analysis, and noise cancellation. Through the utilization of Python libraries such as NumPy, Matplotlib, and SciPy, we delve into the transformation of signals between time and frequency domains, as well as the implementation of noise cancellation algorithms.


Signal Generation:
The project commences with the creation of a composite signal consisting of multiple tones. These tones are defined by pairs of frequencies selected from the 3rd and 4th octaves. The signal generation process unfolds through the following steps:
Frequency Selection: Frequencies from both the 3rd and 4th octaves are chosen. The specific frequencies selected are meticulously documented, providing insight into the musical intervals utilized.
Signal Equation: The signal is generated using a mathematical equation that combines sinusoidal components for each pair of frequencies. This equation incorporates parameters for time, starting time, and duration for each note, ensuring precise timing for each tone.
For each pair of frequencies, the signal equation is represented as:
x(t) = Σ [sin(2π * Fi * t) + sin(2π * fi * t)] * (unit step(t - ti) - unit step(t - ti - Ti))

Where:
Fi and fi represent the frequencies from the 3rd and 4th octaves respectively.
ti is the starting time of each note.
Ti is the duration of each note.
The unit step function is represented as "unit step(t)".
Plotting: The resulting signal in the time domain is visualized using the Matplotlib library. The plotting process is detailed, highlighting the use of the "plt.stem()" function to accurately represent discrete data points.


Signal Analysis:
Following signal generation, attention is directed towards signal analysis, particularly in the frequency domain. The transformation of the signal from the time domain to the frequency domain is thoroughly examined:
FFT Transformation: The Fast Fourier Transform (FFT) algorithm is applied to convert the signal from the time domain to the frequency domain. This transformation is illustrated using both code snippets and explanatory text, ensuring clarity in understanding.
Frequency Spectrum Visualization: The frequency spectrum obtained from the FFT transformation is plotted using Matplotlib. The plotting methodology is explained, including the determination of frequency bins and amplitude scaling.
Noise Addition:

To simulate real-world conditions, noise is intentionally added to the signal, necessitating additional processing steps:
Noise Generation: Random frequencies are generated to produce a noise signal, mirroring the stochastic nature of environmental noise. The process of noise generation is outlined, emphasizing the random nature of the frequencies selected.
Noise Addition: The noise signal is then added to the original signal, resulting in a noisy signal in the time domain. This step is described in detail, highlighting the impact of noise on signal fidelity.

Noise Cancellation:
In response to the introduced noise, noise cancellation techniques are applied to restore signal clarity:
Peak Identification: High-frequency peaks in the noisy signal are identified, exceeding the maximum frequency of the original signal. The methodology for peak detection is explained, underscoring the importance of accurately identifying noise components.
Filtering Process: The identified high-frequency components are subtracted from the noisy signal, effectively filtering out noise. The filtering equation is provided, along with insights into its implementation.

Conclusion:
In conclusion, this project offers a comprehensive exploration of signal processing techniques, ranging from signal generation to noise cancellation. Through detailed documentation of code implementation and analysis methods, readers gain a thorough understanding of signal manipulation in both the time and frequency domains. By simulating real-world noise scenarios and employing noise cancellation algorithms, the project highlights practical applications of signal processing in enhancing signal quality and reliability.
