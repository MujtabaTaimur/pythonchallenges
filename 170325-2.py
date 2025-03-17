# Open the file in read mode
filename = &#39;user_data.txt&#39;
# Prompt the user for the name to search
search_name = input(&quot;Enter the name to search for: &quot;)
# Initialize a flag to check if the record is found
record_found = False
# Open and search through the file
with open(filename, &#39;r&#39;) as file:
    for line in file:
        if search_name in line:
            print(&quot;Record found:&quot;, line.strip())
            record_found = True
            break  # Exit the loop once a match is found
if not record_found:
    print(&quot;No record found with the name:&quot;, search_name)