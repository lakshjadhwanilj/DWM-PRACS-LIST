#importing libraries
import pandas as pd
import numpy as np

#importing dataset
data = pd.read_csv("naive_data.csv")

#converting columns to list
income = list(data['INCOME'].values)
car_type = list(data['CAR_TYPE'].values)
car_age = list(data['CAR_AGE'].values)
insurance = list(data['INSURANCE'].values)

liability = insurance.count('LIABILITY')
colision = insurance.count('COLLISION')

liability_Under50, liability_Under100, liability_Under150 = 0, 0, 0
colision_Under50, colision_Under100, colision_Under150 = 0, 0, 0

liability_Sedan, liability_SUV, liability_Hatchback, liability_Sports = 0, 0, 0, 0
colision_Sedan, colision_SUV, colision_Hatchback, colision_Sports = 0, 0, 0, 0

liability_Under10, liability_Under20 = 0, 0
colision_Under10, colision_Under20 = 0, 0

for i in range(len(income)):
	if insurance[i] == 'LIABILITY':

		if income[i] <= 50000:
			liability_Under50 += 1
		elif income[i] > 50000 and income[i] <= 100000:
			liability_Under100 += 1
		elif income[i] > 100000 and income[i] < 150000:
			liability_Under150 += 1

		if car_type[i] == 'Sedan':
			liability_Sedan += 1
		elif car_type[i] == 'SUV':
			liability_SUV += 1
		elif car_type[i] == 'Hatchback':
			liability_Hatchback += 1
		elif car_type[i] == 'Sports Car':
			liability_Sports += 1

		if car_age[i] <= 10:
			liability_Under10 += 1	
		elif car_age[i] > 10 and car_age[i] <= 20:
			liability_Under20 += 1

	elif insurance[i] == 'COLISION':

		if income[i] <= 50000:
			colision_Under50 += 1
		elif income[i] > 50000 and income[i] <= 100000:
			colision_Under100 += 1
		elif income[i] > 100000 and income[i] < 150000:
			colision_Under150 += 1

		if car_type[i] == 'Sedan':
			colision_Sedan += 1
		elif car_type[i] == 'SUV':
			colision_SUV += 1
		elif car_type[i] == 'Hatchback':
			colision_Hatchback += 1
		elif car_type[i] == 'Sports Car':
			colision_Sports += 1

		if car_age[i] <= 10:
			colision_Under10 += 1	
		elif car_age[i] > 10 and car_age[i] <= 20:
			colision_Under20 += 1

liability_Under50 /= liability
liability_Under100 /= liability
liability_Under150 /= liability
colision_Under50 /= colision
colision_Under100 /= colision
colision_Under150 /= colision

liability_Sedan /= liability
liability_SUV /= liability
liability_Hatchback /= liability
liability_Sports /= liability
colision_Sedan /= colision
colision_SUV /= colision
colision_Hatchback /= colision
colision_Sports /= colision

liability_Under10 /= liability
liability_Under20 /= liability
colision_Under10 /= colision
colision_Under20 /= colision

#taking input
income_Inp = int(input("Enter Your Income: "))
cartype_Inp = input("Enter Car Type: ")
carage_Inp = int(input("Enter Car Age: "))

liability_Op, colision_Op = 0, 0

if income_Inp <= 50000:
	if car_type[i] == 'Sedan':
		if car_age[i] <= 10:
			liability_Op = liability_Under50 * liability_Sedan * liability_Under10 * (liability/len(income))
			colision_Op = colision_Under50 * colision_Sedan * colision_Under10 * (colision/len(income))
		elif car_age[i] > 10 and car_age[i] <= 20:
			liability_Op = liability_Under50 * liability_Sedan * liability_Under20 * (liability/len(income))
			colision_Op = colision_Under50 * colision_Sedan * colision_Under20 * (colision/len(income))
	elif car_type[i] == 'SUV':
		if car_age[i] <= 10:
			liability_Op = liability_Under50 * liability_SUV * liability_Under10 * (liability/len(income))
			colision_Op = colision_Under50 * colision_SUV * colision_Under10 * (colision/len(income))
		elif car_age[i] > 10 and car_age[i] <= 20:
			liability_Op = liability_Under50 * liability_SUV * liability_Under20 * (liability/len(income))
			colision_Op = colision_Under50 * colision_SUV * colision_Under20 * (colision/len(income))
	elif car_type[i] == 'Hatchback':
		if car_age[i] <= 10:
			liability_Op = liability_Under50 * liability_Hatchback * liability_Under10 * (liability/len(income))
			colision_Op = colision_Under50 * colision_Hatchback * colision_Under10 * (colision/len(income))
		elif car_age[i] > 10 and car_age[i] <= 20:
			liability_Op = liability_Under50 * liability_Hatchback * liability_Under20 * (liability/len(income))
			colision_Op = colision_Under50 * colision_Hatchback * colision_Under20 * (colision/len(income))
	elif car_type[i] == 'Sports Car':
		if car_age[i] <= 10:
			liability_Op = liability_Under50 * liability_Sports * liability_Under10 * (liability/len(income))
			colision_Op = colision_Under50 * colision_Sports * colision_Under10 * (colision/len(income))
		elif car_age[i] > 10 and car_age[i] <= 20:
			liability_Op = liability_Under50 * liability_Sports * liability_Under20 * (liability/len(income))
			colision_Op = colision_Under50 * colision_Sports * colision_Under20 * (colision/len(income))

