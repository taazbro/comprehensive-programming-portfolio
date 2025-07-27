# Setup Instructions

**Complete installation and execution guide for running all projects in the comprehensive programming portfolio.**

---

## 🚀 **Quick Start Guide**

This portfolio contains **111 files** across multiple programming languages and frameworks. Follow these instructions to set up your environment and run any project successfully.

**⏱️ Total Setup Time:** 15-30 minutes depending on your system

---

## 📋 **System Requirements**

### **💻 Operating System**
- **Windows 10/11** (Primary support)
- **macOS 10.15+** (Full compatibility)
- **Linux Ubuntu 18.04+** (Command-line focused)

### **💾 Hardware Requirements**
- **RAM:** 4GB minimum, 8GB recommended
- **Storage:** 2GB free space for all dependencies
- **CPU:** Any modern processor (projects are not CPU-intensive)

---

## 🐍 **Python Environment Setup**

### **Step 1: Python Installation**

#### **Windows:**
```bash
# Download from python.org or use winget
winget install Python.Python.3.11

# Verify installation
python --version
# Expected output: Python 3.11.x
```

#### **macOS:**
```bash
# Using Homebrew (recommended)
brew install python3

# Verify installation
python3 --version
# Expected output: Python 3.11.x
```

#### **Linux (Ubuntu/Debian):**
```bash
# Update package list
sudo apt update

# Install Python 3.11
sudo apt install python3.11 python3.11-pip python3.11-dev

# Verify installation
python3.11 --version
```

### **Step 2: Required Python Libraries**

Create a virtual environment (recommended):
```bash
# Create virtual environment
python -m venv portfolio_env

# Activate virtual environment
# Windows:
portfolio_env\Scripts\activate
# macOS/Linux:
source portfolio_env/bin/activate

# Upgrade pip
python -m pip install --upgrade pip
```

Install all required libraries:
```bash
# Computer Vision & Image Processing
pip install opencv-python==4.8.1.78

# Game Development
pip install pygame==2.5.2

# Data Visualization
pip install matplotlib==3.7.2
pip install seaborn==0.12.2

# Excel Integration
pip install openpyxl==3.1.2

# Additional utilities
pip install numpy==1.24.3
pip install pandas==2.0.3
```

### **Step 3: Verify Python Setup**

Test your installation:
```python
# Create test_setup.py and run
import cv2
import pygame
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl

print("✅ All Python libraries installed successfully!")
print(f"OpenCV version: {cv2.__version__}")
print(f"Pygame version: {pygame.version.ver}")
print(f"Matplotlib version: {matplotlib.__version__}")
```

---

## ⚡ **C++ Environment Setup**

### **Step 1: Compiler Installation**

#### **Windows:**
```bash
# Option 1: Visual Studio Build Tools
# Download from: https://visualstudio.microsoft.com/downloads/

# Option 2: MinGW-w64
# Download from: https://www.mingw-w64.org/

# Option 3: Using chocolatey
choco install mingw

# Verify installation
g++ --version
```

#### **macOS:**
```bash
# Install Xcode Command Line Tools
xcode-select --install

# Or install via Homebrew
brew install gcc

# Verify installation
g++ --version
```

#### **Linux:**
```bash
# Ubuntu/Debian
sudo apt install build-essential g++ cmake

# CentOS/RHEL
sudo yum groupinstall "Development Tools"

# Verify installation
g++ --version
```

### **Step 2: Compilation Commands**

Standard compilation for portfolio projects:
```bash
# Basic compilation
g++ -std=c++17 -Wall -Wextra -O2 source.cpp -o executable

# For encryption projects
cd cpp-assignments/02-encryption-algorithms/
g++ -std=c++17 -Wall -Wextra A01-3.cpp -o cipher_tool

# For matrix operations
cd cpp-assignments/03-linear-algebra/
g++ -std=c++17 -Wall -Wextra -I. matrix_test.cpp -o matrix_demo
```

---

## ☕ **Java Environment Setup**

### **Step 1: JDK Installation**

#### **Windows:**
```bash
# Download Oracle JDK 17+ or OpenJDK
# From: https://adoptium.net/

# Using winget
winget install Eclipse.Temurin.17.JDK

# Verify installation
java --version
javac --version
```

#### **macOS:**
```bash
# Using Homebrew
brew install openjdk@17

# Verify installation
java --version
javac --version
```

