# Faulty Signal Detection using Machine Learning

This project aims to detect anomalies in electrical signals such as spikes, sags, frequency shifts, and noise using synthetic data and machine learning models.

## Features Used
- Root Mean Square (RMS)
- Mean
- Standard Deviation (STD)
- Peak Amplitude
- Dominant Frequency
- Frequency Spread

## Signal Classes
- Normal
- Spike
- Sag
- Frequency Change
- Noisy

## Pipeline
1. Generate synthetic signals
2. Extract time & frequency features
3. Train classifier (e.g., Random Forest)
4. Evaluate using accuracy & confusion matrix

## Requirements
1. numpy
2. pandas
3. matplotlib
4. scipy
5. scikit-learn
