# How to Run the Project

## 1. Requirements
Install Python and the required packages listed in `requirements.txt`.

## 2. Dataset
Place `experimental_data_M0-M9.csv` in the same directory as `main.py`.

## 3. Run the Dataset Check
Open a terminal in the project directory and execute:

```bash
python main.py
```

The program checks whether the CSV file can be loaded and displays the dataset columns and first five rows.

## 4. Current Scope
The current script only loads and checks the experimental dataset. It does not yet implement or reproduce the complete GAT–GPR–COA prediction framework described in the manuscript.
