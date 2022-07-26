import csv
import matplotlib.pyplot as plt
import pandas as pd

# Use pandas
def draw_age():
    df = pd.read_csv("https://raw.githubusercontent.com/yganalyst/data_example/main/titanic/train.csv", dtype=str)
    df[["Age"]] = df[["Age"]].astype(float)
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df.head(5)

    plt.title("Histogram", fontsize=15)
    frq, bins, fig = plt.hist(df["Age"], bins=10, alpha=1, color='r')
    plt.ylabel("Bindo", fontsize=13)
    plt.xlabel("Ages", fontsize=13)
    plt.grid()
    plt.show()
    print("*빈도 array :", frq)
    print("*구간 array :", bins)