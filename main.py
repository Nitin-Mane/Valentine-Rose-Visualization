from flask import Flask, render_template
import numpy as np
import plotly.graph_objects as go

app = Flask(__name__)

def generate_rose_petal():
    n = 800
    A = 1.995653
    B = 1.27689
    C = 8
    petalNum = 3.6
    
    r = np.linspace(0, 1, n)
    theta = np.linspace(-2, 20 * np.pi, n)
    R, THETA = np.meshgrid(r, theta)
    
    x = 1 - (1/2) * ((5/4) * (1 - np.mod(petalNum * THETA, 2 * np.pi) / np.pi)**2 - 1/4)**2
    phi = (np.pi / 2) * np.exp(-THETA / (C * np.pi))
    y = A * (R**2) * (B * R - 1)**2 * np.sin(phi)
    R2 = x * (R * np.sin(phi) + y * np.cos(phi))
    X = R2 * np.sin(THETA)
    Y = R2 * np.cos(THETA)
    Z = x * (R * np.cos(phi) - y * np.sin(phi))
    
    return X, Y, Z

@app.route('/')
def index():
    X, Y, Z = generate_rose_petal()
    
    fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale=[[0, 'red'], [1, 'darkred']])])
    fig.update_layout(title="Valentine's Love Rose",
                      scene=dict(xaxis_title='X',
                                 yaxis_title='Y',
                                 zaxis_title='Z',
                                 camera=dict(eye=dict(x=-1.5, y=-1.5, z=1.5))),
                      margin=dict(l=0, r=0, b=0, t=40))
    
    romantic_text = """
    <b>"Love is like a mathematical equation – it balances everything perfectly."</b><br>
    Roses symbolize passion, beauty, and eternal affection.<br>
    <i>If you were a function, you'd be my limit – I'd approach you infinitely!</i>
    """
    
    rose_equation = r"""
\[
x = 1 - \frac{1}{2} \left( \frac{5}{4} \left( 1 - \frac{\mod(3.6\theta, 2\pi)}{\pi} \right)^2 - \frac{1}{4} \right)^2
\]

\[
y = A R^2 (B R - 1)^2 \sin(\phi)
\]

\[
X = R_2 \sin(\theta), \quad Y = R_2 \cos(\theta), \quad Z = x (R \cos(\phi) - y \sin(\phi))
\]
"""

    
    graph_html = fig.to_html(full_html=False)
    return render_template('index.html', graph_html=graph_html, romantic_text=romantic_text, rose_equation=rose_equation)

if __name__ == '__main__':
    app.run(debug=True)