#### **Linux:**
```bash
# Ubuntu/Debian
sudo apt install openjdk-17-jdk

# CentOS/RHEL
sudo yum install java-17-openjdk-devel

# Verify installation
java --version
javac --version
```

### **Step 2: JavaFX Setup**

Download JavaFX SDK:
```bash
# Download from: https://openjfx.io/
# Extract to your preferred location

# Set JAVAFX_HOME environment variable
export JAVAFX_HOME=/path/to/javafx-sdk-17.0.2
```

### **Step 3: Compilation Commands**

```bash
# Navigate to Java project
cd java-assignments/01-gui-applications/

# Compile with JavaFX
javac --module-path $JAVAFX_HOME/lib --add-modules javafx.controls,javafx.fxml *.java

# Run JavaFX application
java --module-path $JAVAFX_HOME/lib --add-modules javafx.controls,javafx.fxml Calculator
```

---

## 🗂️ **Project Directory Structure**

Ensure your local directory matches this structure:
```
comprehensive-programming-portfolio/
├── python-assignments/
│   ├── 01-basic-concepts/
│   ├── 02-data-structures/
│   ├── 03-functions/
│   ├── 04-object-oriented-programming/
│   ├── 05-data-visualization/
│   ├── 06-web-apis-and-databases/
│   ├── 07-image-processing/
│   ├── 08-game-development/
│   ├── 09-advanced-cryptography/
│   └── 10-text-processing/
├── cpp-assignments/
├── java-assignments/
└── data-analysis/
```

---

## 🚀 **Running Individual Projects**

### **🖼️ Computer Vision Projects**

#### **Image Processing Pipeline**
```bash
cd python-assignments/07-image-processing/

# Ensure input image exists
ls Sundarban_Tiger.jpg

# Run the image processing application
python Assignment_3_Image_Processing.py

# Follow menu prompts:
# 1. Resize (choose up/down scaling)
# 2. Flip (choose horizontal/vertical/both)
# 3. Grayscale (automatic conversion)
# 4. Quit

# Generated outputs will appear in the same directory
ls *.jpg
```

**Expected outputs:**
- `resized_tiger_up_*.jpg` (enlarged images)
- `resized_tiger_down_*.jpg` (reduced images)
- `flipped_tiger_h_*.jpg` (horizontally flipped)
- `flipped_tiger_v_*.jpg` (vertically flipped)
- `flipped_tiger_both_*.jpg` (both directions)
- `grayscale_tiger_*.jpg` (grayscale versions)

### **🎮 Game Development Projects**

#### **Color-Catching Ball Game**
```bash
cd python-assignments/08-game-development/

# Run the main game
python Assignment_9.py

# Game controls:
# - Click the blue ball when background is red/green
# - Game duration: 2 minutes
# - Background changes every 5 seconds
# - Score tracked by background color
```

#### **Interactive Ball Physics**
```bash
# Run the physics demo
python mousebutton.py

# Controls:
# - Click the moving ball to increase score
# - Ball bounces off window boundaries
# - Click counter displayed in real-time
```

### **📊 Data Visualization Projects**

#### **Rainfall Statistical Analysis**
```bash
cd python-assignments/05-data-visualization/

# Ensure data files exist
ls rainfallISet1.txt rainfallSet2.txt

# Run statistical analysis
python Assignment_4_rain.py

# Generated charts:
# - comparison_plot.png (trend analysis)
# - Set1_extremes.png (outlier detection)
# - Set2_extremes.png (pattern recognition)
# - average_comparison.png (statistical summary)
```

#### **Personal Activity Dashboard**
```bash
# Run activity analysis
python visualizing_data.py

# Generated output:
# - weekly_activities_full.png (seaborn dashboard)
```

### **🔐 Cryptography Projects**

#### **RSA-Style Public Key Encryption**
```bash
cd python-assignments/09-advanced-cryptography/

# Generate keys and encrypt message
python publicKeyCipher.py

# The program will:
# 1. Generate public/private key pairs
# 2. Encrypt a sample message
# 3. Decrypt and verify the result
# 4. Save keys to files
```

#### **Columnar Transposition Cipher**
```bash
# Simple columnar cipher
python columnarTranspositionSimple_Encrypt.py

# Advanced columnar cipher with complex keys
python columnarTranspositionAdvancedKey.py

# Decryption
python columnarTranspositionSimple_Decrypt.py
```

