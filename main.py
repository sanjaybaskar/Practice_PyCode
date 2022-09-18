

even = []
for i in range (0,20):
	if i%2 == 0:
		even = even + [i]
print("Print Even numbers from 0 to 20: ",even)
print(len(even))
print(even[0::2])

print("Deleting the list now:")
del even[:]
print(even)

string1 = 'Sanjay'[:: -1]


print(string1)