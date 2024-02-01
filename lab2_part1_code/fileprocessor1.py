# Open the file
with open('fileprocessor.input', 'r') as file:
    # Read lines into a list
    lines = file.readlines()

print("Printing out User Data:\n")

# Process each line
for line in lines:
    # Skip lines that start with a hashtag
    if line.startswith('#'):
        print(f"{line.strip()} is skipped because it starts with a hashtag (is commented out)")
        continue

    # Split the line into a list
    user_data = line.strip().split(':')

    # Check to see expected number of items
    if len(user_data) == 4:
        # Extract user data
        username, password, userid, groupid = user_data
        print(f"The user {username} has a password of {password} and has userid {userid} and groupid {groupid}")

print("\nEnd of User Data")


