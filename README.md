Python script to transfer users from titan to integriti.

# Assumptions & Limitations
 - Assumes that Alarm Group 1 hasn't been modified from the default settings (No Access)
 - Assumes all cards are all the same type (Both data type and site code, Titan doesn't store what card is what)
 - Titan doesn't export user pins, script will append "HAD PIN" if they previously had a pin, and an alarm group that wasn't group 1.

# How to use script
1. Have user export file named as "input.rtf" in the same folder as the script
2. Run 
'Titan_To_Integriti.py'
3. "output.csv" will be generated

# How to export users from Titan:
1. Reports > Users > User Summary
2. Select range of users to export (Use "All" checkbox for all)
3. Select Print
4. Save with File Name as "input" and type as "RTF File"

# How to import CSV file into Integriti
Note: Before importing the CSV file, ensure you have setup a card template to be assigned to all the new users, as well as appropriate permission groups
1. Administration > Import Data
2. Select "output.csv"
3. Select Configuration Preset - "Define settings as you go"
4. Set CSV Settings as follows:
+ Delimiter: Comma
+ Quote Character: Double Quote
+ Tick "Has Column Headers"
5. Set "Type to Import" as "User"
6. Set each of the properties:
+ Property Name - "First Name(s)" | Import File Column Name - "First Name" | Transformation - (Leave Blank)
+ Property Name - "Second Name" | Import File Column Name - "Last Name" | Transformation - (Leave Blank)
+ Property Name - "Primary Permission Group" | Import File Column Name - "Access Group" | Transformation - "Map String To Entity" (Every access group will be displayed here, map each one of them to a permission group that you've created. Multiple access groups can be assigned to the same permission group)
+ Property Name - "Cards" (Creates a dropdown menu)
   * Property Name - "CardType" | Import File Column Name - (Leave Blank) | Transformation - "Constant Value" (Set the Value to a card template you created earlier)
   * Property Name - "CardNumber" | Import File Column Name - "Card Number" | Transformation - (Leave Blank)

7. Setup import settings as required (Nil changes required for script, default settings should be fine for new site setup)


# Tested Versions
Titan:
+ TS9002-R03.05.01
   * Build No: 30

Integriti Professional & Integriti Commissioning Software:
+ 22.2.0.20261


	