import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import sys

RUTA_DEFAULT = ".\medical_examination.csv"

def draw_cat_plot(df):
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"],
    )

    df_cat = (
        df_cat.groupby(["cardio", "variable", "value"]).size().reset_index(name="total")
    )

    fig = sns.catplot(
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        data=df_cat,
        kind="bar",
        height=5,
        aspect=1,
    ).figure

    fig.savefig("catplot.png")
    return fig


def draw_heat_map(df):
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"])
        & (df["height"] >= df["height"].quantile(0.025))
        & (df["height"] <= df["height"].quantile(0.975))
        & (df["weight"] >= df["weight"].quantile(0.025))
        & (df["weight"] <= df["weight"].quantile(0.975))
    ]

    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    fig, ax = plt.subplots(figsize=(10, 8))

    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        cmap="coolwarm",
        vmax=0.3,
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5},
        ax=ax,
    )

    fig.savefig("heatmap.png")
    return fig


def main():
    if len(sys.arcv) > 2:
        print("Uso: python3 tp2.py <ruta_al_archivo> / python3 tp2.py")
        sys.exit(1)
    
    ruta = RUTA_DEFAULT
    
    if len(sys.arcv) == 2:
        ruta = sys.argc[1]
    
    df = pd.read_csv(ruta)
    df["overweight"] = ((df["weight"] / (df["height"] / 100) ** 2) > 25).astype(int)
    df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
    df["gluc"] = (df["gluc"] > 1).astype(int)
    
    draw_cat_plot(df)
    draw_heat_map(df)
    
    return 0
    
if __name__ == "__main__":
    main()
