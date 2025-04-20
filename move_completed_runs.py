import os
import shutil

# Define the base directory
base_dir = "outputs/logs/video-val"
completed_dir = os.path.join(base_dir, "completed")

# Create the 'completed' directory if it doesn't exist
os.makedirs(completed_dir, exist_ok=True)

# Iterate over all entries in the base directory
for entry in os.listdir(base_dir):
    entry_path = os.path.join(base_dir, entry)

    # Skip if not a directory or if it's the 'completed' directory
    if not os.path.isdir(entry_path) or entry == "completed":
        continue

    # Iterate over all subdirectories in the date-based directory
    for sub_entry in os.listdir(entry_path):
        sub_entry_path = os.path.join(entry_path, sub_entry)

        # Check if it's a directory and contains 'motion_chunks' subdirectory
        motion_chunks_path = os.path.join(sub_entry_path, "motion_chunks")
        if os.path.isdir(sub_entry_path) and os.path.isdir(motion_chunks_path):
            # Move the completed run to the 'completed' directory
            dest_path = os.path.join(completed_dir, sub_entry)
            print(f"Moving '{sub_entry_path}' to '{dest_path}'")
            shutil.move(sub_entry_path, dest_path)
