# 🧬 Análisis de Datos de Salud Cardiovascular

Este proyecto realiza un análisis exploratorio de datos médicos relacionados con enfermedades cardiovasculares. Incluye limpieza de datos, cálculo de IMC, comparación categórica y visualización de correlaciones entre variables de salud.

---

## 📊 Descripción General

- **Objetivo:** Analizar la relación entre distintos indicadores de salud (colesterol, presión arterial, IMC, etc.) y la presencia de enfermedades cardiovasculares.
- **Fuente de datos:** `medical_examination.csv` — contiene información médica de pacientes como altura, peso, presión arterial, colesterol, glucosa, entre otros.
- **Procesos principales:**
  - Cálculo del IMC y creación de una columna `overweight`.
  - Normalización de variables como `cholesterol` y `gluc`.
  - Creación de un **gráfico categórico** para comparar características de salud según la presencia de enfermedad cardíaca.
  - Generación de un **mapa de calor de correlación** para visualizar relaciones entre variables numéricas.

---

## 🛠️ Herramientas y Librerías

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`

---

## 📂 Estructura del Proyecto

```bash
.
├── medical_examination.csv       # Archivo con los datos
├── main.py                       # Script principal de análisis y visualización
├── catplot.png                   # Gráfico categórico generado
├── heatmap.png                   # Mapa de calor generado
└── README.md                     # Documentación del proyecto
