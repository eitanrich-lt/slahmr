import os
import subprocess
from pathlib import Path

# Paths
video_dir = Path("/home/erichardson/data/pose_detection_2k/videos")
image_root = Path("/home/erichardson/data/pose_detection_2k/images")
image_root.mkdir(parents=True, exist_ok=True)

# Extraction parameters
fps = 25

# Process each video
for video_path in video_dir.glob("*.mp4"):
    seq_name = video_path.stem  # basename without extension
    output_dir = image_root / seq_name
    output_dir.mkdir(parents=True, exist_ok=True)

    output_pattern = output_dir / "%06d.jpg"
    if any(output_dir.glob("*.jpg")):
        print(f"[SKIP] {seq_name} already extracted.")
        continue

    print(f"[EXTRACT] {seq_name} -> {output_dir}")
    cmd = [
        "ffmpeg",
        "-i", str(video_path),
        "-vf", f"fps={fps}",
        str(output_pattern)
    ]
    result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    if result.returncode != 0:
        print(f"[ERROR] Failed to extract frames for {seq_name}")
