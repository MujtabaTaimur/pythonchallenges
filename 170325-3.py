# Open the file in read mode
filename = &#39;user_data.txt&#39;
# Open the file and read all lines
with open(filename, &#39;r&#39;) as file:
    print(&quot;Displaying all records in the file:&quot;)
    for line in file:
        print(line.strip())  # strip() removes extra newlines