import numpy as np
import librosa

def extract_features_and_score(file_paths):
    features = []

    for path in file_paths:
        y, sr = librosa.load(path, sr=None)

        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        zcr = librosa.feature.zero_crossing_rate(y)
        rms = librosa.feature.rms(y=y)

        avg_features = {
            "file": path.split("\\")[-1],
            "mfcc_mean": float(np.mean(mfcc)),
            "zcr_mean": float(np.mean(zcr)),
            "rms_mean": float(np.mean(rms)),
        }
        features.append(avg_features)

    mfccs = [f["mfcc_mean"] for f in features]
    zcrs = [f["zcr_mean"] for f in features]
    rmss = [f["rms_mean"] for f in features]

    # Example cognitive risk score calculation
    risk_score = float(np.mean(mfccs) * 0.5 + np.mean(zcrs) * 0.3 + np.mean(rmss) * 0.2)

    return {
        "risk_score": round(risk_score, 3),
        "file_analysis": features
    }
