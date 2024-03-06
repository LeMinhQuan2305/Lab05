employees= ['Kelly', 'Emma']
defaults = {"designation": 'Developer',"salary":8000}
merge = {i:defaults for i in employees}
print(merge)