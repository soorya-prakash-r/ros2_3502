# 🎯 Real-Time Color Tracker (OpenCV)

A simple Python project that tracks a specific color (red by default) in real-time using your webcam.  
It highlights the detected color region with a circle and displays its coordinates.

---

## 🧠 Features
- Real-time color detection using OpenCV  
- Tracks red color (can be changed to any color using HSV range)  
- Displays the detected area and coordinates on the live feed  
- Noise reduction using morphological operations (erode & dilate)  
- Quit anytime using the **‘q’** key  

---


---

## 🚀 How to Run
```bash
# 1. Clone the repository
git clone https://github.com/soorya-prakash-r/ros2_3502.git
cd color_tracker

# 2. Install dependencies
pip install opencv-python numpy

# 3. Run the program
python color_tracker.py
