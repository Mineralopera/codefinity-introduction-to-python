# Initial items on shelf #1 (provided as a tuple)
shelf1 = ("celery", "spinach", "cucumbers")

# Items being added to the shelf #1 (provided as a list)
shelf1_update = ["tomatoes", "celery", "cilantro"]

# Converting shelf 1 update to a tuple
shelf1_update_tuple = tuple(shelf1_update)

# Concatenating tuples
shelf1_concat = shelf1 + shelf1_update_tuple

# Count of celery
celery_count = shelf1_concat.count("celery")

# First occurance of celery
celery_index = shelf1_concat.index("celery")

# Output
print(f"Updated Shelf #1: {shelf1_concat}")
print(f"Number of Celery: {celery_count}")
print(f"Celery Index: {celery_index}")