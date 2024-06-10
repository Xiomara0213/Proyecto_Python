import sys
import os #Imoportar para interactuar con el Sistema Operativo
# Agrega el directorio que contiene 'analysis.py' al sys.path
current_dir = os.path.dirname(__file__)
analysis_dir = os.path.join(current_dir, '..', 'analysis')
sys.path.append(os.path.abspath(analysis_dir))
from analysis import load_data, clean_data, analyze_data, save_clean_data
import argparse
import tkinter as tk
from tkinter import messagebox, filedialog
import matplotlib.pyplot as plt

def plot_histogram(df):
    plt.hist(df['price'], bins=20, edgecolor='black')
    plt.title('Distribución de Precios')
    plt.xlabel('Precio')
    plt.ylabel('Frecuencia')
    plt.show()

def run_cli(args):
    data_path = args.data_path
    if data_path is None:
        print("Error: data_path no puede ser None. Proporcione un archivo de datos válido.")
        return
    df = load_data(data_path)
    df_cleaned = clean_data(df)
    analyze_data(df_cleaned)
    if args.output_path:
        save_clean_data(df_cleaned, args.output_path)

def run_gui():
    def open_file():
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            df = load_data(file_path)
            df_cleaned = clean_data(df)
            summary_stats = analyze_data(df_cleaned)
            messagebox.showinfo("Summary Statistics", str(summary_stats))
            plot_histogram(df_cleaned)

    root = tk.Tk()
    root.title("Data Analysis Tool")

    btn_open = tk.Button(root, text="Open CSV File", command=open_file)
    btn_open.pack()

    root.mainloop()

def main():
    parser = argparse.ArgumentParser(description="Data Analysis Tool")
    parser.add_argument("data_path", type=str, nargs='?', help="Path to CSV data file")
    parser.add_argument("--gui", action="store_true", help="Run the GUI")
    parser.add_argument("--output_path", type=str, help="Path to save cleaned data")
    args = parser.parse_args()

    if args.gui:
        run_gui()
    else:
        run_cli(args)

if __name__ == "__main__":
    main()
    
# Funciona con una ruta absoluta = python src/main/main.py data/raw/products.csv --output_path data/processed/cleaned_products.csv