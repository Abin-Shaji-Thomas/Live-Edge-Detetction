
---

# **Live Edge Detection**  

This mini-project is designed for students to create a real-time edge detection system using OpenCV. The goal is to help students understand the core concepts of real-time video processing and edge detection by guiding them step-by-step to build the project themselves.  

---

## **Project Overview**  

In this project, you'll learn to:  
- Set up real-time video capture from a webcam.  
- Convert video frames into different formats (e.g., HSV).  
- Apply edge detection using the Canny algorithm.  
- Display the original and processed video feeds side by side.  

---

## **What You’ll Need**  

### **1. Tools and Libraries**  
- **Python** installed on your computer.  
- Libraries: OpenCV, NumPy, and Matplotlib.  
- A working webcam to capture live video.  

### **2. Install the Required Libraries**  
Install the following libraries using pip before starting:  
```bash  
pip install opencv-python numpy matplotlib  
```  

---

## **Steps to Build the Project**  

### **1. Import Libraries**  
Understand why OpenCV is used for image/video processing and NumPy for handling arrays.  

### **2. Load an Image for Testing**  
Start by testing edge detection on a static image before moving to live video. Use OpenCV to load an image and visualize the edges using the Canny algorithm.  

### **3. Capture Live Video from a Webcam**  
Learn how to initialize and access the webcam feed using OpenCV's `VideoCapture` function.  

### **4. Convert Video Frames to HSV Format**  
Understand why converting to the HSV color space is useful for color-based filtering and create a mask to isolate specific colors (e.g., red).  

### **5. Apply Edge Detection to Live Video Frames**  
Learn to apply the Canny edge detection algorithm on each video frame to highlight the edges in the scene.  

### **6. Display Results in Real Time**  
Display both the original video feed and the edge-detected frames side by side in separate windows.  

### **7. Add Controls to Exit the Program**  
Set up a keyboard control (e.g., Esc key) to stop the video capture and close all windows when you're done.  

---

## **Learning Outcomes**  
By the end of this project, you'll:  
- Understand the basics of real-time video processing using OpenCV.  
- Learn how to apply edge detection algorithms to images and videos.  
- Gain hands-on experience in debugging and improving your code.  

---
