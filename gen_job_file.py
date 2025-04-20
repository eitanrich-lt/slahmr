import os

# Define the path to your videos directory
videos_dir = '/home/erichardson/data/pose_detection_2k/videos'

# Define the output job file path
job_file_path = 'slahmr_jobs.txt'

# List all .mp4 files in the videos directory
video_files = [f for f in os.listdir(videos_dir) if f.endswith('.mp4')]

# Extract the base names (without extension)
base_names = [os.path.splitext(f)[0] for f in video_files]

# Write the base names to the job file
with open(job_file_path, 'w') as job_file:
    for name in base_names:
        job_file.write(f"{name}\n")

print(f"Job file '{job_file_path}' has been created with {len(base_names)} entries.")
