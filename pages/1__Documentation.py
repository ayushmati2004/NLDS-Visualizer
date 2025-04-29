import streamlit as st
import streamlit.components.v1 as components

# Set page config for dark theme
st.set_page_config(
    page_title="Tree Algorithm Documentation",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    
    .main {
        background: #0E1117;
        color: #FAFAFA;
    }
    
    .stApp {
        background: #0E1117;
        font-family: 'Poppins', sans-serif;
    }
    
    .title {
        font-size: 2.5rem;
        color: #00FFA3;
        text-align: center;
        margin-bottom: 2rem;
        animation: fadeIn 2s;
    }
    
    .card {
        background: #1E1E1E;
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        transition: transform 0.3s ease;
        color: #FAFAFA;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0, 255, 163, 0.2);
    }
    
    .algorithm-title {
        color: #00FFA3;
        font-size: 1.8rem;
        margin-bottom: 1rem;
    }
    
    .description {
        color: #FAFAFA;
        line-height: 1.6;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    .code-block {
        background: #2C3E50;
        color: #FAFAFA;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        font-family: 'Courier New', monospace;
    }
    
    .nav-link {
        color: #00FFA3;
        text-decoration: none;
        padding: 10px 20px;
        border-radius: 5px;
        transition: all 0.3s;
        background: #1E1E1E;
        margin: 5px;
    }
    
    .nav-link:hover {
        background: #00FFA3;
        color: #0E1117;
        box-shadow: 0 0 10px rgba(0, 255, 163, 0.5);
    }
    
    .section-title {
        color: #00FFA3;
        font-size: 1.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    
    .complexity {
        background: #2C3E50;
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Page content
st.markdown('<h1 class="title">Tree-Based Algorithm Visualizer Documentation</h1>', unsafe_allow_html=True)

# Navigation
st.markdown("""
<div style="display: flex; justify-content: center; margin-bottom: 2rem;">
    <a href="app.py" class="nav-link">Back to Visualizer</a>
</div>
""", unsafe_allow_html=True)

# Introduction
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("""
<div class="description">
This documentation provides detailed information about the three tree-based algorithms implemented in the visualizer:
Tournament Trees, Decision Trees, and Cartesian Trees. Each section includes a description of the algorithm,
its implementation, and performance characteristics.
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Tournament Tree Section
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h2 class="algorithm-title">Tournament Tree</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="description">
    A Tournament Tree is a binary tree used to find the maximum (or minimum) value in a dataset. 
    It simulates a knockout tournament where each node represents a comparison between two values.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">Implementation</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="code-block">
    def build_tournament_tree(arr):
        n = len(arr)
        tree = [0] * (2 * n)
        # Fill leaves
        for i in range(n):
            tree[n + i] = arr[i]
        # Build tree
        for i in range(n - 1, 0, -1):
            tree[i] = max(tree[2 * i], tree[2 * i + 1])
        return tree
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">Performance</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="complexity">
    Time Complexity: O(n) for construction<br>
    Space Complexity: O(n)
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Decision Tree Section
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h2 class="algorithm-title">Decision Tree</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="description">
    A Decision Tree is a flowchart-like structure where each internal node represents a test on an attribute, 
    each branch represents the outcome of the test, and each leaf node represents a class label or decision.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">Implementation</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="code-block">
    def make_decision(credit_score, income, employed):
        if credit_score < 600:
            return "Rejected: Low Credit Score"
        elif income < 30000:
            return "Rejected: Low Income"
        elif not employed:
            return "Rejected: Not Employed"
        else:
            return "Approved"
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">Performance</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="complexity">
    Time Complexity: O(1) per decision<br>
    Space Complexity: O(1)
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Cartesian Tree Section
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h2 class="algorithm-title">Cartesian Tree</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="description">
    A Cartesian Tree is a binary tree derived from a sequence of numbers. It maintains the heap property 
    with respect to the values and supports efficient range minimum queries.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">Implementation</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="code-block">
    def build_cartesian_tree(arr):
        if not arr:
            return None
        
        min_val = min(arr)
        min_idx = arr.index(min_val)
        
        root = Node(min_val)
        root.left = build_cartesian_tree(arr[:min_idx])
        root.right = build_cartesian_tree(arr[min_idx + 1:])
        
        return root
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">Performance</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="complexity">
    Time Complexity: O(n log n) for construction<br>
    Space Complexity: O(n)
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 2rem; color: #7f8c8d;">
    <p>Created with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True) 