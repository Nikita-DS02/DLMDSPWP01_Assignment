# DLMDSPWP01 Assignment - Function Selection Using Python


# 📈 Optimizing Function Selection Using Python  
## An Application of Least Squares Method for Ideal Function Approximation

### 🔍 Overview

This project demonstrates the use of the **Least Squares Method** to select the best-fitting ideal functions from a given dataset of 50 candidates. Using object-oriented Python, it:

- Loads and stores training, ideal, and test datasets in a **SQLite database**
- Applies **least square minimization** to match training data with ideal functions
- Matches **test data** points with mapped ideal functions based on the √2 deviation rule
- Visualizes the relationships and deviations using **Bokeh**
- Follows a **professional Git workflow** including `develop` and `feature` branching

---

### 📁 Project Structure

<pre>
DLMDSPWP01_Assignment/
├── src/                       # Core implementation
│   ├── database.py            # Handles SQLite interactions
│   ├── function_selector.py   # Ideal function selection (LSE)
│   ├── test_matcher.py        # Matching test data with √2 rule
│   ├── visualizer.py          # Bokeh-based HTML visualizations
│   └── main.py                # Entry point to run full pipeline
├── tests/                     # All unit tests (unittest framework)
│   ├── test_database.py
│   ├── test_function_selector.py
│   └── test_matcher.py
├── Data/                      # Raw CSV data files
│   ├── train.csv
│   ├── ideal.csv
│   └── test.csv
├── project_data.db            # SQLite database used for the project
├── results_visualization.html # Final plotted output (Bokeh)
├── requirements.txt           # Python dependencies
└── README.md                  # Project overview and setup
</pre>

---

### 📌 Technologies Used

- **Python 3.10+**
- **pandas** for data manipulation
- **SQLAlchemy** for database interaction
- **Bokeh** for interactive visualization
- **pytest**  for unit testing
- **Git** + **GitHub** for version control

---

### 🧠 Core Workflow

1. **Data Load**  
   Load 3 CSVs into an SQLite database.

2. **Function Selection**  
   Use least squares error to select best matching ideal function for each training function.

3. **Test Matching**  
   Match each test point to ideal function within threshold (√2 × max training deviation).

4. **Visualization**  
   Show training vs ideal functions and matched test points using Bokeh.

---

### 🔧 How to Run the Project

1. **Clone the repository**
   ```bash
   git clone -b develop https://github.com/Nikita-DS02/DLMDSPWP01_Assignment.git
   cd DLMDSPWP01_Assignment

2. **Create a virtual environment**
     ```bash
    python3 -m venv .venv
    source .venv/bin/activate

3. **Install dependencies**
     ```bash
    pip install -r requirements.txt

4. **Run the project**  
     ```bash
    python src/main.py

5. **View the visualization**
     ```bash
    Open results_visualization.html in your browser

---

### ✅ Unit Testing

Run all tests using:

```bash
python3 -m unittest discover tests/
```

---

### 🔐 Git Workflow Practiced

- Feature branching (`feature/...`)
- Pull requests, merges, clean commit history
- `.gitignore` included for Python best practices

---

### Features Implemented
🗂️ SQLite DB creation and multi-table storage
📉 Ideal function selection via least squares error minimization
📊 Visual mapping of training vs. ideal vs. test data
✅ Test point assignment with √2 deviation threshold
⚙️ Object-oriented modular design with inheritance and exception handling
🧪 Unit test-ready structure
💡 Well-commented code and docstrings
🔁 Real-world Git workflow with pull request and branch management

---

### What I Learned
This project gave me hands-on experience with data approximation, modular Python coding, version control, and collaborative Git workflows. It strengthened my problem-solving mindset and helped me understand how theory translates into practical solutions.

---

### License
This project is submitted as part of the IU assignment DLMDSPWP01 and is not intended for commercial use.

---

### Note
The requirements.txt file is kept minimal and includes only the direct dependencies used in this project. No unnecessary packages or transitive dependencies are listed.