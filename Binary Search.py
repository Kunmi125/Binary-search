# Variables
found = False
items = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
lb = 0
ub = len(items) - 1
search_item = "Strawberry"
mid = (ub + lb) // 2
# Main code

while lb <= ub:
    if items[mid] == search_item:
        print("Item has been found")
        found = True
        break
    
    elif items[mid] > search_item:
        ub = mid - 1
        mid = (ub + lb) // 2
    
    elif items[mid] < search_item:
        lb = mid + 1
        mid = (ub + lb) // 2
    
if found == False:
    print("Item was not found")
    
