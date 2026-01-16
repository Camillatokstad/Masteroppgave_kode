import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_30 = pd.read_csv("30MeV.csv")
data_55 = pd.read_csv("55MeV.csv")

data_30["Time"] = pd.to_datetime(data_30["Time"])
data_55["Time"] = pd.to_datetime(data_55["Time"])

data_30["Elapsed Time (s)"] = (data_30["Time"] - data_30["Time"].iloc[0]).dt.total_seconds()
data_55["Elapsed Time (s)"] = (data_55["Time"] - data_55["Time"].iloc[0]).dt.total_seconds()

window = 10  
data_30["Smoothed Current (nA)"] = data_30["Current (nA)"].rolling(window=window, center=True).mean()
data_55["Smoothed Current (nA)"] = data_55["Current (nA)"].rolling(window=window, center=True).mean()


# === Stilinnstillinger ===
plt.rcParams.update({
    'font.size': 20,            # normal tekststørrelse for akseetiketter og titler
    'xtick.labelsize': 15,      # større tall på aksene
    'ytick.labelsize': 15,
    'xtick.major.width': 1.5,   # litt tykkere tics (uten at rammen blir bold)
    'ytick.major.width': 1.5,
})

# === 30 MeV-plott ===
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(data_30["Elapsed Time (s)"], data_30["Smoothed Current (nA)"],
        color='lightcoral', linewidth=2)

ax.set_title("Average Beam Current (30 MeV)", fontsize=15)
ax.set_xlabel("Time (s)", fontsize=13)
ax.set_ylabel("Beam Current (nA)", fontsize=13)
ax.set_xlim(140, 3950)
ax.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig("Beam_current_30MeV.png")
plt.show()


# === 55 MeV-plott ===
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(data_55["Elapsed Time (s)"], data_55["Smoothed Current (nA)"],
        color='cornflowerblue', linewidth=2)

ax.set_title("Average Beam Current (55 MeV)", fontsize=15)
ax.set_xlabel("Time since start (s)", fontsize=13)
ax.set_ylabel("Beam Current (nA)", fontsize=13)
ax.set_xlim(70, 3700)
ax.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig("Beam_current_55MeV.png", dpi= 1200)
plt.show()



"""
plt.figure(figsize=(10, 6))
plt.plot(data_30["Elapsed Time (s)"], data_30["Smoothed Current (nA)"], color='lightcoral', linewidth=2)
plt.title("Average Beam Current (30 MeV)")
plt.xlabel("Time (s)")
plt.ylabel("Beam Current (nA)")
plt.xlim(140, 3950)
plt.grid(True, linestyle='--', alpha=0.7)
#plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
plt.plot(data_55["Elapsed Time (s)"], data_55["Smoothed Current (nA)"], color='cornflowerblue', linewidth=2)
plt.title("Average Beam Current (55 MeV)")
plt.xlabel("Time since start (s)")
plt.ylabel("Beam Current (nA)")
plt.xlim(70, 3700)
plt.grid(True, linestyle='--', alpha=0.7)
#plt.tight_layout()
plt.show()
"""