import matplotlib.pyplot as plt
u = [74.938059, 69.912328, 64.958243, 60.109731, 55.398510, 50.853489, 46.500249, 42.360649, 38.452546, 34.789657, 31.381532, 28.233662, 25.347691, 22.721721, 20.350706, 18.226895, 16.340320, 14.679300, 13.230954, 11.981685, 10.917647, 10.025160, 9.291079, 8.703096, 8.249988, 7.921798, 7.709945, 7.607284, 7.608096, 7.708033, 7.904009, 8.194056, 8.577134, 9.052927, 9.621607, 10.283597, 11.039315, 11.888939, 12.832170, 13.868020, 14.994625, 16.208073, 17.504391, 18.878421, 20.323798, 21.832963, 23.397241, 25.006939, 26.651507, 28.319713]
x = [0.005000, 0.015000, 0.025000, 0.035000, 0.045000, 0.055000, 0.065000, 0.075000, 0.085000, 0.095000, 0.105000, 0.115000, 0.125000, 0.135000, 0.145000, 0.155000, 0.165000, 0.175000, 0.185000, 0.195000, 0.205000, 0.215000, 0.225000, 0.235000, 0.245000, 0.255000, 0.265000, 0.275000, 0.285000, 0.295000, 0.305000, 0.315000, 0.325000, 0.335000, 0.345000, 0.355000, 0.365000, 0.375000, 0.385000, 0.395000, 0.405000, 0.415000, 0.425000, 0.435000, 0.445000, 0.455000, 0.465000, 0.475000, 0.485000, 0.495000]


x0 = [0.005,0.025 , 0.045,0.065 ,0.085 ,0.115,0.15 ,0.1775,0.225,0.345,0.405,0.435,0.495]
u0 = [80,70,60,50,40,30,20,15,10,10,15,20,30]

plt.figure(figsize=(15,10))
plt.grid(True)
plt.title('T(x)')
plt.xlabel('x')
plt.ylabel('T')
plt.plot(x,u,'-o',color='red',label='real')
plt.plot(x0,u0,'-o',color='blue',label='expected')
plt.legend(loc='best')
plt.savefig("plot_Tx_result_and_expected.jpg")
plt.show()
