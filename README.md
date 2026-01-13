<h1 align="center">
  <img
    src="https://github.com/Taha-bouhafa1/Pedestrian-Behavior-Prediction/raw/main/Gemini_Generated_Image_5ak14w5ak14w5ak1-removebg-preview.png"
    alt="CivicVision Logo"
    width="60"
    style="vertical-align: middle; margin-right: 12px;"
  />
  AI-Based Vision System for Pedestrian Crossing Behavior Recognition
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen" />
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue" />
  <img src="https://img.shields.io/badge/TensorFlow-2.x-orange" />
  <img src="https://img.shields.io/badge/Frontend-React-blueviolet" />
  <img src="https://img.shields.io/badge/License-MIT-grey" />
</p>

**CivicVision** is an embedded computer vision system designed for intelligent transportation systems (ITS) and autonomous vehicle safety. This project implements a Deep Learning framework to detect pedestrians and predict their crossing intention in real-time by analyzing spatio-temporal features (body language, gaze, and action) using an Inflated 3D ConvNet (I3D) architecture.

---

## System Demonstration

<div align="center">
  <img
    src="https://github.com/Taha-bouhafa1/Pedestrian-Behavior-Prediction/raw/main/civicvision.png"
    alt="CivicVision Demo"
    width="85%"
  />
  <br/>
  <em>Real-time CivicVision dashboard and pedestrian behavior prediction.</em>
</div>

<br/>

To view the system in operation, including the real-time inference dashboard and decision-making engine, please refer to the demonstration video below:

<div align="center">
  <video src="https://github.com/Taha-bouhafa1/Pedestrian-Behavior-Prediction/raw/main/Screen%20Recording%202025-12-17%20044054.mp4" width="100%" controls autoplay loop muted></video>
  <br/>
  <em>If the video does not play automatically, please <a href="https://github.com/Taha-bouhafa1/Pedestrian-Behavior-Prediction/blob/main/Screen%20Recording%202025-12-17%20044054.mp4">click here to download it</a>.</em>
</div>


---

## Abstract

In the context of Smart Cities, the safety of vulnerable road users remains a critical challenge. Traditional object detection systems identify the presence of pedestrians but fail to anticipate their future actions. This project proposes a behavioral prediction module that utilizes a **Two-Stream I3D architecture** to analyze both RGB visual data and Optical Flow motion data. The system achieves a classification accuracy of **95.00%** on the JAAD dataset, significantly outperforming traditional CNN-GRU approaches in distinguishing between walking, standing, and crossing behaviors.

---

## Methodology and Architecture

The proposed solution integrates a React-based frontend dashboard with a Python-based backend for data processing and model inference simulation.

### 1. Model Architecture: I3D (Inflated 3D ConvNet)
The core predictive engine is based on the I3D architecture, which expands 2D Convolutional Neural Networks (Inception-V1) into the temporal dimension. This allows the model to learn:
* **Spatial Features:** Visual appearance of the pedestrian and environment.
* **Temporal Features:** Motion dynamics and behavioral changes over time.

### 2. Decision Engine
The system outputs a risk probability score (P_risk) which dictates the planner recommendation for the autonomous vehicle:
* **P_risk < 0.5:** Maintain trajectory (Low Risk).
* **P_risk > 0.7:** Initiate emergency braking (High Risk).

---

## Dataset

This project utilizes the **JAAD (Joint Attention in Autonomous Driving)** dataset. JAAD is a large-scale dataset focusing on pedestrian and driver behaviors in urban environments.

* **Source:** [JAAD Dataset Official Website](http://data.nvision2.eecs.yorku.ca/JAAD_dataset/)
* **Reference:** *Rasouli, A., Kotseruba, I., & Tsotsos, J. K. (2017). Are they going to cross? A benchmark dataset and baseline for pedestrian intention prediction. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition Workshops (pp. 206-213).*

---

## Experimental Results

The I3D-based approach was evaluated against baseline models (CNN+GRU) and demonstrated superior performance in action classification metrics.

| Metric | Value |
| :--- | :--- |
| **Accuracy** | **95.00%** |
| **Recall** | **91.67%** |
| **F1-Score** | **53.66%** |

*Table 1: Performance metrics of the proposed I3D model on the validation set.*

---

## Installation and Usage

### Prerequisites
* Node.js (v16+)
* Python (v3.8+)
* TensorFlow / Keras

### 1. Clone Repository
```bash
git clone [https://github.com/Taha-bouhafa1/Pedestrian-Behavior-Prediction.git](https://github.com/Taha-bouhafa1/Pedestrian-Behavior-Prediction.git)
cd Pedestrian-Behavior-Prediction
```
2. Install Frontend Dependencies
Bash

npm install

3. Data Processing
The system requires preprocessing of XML annotations to generate the dashboard timeline data. Ensure the annotations/ directory contains the relevant JAAD XML files.

```bash

python process_data.py
```
4. Launch Application
Start the development server to view the dashboard interface.

```bash
npm run dev
```
Access the application at http://localhost:5173.

### Features
Dual Input Mode: Supports offline analysis via video upload and real-time analysis via webcam feed.

Ground Truth Synchronization: Automatically maps uploaded video filenames to the annotated dataset for validation.

Real-Time Metrics: Displays system latency, inference FPS, and instantaneous crossing probability.

Dynamic Visualization: Renders bounding boxes and status indicators overlaying the video feed.

---

## Citation

```bibtex
@misc{bouhafa2025civicvision,
  author       = {Taha Bouhafa},
  title        = {CivicVision: AI-Based Vision System for Pedestrian Crossing Behavior Recognition},
  year         = {2025},
  institution  = {Abdelmalek Essaadi University, National School of Applied Sciences of Tétouan},
  supervisor   = {Prof. Aghzout Otman},
  howpublished = {\url{https://github.com/Taha-bouhafa1/Pedestrian-Behavior-Prediction}},
  note         = {Computer Vision Project}
}
```

### License
This project is licensed under the MIT License. See the LICENSE file for details.


