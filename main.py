import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import sys

# CONSTANTES
RUTA_DEFAULT = r".\medical_examination.csv"
CARDIO = "cardio"
CHOLESTEROL = "cholesterol"
GLUC = "gluc"
SMOKE = "smoke"
ALCO = "alco"
ACTIVE = "active"
OVERWEIGHT = "overweight"
VARIABLE = "variable"
VALUE = "value"
TOTAL = "total"
HEIGHT = "height"
WEIGHT = "weight"
AP_LO = "ap_lo"
AP_HI = "ap_hi"


def draw_cat_plot(df):
    df_cat = pd.melt(
        df,
        id_vars=[CARDIO],
        value_vars=[CHOLESTEROL, GLUC, SMOKE, ALCO, ACTIVE, OVERWEIGHT],
    )

    df_cat = (
        df_cat.groupby([CARDIO, VARIABLE, VALUE]).size().reset_index(name=TOTAL)
    )

    fig = sns.catplot(
        x=VARIABLE,
        y=TOTAL,
        hue=VALUE,
        col=CARDIO,
        data=df_cat,
        kind="bar",
        height=5,
        aspect=1,
    ).figure

    fig.savefig("catplot.png")
    return fig


def draw_heat_map(df):
    df_heat = df[
        (df[AP_LO] <= df[AP_HI])
        & (df[HEIGHT] >= df[HEIGHT].quantile(0.025))
        & (df[HEIGHT] <= df[HEIGHT].quantile(0.975))
        & (df[WEIGHT] >= df[WEIGHT].quantile(0.025))
        & (df[WEIGHT] <= df[WEIGHT].quantile(0.975))
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
    if len(sys.argv) > 2:
        print("Uso: python3 tp2.py <ruta_al_archivo> o python3 tp2.py")
        sys.exit(1)
    
    ruta = RUTA_DEFAULT
    
    if len(sys.argv) == 2:
        ruta = sys.argv[1]
    
    df = pd.read_csv(ruta)
    
    df[OVERWEIGHT] = ((df[WEIGHT] / (df[HEIGHT] / 100) ** 2) > 25).astype(int)
    df[CHOLESTEROL] = (df[CHOLESTEROL] > 1).astype(int)
    df[GLUC] = (df[GLUC] > 1).astype(int)
    
    draw_cat_plot(df)
    draw_heat_map(df)
    
    return 0

if __name__ == "__main__":
    main()