elif income[i] > 50000 and income[i] <= 100000:
	if car_type[i] == 'Sedan':
		if car_age[i] <= 10:
			liability_Op = liability_Under100 * liability_Sedan * liability_Under10 * (liability/len(income))
			colision_Op = colision_Under100 * colision_Sedan * colision_Under10 * (colision/len(income))
		elif car_age[i] > 10 and car_age[i] <= 20:
			liability_Op = liability_Under100 * liability_Sedan * liability_Under20 * (liability/len(income))
			colision_Op = colision_Under100 * colision_Sedan * colision_Under20 * (colision/len(income))
	elif car_type[i] == 'SUV':
		if car_age[i] <= 10:
			liability_Op = liability_Under100 * liability_SUV * liability_Under10 * (liability/len(income))
			colision_Op = colision_Under100 * colision_SUV * colision_Under10 * (colision/len(income))
		elif car_age[i] > 10 and car_age[i] <= 20:
			liability_Op = liability_Under100 * liability_SUV * liability_Under20 * (liability/len(income))
			colision_Op = colision_Under100 * colision_SUV * colision_Under20 * (colision/len(income))
	elif car_type[i] == 'Hatchback':
		if car_age[i] <= 10:
			liability_Op = liability_Under100 * liability_Hatchback * liability_Under10 * (liability/len(income))
			colision_Op = colision_Under100 * colision_Hatchback * colision_Under10 * (colision/len(income))
		elif car_age[i] > 10 and car_age[i] <= 20:
			liability_Op = liability_Under100 * liability_Hatchback * liability_Under20 * (liability/len(income))
			colision_Op = colision_Under100 * colision_Hatchback * colision_Under20 * (colision/len(income))
	elif car_type[i] == 'Sports Car':
		if car_age[i] <= 10:
			liability_Op = liability_Under100 * liability_Sports * liability_Under10 * (liability/len(income))
			colision_Op = colision_Under100 * colision_Sports * colision_Under10 * (colision/len(income))
		elif car_age[i] > 10 and car_age[i] <= 20:
			liability_Op = liability_Under100 * liability_Sports * liability_Under20 * (liability/len(income))
			colision_Op = colision_Under100 * colision_Sports * colision_Under20 * (colision/len(income))
elif income[i] > 100000 and income[i] < 150000:
	if car_type[i] == 'Sedan':
		if car_age[i] <= 10:
			liability_Op = liability_Under150 * liability_Sedan * liability_Under10 * (liability/len(income))
			colision_Op = colision_Under150 * colision_Sedan * colision_Under10 * (colision/len(income))
		elif car_age[i] > 10 and car_age[i] <= 20:
			liability_Op = liability_Under150 * liability_Sedan * liability_Under20 * (liability/len(income))
			colision_Op = colision_Under150 * colision_Sedan * colision_Under20 * (colision/len(income))
	elif car_type[i] == 'SUV':
		if car_age[i] <= 10:
			liability_Op = liability_Under150 * liability_SUV * liability_Under10 * (liability/len(income))
			colision_Op = colision_Under150 * colision_SUV * colision_Under10 * (colision/len(income))
		elif car_age[i] > 10 and car_age[i] <= 20:
			liability_Op = liability_Under150 * liability_SUV * liability_Under20 * (liability/len(income))
			colision_Op = colision_Under150 * colision_SUV * colision_Under20 * (colision/len(income))
	elif car_type[i] == 'Hatchback':
		if car_age[i] <= 10:
			liability_Op = liability_Under150 * liability_Hatchback * liability_Under10 * (liability/len(income))
			colision_Op = colision_Under150 * colision_Hatchback * colision_Under10 * (colision/len(income))
		elif car_age[i] > 10 and car_age[i] <= 20:
			liability_Op = liability_Under150 * liability_Hatchback * liability_Under20 * (liability/len(income))
			colision_Op = colision_Under150 * colision_Hatchback * colision_Under20 * (colision/len(income))
	elif car_type[i] == 'Sports Car':
		if car_age[i] <= 10:
			liability_Op = liability_Under150 * liability_Sports * liability_Under10 * (liability/len(income))
			colision_Op = colision_Under150 * colision_Sports * colision_Under10 * (colision/len(income))
		elif car_age[i] > 10 and car_age[i] <= 20:
			liability_Op = liability_Under150 * liability_Sports * liability_Under20 * (liability/len(income))
			colision_Op = colision_Under150 * colision_Sports * colision_Under20 * (colision/len(income))

if liability_Op > colision_Op:
	print("Insurance Type Bought is Liability")
else:
	print("Insurance Type Bought is Colision")

