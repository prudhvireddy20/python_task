
## Task Overview

The goal of this task is to implement a **Python program** that arranges a set of **images of varying sizes and shapes** into a PDF in a way that **minimizes total wasted space**, while preserving each image’s **original aspect ratio**.

This task evaluates your skills in:

* **Rectangle packing algorithms**
* **Image processing**
* **PDF generation**
* **Efficient and clean code design**


## Getting Started

Follow these steps to set up and run the project:

1. **Clone the repository** to your local machine:

   ```bash
   git clone 
   cd <repository_folder>
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Generate sample images**:

   ```bash
   python sample_data_generation.py
   ```

   This will create images in the `input_images/` folder.

5. **Preprocess images**:

   * Crop to the **bounding box of visible content**
   * Remove transparent backgrounds (optional)
   * Preserve the **original aspect ratio**

6. **Pack images into PDF pages**:

   * Each page has a **fixed size** (A4, Letter, or configurable)
   * Arrange images to **minimize wasted space**

7. **Generate the output PDF**:

   * The final PDF will be saved as `output.pdf` in the project directory

---

## Starter Files

| File                        | Description                                             | Notes                                     |
| --------------------------- | ------------------------------------------------------- | ----------------------------------------- |
| `sample_data_generation.py` | Script to generate sample images                        | Run `python sample_data_generation.py`    |
| `input_images/`             | Folder containing generated images                      | Created automatically if it doesn’t exist |
| `task_1_starter_code.py`    | Starter template for implementing the packing algorithm | Use this file to implement your solution  |
| `README.md`                 | Instructions and task overview                          | Update this file if needed                |
| `requirements.txt`          | List of dependencies                                    | Install in virtual environment            |


## Steps to Implement the Task

1. Create a virtual environment and activate it.
2. Install dependencies.
3. Generate sample images using `sample_data_generation.py`.
4. Implement the image packing logic in `task_1_starter_code.py`.
5. Run your solution to generate `output.pdf`.
6. Ensure the PDF images are correctly packed, maintaining aspect ratios, and minimizing wasted space.

