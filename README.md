# Tree-Based Algorithm Visualizer

A web application that demonstrates three different tree-based algorithms:
- Tournament Trees
- Decision Trees
- Cartesian Trees

## Live Demo

Check out the live demo of the project at: [Tree-Based Algorithm Visualizer](https://nlds-tree-visualizer.netlify.app/)

## Features
- Interactive visualization of tree structures
- Step-by-step demonstration of each algorithm
- Performance comparison between algorithms
- User-friendly interface with Streamlit

## Setup
1. Install Python 3.8 or higher
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Install Graphviz (required for tree visualizations):
   - Windows: Download and install from [Graphviz website](https://graphviz.org/download/)
   - Linux: `sudo apt-get install graphviz`
   - Mac: `brew install graphviz`

## Running the Application
1. Navigate to the project directory
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
3. Open your web browser and go to the URL shown in the terminal (usually http://localhost:8501)

## Usage
1. Select an algorithm from the sidebar
2. For Tournament and Cartesian Trees:
   - Enter comma-separated numbers
   - View the tree visualization
3. For Decision Tree:
   - Adjust the input parameters using sliders
   - See the decision path and result
4. Use the "Run Performance Test" button to compare algorithm performance

## Algorithm Descriptions

### Tournament Tree
- Used to find the maximum value in a dataset
- Simulates a knockout tournament structure
- Each node represents a comparison between two values

### Decision Tree
- Demonstrates a simple loan approval system
- Uses three criteria: credit score, income, and employment status
- Shows how decisions are made based on multiple factors

### Cartesian Tree
- Organizes numbers in a binary tree structure
- Supports efficient range minimum queries
- Maintains heap property with respect to values 
