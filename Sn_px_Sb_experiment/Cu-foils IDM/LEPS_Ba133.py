import curie as ci
import matplotlib.pyplot as plt

# --- Les inn spekteret ---
spe = ci.Spectrum('CP20251028_LEPS_Ba133_60cm.Spe')

# --- Plot som rådata (kanaler vs. counts) ---
spe.isotopes = ['133BA']
spe.plot(calibrated=False, annotate=False)
plt.show()

spe.summarize()