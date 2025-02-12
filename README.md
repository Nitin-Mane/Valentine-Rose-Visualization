# Valentine-Rose-Visualization

# 🌹 Valentine's Love Rose - A Mathematical Visualization 🌹

## 📌 Project Overview
This project is a **beautiful Valentine's Day web app** that visualizes a **3D mathematical rose animation** using **Plotly**. It also displays the **rose equation** alongside the graph, making it a perfect blend of **mathematics and romance**. 💖✨

---

## 🎨 Features
✅ **3D Rose Visualization** - Rendered using **Plotly**  
✅ **Beautiful Valentine's Theme** - Aesthetic pink-red gradient background  
✅ **Mathematical Representation** - Displays the **Rose equation** using MathJax  
✅ **Smooth UI & Responsive Design** - Graph and equation **side-by-side with proper alignment**  
✅ **Auto Scrolling & Background Animation** - Ensuring a visually stunning experience  

---

## 🛠️ Tech Stack
- **Flask** (Backend Web Framework)
- **Plotly** (3D Graph Rendering)
- **MathJax** (LaTeX Equation Rendering)
- **HTML, CSS, JavaScript** (Frontend)
- **Python** (Backend Logic)

---

## 📜 Mathematical Rose Equation

The 3D rose structure is mathematically represented as:

**Equation for x:**
$$x = 1 - \frac{1}{2} \left( \frac{5}{4} \left( 1 - \frac{\mod(3.6\theta, 2\pi)}{\pi} \right)^2 - \frac{1}{4} \right)^2$$

**Equation for y:**
$$y = A R^2 (B R - 1)^2 \sin(\phi)$$

**Equations for X, Y, and Z:**
$$X = R_2 \sin(\theta), \quad Y = R_2 \cos(\theta), \quad Z = x (R \cos(\phi) - y \sin(\phi))$$

## 🚀 How to Run the Project

### 📥 1. Clone the Repository
```bash
git clone https://github.com/Nitin-Mane/Valentine-Rose-Visualization.git
cd Valentine-Rose-Visualization
```

📦 2. Install Dependencies
```
pip install flask plotly
```

🏃‍♂️ 3. Run the Flask App
```
python main.py
```

🔗 Open http://127.0.0.1:5000/ in your browser to see the Valentine’s Love Rose!

🖥️ Project Structure

```
📂 Valentine-Rose-Visualization
│── 📄 main.py         # Flask backend script
│── 📄 templates/
│   ├── index.html     # Webpage structure (Graph + Equation)
│── 📄 README.md       # Project Documentation
```

## 📷 Screenshot Preview

![Screenshot of Valentine's Love Rose](images/screenshot.png)


