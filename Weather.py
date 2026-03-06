import matplotlib.pyplot as plt
import kagglehub
path = kagglehub.dataset_download("farnooshsoltani/wather-englich")
days = ['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri']
temps = [22, 35, 21, 26, 27, 30, 24]
plt.figure(figsize=(8, 5))
plt.plot(days, temps, marker='*', markersize=15, linestyle='-', color='darkred', linewidth=3)
plt.title('Weekly Temperature') 
plt.xlabel('Days of the Week')          
plt.ylabel('Temperature (°C)')           
print("Path to dataset files:", path) 
plt.grid()
plt.show()