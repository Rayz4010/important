MACHINE LEARNING II LAB PROGRAMS (BAI702)
=========================================

Each program is a standalone Python script. Open a script, copy it into your editor, and run it.

Install common packages:
    pip install numpy pandas scikit-learn matplotlib

Extra packages:
    pip install minisom       # Program 5
    pip install pgmpy         # Programs 7 and 8

DATASET OPTIONS
---------------
1. Programs 1, 2, 7, and 8 use a small inbuilt categorical Weather/Traffic dataset by default.
   You can replace it with a CSV by changing USE_CSV to True and setting CSV_PATH.
2. Programs 3, 4, and 5 use scikit-learn's inbuilt Iris dataset. It is loaded locally from
   scikit-learn; no manual download is needed.
3. Program 6 generates random samples, so no dataset is needed.

For CSV input:
- Use a CSV with column headers.
- For Programs 1 and 2, the final column is the target/class label.
- For Programs 7 and 8, use columns named Rain, Traffic, and Late, with categorical values
  such as Yes/No.
- Programs 3–5 can be adapted to numeric datasets with feature columns and a target column.
