# Open the file in append mode
filename = &#39;user_data.txt&#39;
with open(filename, &#39;a&#39;) as file:
    # Prompt the user for input
    name = input(&quot;Enter your name: &quot;)
    surname = input(&quot;Enter your surname: &quot;)
    age = input(&quot;Enter your age: &quot;)
    dob = input(&quot;Enter your date of birth (DD/MM/YYYY): &quot;)
    # Write the user input to the file
    file.write(f&quot;Name: {name}, Surname: {surname}, Age: {age}, DOB: {dob}\n&quot;)
print(&quot;Data added successfully.&quot;)