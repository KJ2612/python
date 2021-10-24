import time
print("Hello friend! my name is Kush")
time.sleep(1)
name = str(input('What is your name? : '))
print(f"Hello {name}! ")
time.sleep(0.7)
w_b_m_f = str(input('Do you wanna be my friend? : '))
if w_b_m_f == "yes" or w_b_m_f == "Yes":
	country = str(input("Where are you from? : "))
	time.sleep(1)
	print(f"I m also from {country}!")
	time.sleep(0.5)
	hobby = str(input("What is your hobby? : "))
	time.sleep(1)
	print(f"""So... we are from {country} and you like {hobby}
That's soo cool bro!
I think we are gonna be the best friends.""")
else:
	print("Whatever!!!")