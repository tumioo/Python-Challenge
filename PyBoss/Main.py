# import libraries
import csv

# setting the path
csvpath = "employee_data.csv"

# declare placeholders for lists you will create from breaking up the data sets
emp_id = []
first_name = []
last_name = []
dob = []
ssn = []
state = []

# create dictionary of key: state name value: state abbreviation
us_state_abbrev = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
    'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
    'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
    'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN',
    'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV',
    'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC',
    'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA',
    'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX',
    'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV',
    'Wisconsin': 'WI', 'Wyoming': 'WY',
}

# reading the employee file in
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

    # looping through the read file
    for row in csvreader:
        # appending employee id to a new list
        emp_id.append(row[0])

        # appending first & last name to two separate lists
        name = row[1].split(" ") # splitting name by space
        first_name.append(name[0]) # appending first name
        last_name.append(name[1]) # appending last name

        # formatting & appending dob
        bdate = row[2].split("-")# splitting dob by '-'
        new_db = bdate[1] + "/" + bdate[2] + "/" + bdate[0] # formatting dob
        dob.append(new_db) # appending formatted dob

        #formatting & appending ssn
        ssn_split = row[3].split("-") # splitting ssn by '-'
        new_ssn = "***-**-" +ssn_split[2] # formatting ssn
        ssn.append(new_ssn) # appending formatted ssn

        # looping through states dictionary
        state.append(us_state_abbrev[row[4]])


# zip all of the employee lists together for iteration
employees = zip(emp_id, first_name, last_name, dob, ssn, state)

# creating the new csv file
output_file = "converted_employee_file.csv"

# opening & writing the file
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')

    # writing in headers
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    # writing data
    for employee in employees:
        writer.writerow(employee)