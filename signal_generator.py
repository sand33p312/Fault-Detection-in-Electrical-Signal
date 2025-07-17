import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def generate_sine_wave(frequency, amplitude, time_duration, sample_rate):
    """Generate sine wave data."""

    time = np.linspace(0, time_duration, sample_rate * time_duration, endpoint=False)
    sine_wave = amplitude * np.sin(2 * np.pi * frequency * time)

    h = round(np.log10(sample_rate * time_duration))

    time = [round(x, h) for x in time]
    time = np.array(time)

    # Save normal data

    df = pd.DataFrame({'Time' : time, 'Amplitude' : sine_wave, 'Label' : 'Normal'})
    df.to_csv('data/normal_signals.csv', index=False)

    # Save spiky data

    random_spikes = np.random.randint(0, 2, sample_rate * time_duration)
    spike_sine_wave = sine_wave + random_spikes

    dff = pd.DataFrame({'Time' : time, 'Amplitude' : spike_sine_wave, 'Label' : 'Spike'})
    dff.to_csv('data/spike_signals.csv', index=False)

    # Save sag signal
    
    sag_start = np.random.uniform(0.2*time_duration, 0.6*time_duration)
    sag_duration = np.random.uniform(0.05*time_duration, 0.2*time_duration)
    sag_end = sag_start + sag_duration

    sag_mask = (time >= sag_start) & (time <= sag_end)
    signal_with_sag = sine_wave.copy()
    signal_with_sag[sag_mask] *= 0.5

    dfs = pd.DataFrame({'Time' : time, 'Amplitude' : signal_with_sag, 'Label' : 'Sag'})
    dfs.to_csv('data/sag_signals.csv', index=False)

    # Save noisy signals

    noise = np.random.normal(0, 0.8, sample_rate * time_duration)
    noisy_signals = sine_wave + noise

    dfss = pd.DataFrame({'Time' : time, 'Amplitude' : noisy_signals, 'Label' : 'Noisy'})
    dfss.to_csv('data/noisy_signals.csv', index=False)

    # Save freq. change signal
    random_freq = np.random.randint(10*frequency, 20*frequency)
    
    change_start = np.random.uniform(0.1*time_duration, 0.3*time_duration)
    change_end = np.random.uniform(0.4*time_duration, 0.8*time_duration)

    freq_mask = (time >= change_start) & (time <= change_end)
    freq = np.full_like(time, frequency)
    freq[freq_mask] = random_freq

    phase = np.cumsum(freq) * (time[1] - time[0]) * 2 * np.pi
    freq_change_signal = np.sin(phase)

    dffc = pd.DataFrame({'Time' : time, 'Amplitude' : freq_change_signal, 'Label' : 'Freq_change'})
    dffc.to_csv('data/freq_change_signals.csv', index=False)
    
    # plt.figure(figsize=(10,6))
    # plt.plot(time, sine_wave)
    # plt.show()
    
if __name__ == "__main__":
    freq = 1
    amp = 10
    td = 3
    sr = 1000

    sine_wave_data = generate_sine_wave(freq,amp, td, sr) 
