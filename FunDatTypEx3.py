#!/usr/bin/env python3

# https://campus.datacamp.com/courses/data-types-for-data-science/fundamental-data-types?ex=3

# Create the empty list: baby_names
baby_names = []

# Loop over records
for row in records:
    # Add the name to the list
    baby_names.append(row[3])

# Sort the names in alphabetical order
for name in sorted(baby_names):
    # Print each name
    print(name)
