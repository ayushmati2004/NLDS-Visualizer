import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import graphviz
import time
import sys

# Set higher recursion limit
sys.setrecursionlimit(10000)

# Set page config for dark theme
st.set_page_config(
    page_title="Tree-Based Algorithm Visualizer",
    page_icon="🌳",
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
    
    .input-section {
        background: #1E1E1E;
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        color: #FAFAFA;
    }
    
    .result-section {
        background: #2C3E50;
        color: #FAFAFA;
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
        animation: slideIn 1s;
    }
    
    .stButton>button {
        background: #00FFA3;
        color: #0E1117;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 1rem;
        transition: all 0.3s;
        font-weight: 600;
    }
    
    .stButton>button:hover {
        background: #00CC83;
        box-shadow: 0 0 10px rgba(0, 255, 163, 0.5);
    }
    
    .stSelectbox {
        background: #1E1E1E;
        border-radius: 5px;
        padding: 10px;
        color: #FAFAFA;
    }
    
    .stTextInput>div>div>input {
        background: #1E1E1E;
        color: #FAFAFA;
    }
    
    .stSlider>div>div>div>div {
        background: #00FFA3;
    }
    
    .stCheckbox>div>div>div {
        background: #1E1E1E;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    @keyframes slideIn {
        from { transform: translateY(20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
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
    
    /* Sidebar styling */
    .css-1d391kg {
        background: #1E1E1E;
    }
    
    .css-1d391kg .stSelectbox {
        background: #1E1E1E;
        color: #FAFAFA;
    }
    
    /* Graphviz styling */
    .graphviz {
        background: #1E1E1E;
        padding: 20px;
        border-radius: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Function definitions
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

def visualize_tournament_tree(tree, n):
    dot = graphviz.Digraph()
    for i in range(1, 2 * n):
        if i < n:
            dot.node(str(i), str(tree[i]))
            dot.edge(str(i), str(2 * i))
            dot.edge(str(i), str(2 * i + 1))
        else:
            dot.node(str(i), str(tree[i]))
    return dot

def make_decision(credit_score, income, employed):
    if credit_score < 600:
        return "Rejected: Low Credit Score"
    elif income < 30000:
        return "Rejected: Low Income"
    elif not employed:
        return "Rejected: Not Employed"
    else:
        return "Approved"

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_cartesian_tree(arr):
    if not arr:
        return None
    
    # Find minimum value and its index
    min_val = min(arr)
    min_idx = arr.index(min_val)
    
    # Create root node
    root = Node(min_val)
    
    # Build left and right subtrees only if they have elements
    if min_idx > 0:
        root.left = build_cartesian_tree(arr[:min_idx])
    if min_idx < len(arr) - 1:
        root.right = build_cartesian_tree(arr[min_idx + 1:])
    
    return root

def visualize_cartesian_tree(node, dot=None, parent=None, label=""):
    if dot is None:
        dot = graphviz.Digraph()
    
    if node is None:
        return dot
    
    dot.node(str(id(node)), str(node.value))
    if parent is not None:
        dot.edge(str(id(parent)), str(id(node)), label=label)
    
    visualize_cartesian_tree(node.left, dot, node, "L")
    visualize_cartesian_tree(node.right, dot, node, "R")
    
    return dot

# Main application
st.markdown('<h1 class="title">Tree-Based Algorithm Visualizer</h1>', unsafe_allow_html=True)

# Navigation
st.markdown("""
<div style="display: flex; justify-content: center; margin-bottom: 2rem;">
    <a href="https://tree-algorithm-visualizer.streamlit.app/" class="nav-link">View Documentation</a>
</div>
""", unsafe_allow_html=True)

# Sidebar for algorithm selection
algorithm = st.sidebar.selectbox(
    "Select Algorithm",
    ["Tournament Tree", "Decision Tree", "Cartesian Tree"]
)

# Common input section
st.markdown('<div class="input-section">', unsafe_allow_html=True)
st.header("Input Data")
if algorithm == "Tournament Tree" or algorithm == "Cartesian Tree":
    input_data = st.text_input("Enter numbers (comma-separated)", "5,3,8,1,9,4,7")
    numbers = [int(x.strip()) for x in input_data.split(",")]
elif algorithm == "Decision Tree":
    st.write("Sample Decision Tree for Loan Approval")
    st.write("Features: Credit Score, Income, Employment Status")
st.markdown('</div>', unsafe_allow_html=True)

# Algorithm implementations
if algorithm == "Tournament Tree":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Tournament Tree")
    tree = build_tournament_tree(numbers)
    st.graphviz_chart(visualize_tournament_tree(tree, len(numbers)))
    st.markdown('<div class="result-section">', unsafe_allow_html=True)
    st.write("Maximum value:", tree[1])
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif algorithm == "Decision Tree":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Decision Tree")
    # Sample input form
    credit_score = st.slider("Credit Score", 300, 850, 700)
    income = st.slider("Annual Income ($)", 0, 200000, 50000)
    employed = st.checkbox("Currently Employed", True)
    
    result = make_decision(credit_score, income, employed)
    st.markdown('<div class="result-section">', unsafe_allow_html=True)
    st.write("Decision:", result)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Visualize decision tree
    dot = graphviz.Digraph()
    dot.node("root", "Credit Score > 600?")
    dot.node("left", "Reject")
    dot.node("right", "Income > $30k?")
    dot.node("right_left", "Reject")
    dot.node("right_right", "Employed?")
    dot.node("final_reject", "Reject")
    dot.node("final_approve", "Approve")
    
    dot.edge("root", "left", "No")
    dot.edge("root", "right", "Yes")
    dot.edge("right", "right_left", "No")
    dot.edge("right", "right_right", "Yes")
    dot.edge("right_right", "final_reject", "No")
    dot.edge("right_right", "final_approve", "Yes")
    
    st.graphviz_chart(dot)
    st.markdown('</div>', unsafe_allow_html=True)

elif algorithm == "Cartesian Tree":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Cartesian Tree")
    tree = build_cartesian_tree(numbers)
    st.graphviz_chart(visualize_cartesian_tree(tree))
    
    # Range Minimum Query
    st.subheader("Range Minimum Query")
    start = st.slider("Start Index", 0, len(numbers)-1, 0)
    end = st.slider("End Index", 0, len(numbers)-1, len(numbers)-1)
    
    if start <= end:
        min_val = min(numbers[start:end+1])
        st.markdown('<div class="result-section">', unsafe_allow_html=True)
        st.write(f"Minimum value in range [{start}, {end}]: {min_val}")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Performance comparison section
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("Performance Comparison")
if st.button("Run Performance Test"):
    test_data = list(range(100, 0, -1))  # Reduced size for performance test
    
    # Tournament Tree
    start_time = time.time()
    build_tournament_tree(test_data)
    tournament_time = time.time() - start_time
    
    # Cartesian Tree
    start_time = time.time()
    build_cartesian_tree(test_data)
    cartesian_time = time.time() - start_time
    
    # Decision Tree (simple comparison)
    start_time = time.time()
    for _ in range(1000):
        make_decision(700, 50000, True)
    decision_time = time.time() - start_time
    
    st.markdown('<div class="result-section">', unsafe_allow_html=True)
    st.write("Execution times for 100 elements:")
    st.write(f"Tournament Tree: {tournament_time:.6f} seconds")
    st.write(f"Cartesian Tree: {cartesian_time:.6f} seconds")
    st.write(f"Decision Tree (1000 decisions): {decision_time:.6f} seconds")
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 2rem; color: #7f8c8d;">
    <p>Created with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True) 