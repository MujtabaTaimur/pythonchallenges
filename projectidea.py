def add_student():
pass
def grades():
pass
def search_student():
pass
def calculate():
pass
def show_students():
pass

def menu():
print(&quot;1. Add a Student&quot;)
print(&quot;2. Record Student Grades&quot;)
print(&quot;3. Search for one Student&quot;)
print(&quot;4. Calculate average grades&quot;)
print(&quot;5. Show all students and grades&quot;)
print(&quot;6. Exit&quot;)
try:
choice = int(input(&quot;Please select one option&quot;))
if (choice &lt; 1) or (choice &gt; 6):
print(&quot;Invalid Option&quot;)
print(&quot;Press Enter to come back to Menu&quot;)
input()
menu()
else:
if choice == 1:
add_student()
elif choice == 2:
grades()
elif choice == 3:

search_student()
elif choice == 4:
calculate()
elif choice == 5:
show_students()
else:
print(&quot;Good Bye&quot;)
except ValueError:
print(&quot;You MUST input a number from 1 to 6&quot;)
print(&quot;Press Enter to come back to Menu&quot;)
input()
menu()

#Main program
menu()