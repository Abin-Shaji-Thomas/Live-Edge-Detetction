
# **Live Edge Detection**  
A mini-project demonstrating real-time video processing with OpenCV, showcasing edge detection on live video feeds captured from a webcam.  

## **Project Overview**  
This project utilizes the Python OpenCV library to perform edge detection on live video feeds. It demonstrates:  
- Real-time video capture and processing using OpenCV.  
- Application of the Canny edge detection algorithm.  
- Integration of HSV masking for isolating specific color ranges.  

### **Key Features**  
- **Real-time Edge Detection**: Displays edges in live video captured from a webcam.  
- **Color Masking**: Allows segmentation of red hues using HSV color space.  

---

## **Technologies Used**  
- **Python**  
- **OpenCV**  
- **NumPy**  
- **Matplotlib (optional)**  

---

## **Getting Started**  

### **Prerequisites**  
Ensure you have Python installed. Install the required libraries using pip:  
```bash  
pip install opencv-python numpy matplotlib  
```  

### **Usage**  

#### **For Edge Detection on Images**  
1. Place an image (e.g., `test.jpg`) in the same directory.  
2. Run the script `edge_detection_image.py` to detect edges in the image and visualize results.  

```bash  
python edge_detection_image.py  
```  

#### **For Real-Time Edge Detection on Live Video**  
1. Ensure your webcam is connected and accessible.  
2. Run the script `edge_detection_video.py` for live edge detection.  

```bash  
python edge_detection_video.py  
```  

---

## **Code Explanation**  

### **Image Edge Detection**  
1. Load the image using `cv2.imread`.  
2. Apply the Canny edge detection algorithm with `cv2.Canny(image, 100, 200)`.  
3. Display both the original and edge-detected images using `matplotlib`.  

### **Live Video Edge Detection**  
1. Access the webcam using `cv2.VideoCapture(0)`.  
2. Convert the frame from BGR to HSV format.  
3. Use `cv2.Canny` to detect edges in real-time.  
4. Display original and edge-detected frames side by side.  
5. Press `Esc` to exit the application.  

---

## **Output Example**  
### **Edge Detection on Image**  
- **Left**: Original Image  
- **Right**: Edge Detected Image  

### **Real-Time Edge Detection**  
- Live feed with edge detection applied, alongside the original video.  

---

## **Applications**  
- Real-time video processing for surveillance systems.  
- Preprocessing step for computer vision tasks like object detection and tracking.  

---

## **Future Enhancements**  
- Adding user controls for dynamic threshold adjustment.  
- Expanding color masking to support multiple ranges.  
- Integrating advanced edge detection techniques.  

---
