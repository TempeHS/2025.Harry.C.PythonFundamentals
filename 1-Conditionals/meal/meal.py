def main():
		time = input("What's the time"):
		print(convert(time))

def convert(time):
		hours, minutes = time.split(":")
		x = float(minutes) / 60
		y = int(hours) + x
		

	if x == "__main__":

main()