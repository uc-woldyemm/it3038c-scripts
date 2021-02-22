import shutil
capacity, used, space = shutil.disk_usage("/")
print ("Capacity: %d GiB " % (capacity // (2**30)))
print ("Used: %d GiB " % (used // (2**30)))
print ("Space: %d GiB " % (space // (2**30)))