#### **Cipher Breaking Tools**
```bash
# Language detection for cipher analysis
python detectEnglish.py

# Pattern analysis for frequency attacks
python makeWordPatterns.py

# Reverse cipher (basic)
python reverseCipher-1.py
```

### **🌐 Web & Database Projects**

#### **REST API Integration**
```bash
cd python-assignments/06-web-apis-and-databases/

# Country data retrieval (requires internet)
python Assignment_7.py

# Generated output:
# - bangladesh_details.txt (structured country report)
```

#### **Weather Database System**
```bash
# Weather data processing with SQLite
python Discussion_8.py

# Generated outputs:
# - bd_weather.db (SQLite database)
# - bangladesh_weather.txt (analysis report)
# - city_weather_info.txt (additional metrics)
```

#### **Excel File Conversion**
```bash
# Text to Excel conversion
python Excel_txt_spreadshit.py

# Converts text files to professional Excel format
```

### **⚡ C++ Projects**

#### **Encryption Algorithms**
```bash
cd cpp-assignments/02-encryption-algorithms/

# Compile encryption tool
g++ -std=c++17 -Wall -Wextra A01-3.cpp -o cipher

# Run with command-line arguments
./cipher -p "Hello World" -k 5 -e    # Encrypt
./cipher -p "Encrypted_Text" -k 5 -d # Decrypt

# Alternative implementations
g++ A01.cpp -o basic_cipher
g++ A01-2.cpp -o error_handling_cipher
g++ Modified_A01.cpp -o alternative_cipher
```

#### **Matrix Operations**
```bash
cd cpp-assignments/03-linear-algebra/

# The matrix.h header contains advanced operations
# Create a test program to use the matrix class:

# matrix_test.cpp
#include "matrix.h"
int main() {
    // Test matrix operations
    return 0;
}

# Compile and run
g++ -std=c++17 matrix_test.cpp -o matrix_demo
./matrix_demo
```

### **☕ Java Projects**

#### **JavaFX Calculator**
```bash
cd java-assignments/01-gui-applications/

# Compile JavaFX application
javac --module-path $JAVAFX_HOME/lib --add-modules javafx.controls,javafx.fxml Calculator.java

# Run the calculator
java --module-path $JAVAFX_HOME/lib --add-modules javafx.controls,javafx.fxml Calculator

# If FXML file is available:
# The calculator_fxml.txt contains the FXML layout
# Rename to Calculator.fxml and update the controller
```

---

## 🔧 **Troubleshooting Common Issues**

### **🐍 Python Issues**

#### **Import Errors**
```bash
# Error: ModuleNotFoundError: No module named 'cv2'
# Solution: Install OpenCV
pip install opencv-python

# Error: ModuleNotFoundError: No module named 'pygame'
# Solution: Install Pygame
pip install pygame

# Error: No module named 'matplotlib'
# Solution: Install visualization libraries
pip install matplotlib seaborn
```

#### **Pygame Audio Issues**
```bash
# If you encounter SDL audio errors
# Windows: Install Visual C++ Redistributable
# macOS: brew install sdl2
# Linux: sudo apt install libsdl2-dev
```

#### **OpenCV Build Issues**
```bash
# If OpenCV fails to load
# Try the headless version
pip uninstall opencv-python
pip install opencv-python-headless
```

### **⚡ C++ Issues**

#### **Compilation Errors**
```bash
# Error: g++ command not found
# Windows: Install MinGW or Visual Studio Build Tools
# macOS: xcode-select --install
# Linux: sudo apt install build-essential

# Error: C++17 features not supported
# Solution: Update compiler or use explicit flag
g++ -std=c++17 source.cpp
```

#### **Linking Errors**
```bash
# If you encounter linking issues
# Add explicit library paths
g++ -L/usr/local/lib source.cpp -o output

# For static linking
g++ -static source.cpp -o output
```

### **☕ Java Issues**

#### **JavaFX Runtime Errors**
```bash
# Error: JavaFX runtime components are missing
# Solution: Download JavaFX SDK separately
# Set module path correctly

# Alternative: Use OpenJFX from package manager
# Ubuntu: sudo apt install openjfx
# macOS: brew install openjfx
```

#### **FXML Loading Issues**
```bash
# Error: FXML file not found
# Solution: Ensure FXML file is in correct location
# Check resource path in code

# Error: Controller class not found
# Solution: Verify fx:controller attribute in FXML
```

---

## 📊 **Performance Optimization**

