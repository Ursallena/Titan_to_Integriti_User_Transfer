from striprtf.striprtf import rtf_to_text
import csv

INPUT_FILE = "input.rtf"
OUTPUT_FILE = "output.csv"

# List of lines that we ignore from the input file
NOT_USER_LINES = ["User", "Page", "Printed", "System", "Department:", "Pin", "Card", "Groups", "Alarm", "Door", "Name", "Trace", "Generated"]

# Headers of the CSV Output file
OUTPUT_HEADER = ["User Number", "First Name", "Last Name", "Access Group", "Card Number"]

output_list = []

# Reading and parsing the input
with open(INPUT_FILE, "r") as input_file:
	for line in input_file:
		line = rtf_to_text(line).split()

		if not line == []:
			if not line[0] in NOT_USER_LINES:
				temp = {"User Number" : line[0], "Card Number" : line[0]}

				# If the user had a pin code, AND has an alarm group, appends ("HAD PIN") to the last name
				# ASSUMES that the default (first) alarm group (*.1) is no access, and wont count that as a valid alarm group

				# Pin codes will have to be retrieved from titan individually, these cannot be exported in any way
				if line[-6] == "Yes":
					user_had_pin = True
				else:
					user_had_pin = False

				if line[-10] == "-" or line[-10].split(".")[-1] == "1":
					user_had_alarm_group = False
				else:
					user_had_alarm_group = True	

				# Contains no name
				if len(line) == 11:
					temp["First Name"] = "No"
					temp["Access Group"] = line[2]

					if user_had_alarm_group and user_had_pin:
						temp["Last Name"] = "Name HAD PIN"
					else:
						temp["Last Name"] = "Name"

				# Contains only one name (assumed to be first name)
				elif len(line) == 12:
					temp["First Name"] = line[1]
					temp["Access Group"] = line[3]

					if user_had_alarm_group and user_had_pin:
						temp["Last Name"] = "HAD PIN"
					else:
						temp["Last Name"] = " "

				# Contains both first and last name
				elif len(line) == 13:
					temp["First Name"] = line[1]
					temp["Access Group"] = line[4]
					
					if user_had_alarm_group and user_had_pin:
						temp["Last Name"] = line[2] + "HAD PIN"
					else:
						temp["Last Name"] = line[2]

				# First and/or last name are more than one word
				# Assume all additional words are first names, and only one word in last name
				else:
					temp["First Name"] = " ".join(line[1:(len(line) - 11)])
					temp["Access Group"] = line[-9]

					if user_had_alarm_group and user_had_pin:
						temp["Last Name"] = line[-11] + line[-5]
					else:
						temp["Last Name"] = line[-11]

				output_list.append(temp)

# Writing the output
with open(OUTPUT_FILE, "w", newline = "") as output_file:
	output_writer = csv.DictWriter(output_file, fieldnames = OUTPUT_HEADER)

	output_writer.writeheader()

	for line in output_list:
		output_writer.writerow(line)
