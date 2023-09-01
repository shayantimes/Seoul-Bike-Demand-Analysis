
import sys
import matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn as sn

df = pd.read_csv(r'D:/University\Data Mining/SeoulBikeData.csv',encoding= 'unicode_escape')
# mean of each column
mean1 = df["Rented Bike Count"].mean()
min1 = df["Rented Bike Count"].min()
max1 = df["Rented Bike Count"].max()
var1 = df["Rented Bike Count"].var()

mean2 = df["Hour"].mean()
min2 = df["Hour"].min()
max2 = df["Hour"].max()
var2 = df["Hour"].var()

mean3 = df["Temperature(°C)"].mean()
min3 = df["Temperature(°C)"].min()
max3 = df["Temperature(°C)"].max()
var3 = df["Temperature(°C)"].var()

mean4 = df["Humidity(%)"].mean()
min4 = df["Humidity(%)"].min()
max4 = df["Humidity(%)"].max()
var4 = df["Humidity(%)"].var()

mean5 = df["Wind speed (m/s)"].mean()
min5 = df["Wind speed (m/s)"].min()
max5 = df["Wind speed (m/s)"].max()
var5 = df["Wind speed (m/s)"].var()

mean6 = df["Visibility (10m)"].mean()
min6 = df["Visibility (10m)"].min()
max6 = df["Visibility (10m)"].max()
var6 = df["Visibility (10m)"].var()

mean7 = df["Dew point temperature(°C)"].mean()
min7 = df["Dew point temperature(°C)"].min()
max7 = df["Dew point temperature(°C)"].max()
var7 = df["Dew point temperature(°C)"].var()

mean8 = df["Solar Radiation (MJ/m2)"].mean()
min8 = df["Solar Radiation (MJ/m2)"].min()
max8 = df["Solar Radiation (MJ/m2)"].max()
var8 = df["Solar Radiation (MJ/m2)"].var()

mean9 = df["Rainfall(mm)"].mean()
min9 = df["Rainfall(mm)"].min()
max9 = df["Rainfall(mm)"].max()
var9 = df["Rainfall(mm)"].var()

mean10= df["Snowfall (cm)"].mean()
min10= df["Snowfall (cm)"].min()
max10= df["Snowfall (cm)"].max()
var10= df["Snowfall (cm)"].var()


# print("----------------------------")
# print("Rented Bike Count:")
# print("mean:",mean1,"\n","min:",min1,"\n","max:",max1,"\n","var:",var1,"\n")
# print("Hour:")
# print("mean:",mean2,"\n","min:",min2,"\n","max:",max2,"\n","var:",var2,"\n")
# print("Temperature(°C):")
# print("mean:",mean3,"\n","min:",min3,"\n","max:",max3,"\n","var:",var3,"\n")
# print("Humidity(%):")
# print("mean:",mean4,"\n","min:",min4,"\n","max:",max4,"\n","var:",var4,"\n")
# print("Wind speed (m/s):")
# print("mean:",mean5,"\n","min:",min5,"\n","max:",max5,"\n","var:",var5,"\n")
# print("Visibility (10m):")
# print("mean:",mean6,"\n","min:",min6,"\n","max:",max6,"\n","var:",var6,"\n")
# print("Dew point temperature(°C):")
# print("mean:",mean7,"\n","min:",min7,"\n","max:",max7,"\n","var:",var7,"\n")
# print("Solar Radiation (MJ/m2):")
# print("mean:",mean8,"\n","min:",min8,"\n","max:",max8,"\n","var:",var8,"\n")
# print("Rainfall(mm):")
# print("mean:",mean9,"\n","min:",min9,"\n","max:",max9,"\n","var:",var9,"\n")
# print("Snowfall (cm):")
# print("mean:",mean10,"\n","min:",min10,"\n","max:",max10,"\n","var:",var10,"\n")
# print("----------------------------")

# # print(df2,df3,df4,df5,df6,df7,df8,df8,df9,df10,df11)

# print("------------------")
# #Scatter plot According to Rented Bike Count

# df.plot(kind = 'scatter', x = 'Rented Bike Count', y = 'Hour')
# df.plot(kind = 'scatter', x = 'Rented Bike Count', y = 'Temperature(°C)')
# df.plot(kind = 'scatter', x = 'Rented Bike Count', y = 'Humidity(%)')
# df.plot(kind = 'scatter', x = 'Rented Bike Count', y = 'Wind speed (m/s)')
# df.plot(kind = 'scatter', x = 'Rented Bike Count', y = 'Visibility (10m)')
# df.plot(kind = 'scatter', x = 'Rented Bike Count', y = 'Dew point temperature(°C)')
# df.plot(kind = 'scatter', x = 'Rented Bike Count', y = 'Solar Radiation (MJ/m2)')
# df.plot(kind = 'scatter', x = 'Rented Bike Count', y = 'Rainfall(mm)')
# df.plot(kind = 'scatter', x = 'Rented Bike Count', y = 'Snowfall (cm)')
# plt.show()

# #Histogram Plot 

# df["Temperature(°C)"].plot(kind = 'hist')
# plt.show()
# df["Humidity(%)"].plot(kind = 'hist')
# plt.show()
# df["Wind speed (m/s)"].plot(kind = 'hist')
# plt.show()
# df["Visibility (10m)"].plot(kind = 'hist')
# plt.show()
# df["Dew point temperature(°C)"].plot(kind = 'hist')
# plt.show()
# df["Solar Radiation (MJ/m2)"].plot(kind = 'hist')
# plt.show()
# df["Rainfall(mm)"].plot(kind = 'hist')
# plt.show()
# df["Snowfall (cm)"].plot(kind = 'hist')
# plt.show()

# print("------------------------------------")\



# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()


# dataTest = pd.DataFrame(df)

# corr_matrix = dataTest.corr()
# sn.heatmap(corr_matrix, annot=True)
# plt.show()



# sns.catplot(
#     data=df, x="Seasons", y="Rented Bike Count", hue="Holiday",
#     kind="violin", inner="stick", split=True, palette="pastel",
# )
# sns.catplot(
#     data=df, x="Seasons", y="Rented Bike Count", hue="Holiday",
#     kind="swarm", col="Functioning Day", aspect=.7,
# )
# selectedData = df[["Rented Bike Count","Holiday"]]
# # print(selectedData)
# dataTest = pd.DataFrame(selectedData)
# Holidaycount = dataTest.groupby(['Holiday']).count();
# print(Holidaycount)


# selectedData = df[["Rented Bike Count","Seasons"]]
# dataTest = pd.DataFrame(selectedData)
# Seasonscount = dataTest.groupby(['Seasons']).count();
# print(Seasonscount)
# ,"Seasons","Holiday","Functioning Day"
# plt.show()