### **🖼️ Image Processing**
```python
# For large images, consider memory optimization
import cv2
import gc

def process_large_image(image_path):
    img = cv2.imread(image_path)
    # Process image
    processed = cv2.resize(img, (new_width, new_height))
    
    # Free memory
    del img
    gc.collect()
    
    return processed
```

### **🎮 Game Performance**
```python
# Optimize game loop for consistent framerate
clock = pygame.time.Clock()
target_fps = 60

while running:
    dt = clock.tick(target_fps)  # Delta time for frame-independent movement
    # Game logic here
```

### **📊 Data Processing**
```python
# For large datasets, use chunking
import pandas as pd

def process_large_dataset(file_path):
    chunk_size = 10000
    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        # Process chunk
        yield process_chunk(chunk)
```

---

## 🧪 **Testing Your Setup**

### **Complete Environment Test**
Create `test_environment.py`:
```python
#!/usr/bin/env python3
"""
Complete environment test for portfolio projects
"""

def test_python_libraries():
    """Test all required Python libraries"""
    try:
        import cv2
        print(f"✅ OpenCV {cv2.__version__}")
    except ImportError:
        print("❌ OpenCV not installed")
    
    try:
        import pygame
        print(f"✅ Pygame {pygame.version.ver}")
    except ImportError:
        print("❌ Pygame not installed")
    
    try:
        import matplotlib
        print(f"✅ Matplotlib {matplotlib.__version__}")
    except ImportError:
        print("❌ Matplotlib not installed")
    
    try:
        import seaborn
        print(f"✅ Seaborn {seaborn.__version__}")
    except ImportError:
        print("❌ Seaborn not installed")
    
    try:
        import openpyxl
        print(f"✅ OpenPyXL {openpyxl.__version__}")
    except ImportError:
        print("❌ OpenPyXL not installed")

def test_file_structure():
    """Test project directory structure"""
    import os
    
    required_dirs = [
        'python-assignments',
        'cpp-assignments', 
        'java-assignments',
        'data-analysis'
    ]
    
    for dir_name in required_dirs:
        if os.path.exists(dir_name):
            print(f"✅ {dir_name}/ directory found")
        else:
            print(f"❌ {dir_name}/ directory missing")

def test_sample_projects():
    """Test that sample projects can run"""
    import subprocess
    import os
    
    # Test Python basic project
    if os.path.exists('python-assignments/01-basic-concepts/test1.py'):
        try:
            result = subprocess.run(['python', 'python-assignments/01-basic-concepts/test1.py'], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                print("✅ Python projects can execute")
            else:
                print("❌ Python execution error")
        except Exception as e:
            print(f"❌ Python test failed: {e}")

if __name__ == "__main__":
    print("🔍 Testing Portfolio Environment Setup")
    print("=" * 50)
    
    test_python_libraries()
    print()
    test_file_structure()
    print()
    test_sample_projects()
    
    print("\n🎉 Environment test complete!")
```

Run the test:
```bash
python test_environment.py
```

---

## 📚 **Additional Resources**

### **📖 Documentation Links**
- [Python Official Documentation](https://docs.python.org/3/)
- [OpenCV Documentation](https://docs.opencv.org/)
- [Pygame Documentation](https://www.pygame.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/)
- [JavaFX Documentation](https://openjfx.io/)

### **🆘 Getting Help**
1. **Check error messages** carefully - they usually indicate the exact issue
2. **Verify file paths** - ensure you're in the correct directory
3. **Check dependencies** - make sure all required libraries are installed
4. **Review system requirements** - ensure your system meets minimum requirements
5. **Test with simple examples** first before running complex projects

### **🔄 Updating Dependencies**
```bash
# Update all Python packages
pip install --upgrade opencv-python pygame matplotlib seaborn openpyxl

# Check for outdated packages
pip list --outdated

# Update specific package
pip install --upgrade package_name
```

---

## 🎯 **Ready to Explore!**

Once your environment is set up, you can run any project in the portfolio:

1. **Start with simple projects** like basic Python concepts
2. **Progress to interactive projects** like games and image processing
3. **Explore advanced projects** like cryptography and data visualization
4. **Experiment with modifications** to understand the code better

**🚀 Your comprehensive programming portfolio is ready to showcase your skills!**

---

**⚠️ Note:** Some projects require internet connectivity for API calls. Ensure you have a stable internet connection when running web-related projects.
