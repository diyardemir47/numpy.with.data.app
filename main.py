import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

class DataAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Basit Veri Analizi Aracı")
        self.root.geometry("600x300")  # Ekran boyutunu belirle

        self.data = None
        self.data_loaded = False

        # Navbar
        self.navbar = tk.Frame(root)
        self.navbar.pack(pady=10)

        self.load_button = tk.Button(self.navbar, text="Veri Kümesini Yükle", command=self.load_data)
        self.load_button.pack(side=tk.LEFT, padx=10)

        self.analyze_button = tk.Button(self.navbar, text="Temel Analiz Yap", command=self.perform_analysis)
        self.analyze_button.pack(side=tk.LEFT, padx=10)

        self.visualize_button = tk.Button(self.navbar, text="Veriyi Görselleştir", command=self.visualize_data)
        self.visualize_button.pack(side=tk.LEFT, padx=10)

        # Intro ekranı
        self.intro_label = tk.Label(root, text="Hoş Geldiniz!", font=("Helvetica", 24, "bold"))
        self.intro_label.pack(pady=50)

    def load_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Dosyaları", "*.csv")])
        if file_path:
            try:
                self.data = np.loadtxt(file_path, delimiter=',')
                messagebox.showinfo("Başarılı", "Veri yüklendi.")
                self.data_loaded = True
            except Exception as e:
                messagebox.showerror("Hata", f"Veri yüklenirken bir hata oluştu:\n{e}")

    def perform_analysis(self):
        if self.data is not None:
            mean = np.mean(self.data)
            median = np.median(self.data)
            variance = np.var(self.data)
            std_dev = np.std(self.data)
            min_val = np.min(self.data)
            max_val = np.max(self.data)

            result = f"Ortalama: {mean:.2f}\nMedyan: {median:.2f}\nVaryans: {variance:.2f}" \
                     f"\nStandart Sapma: {std_dev:.2f}\nMinimum Değer: {min_val:.2f}\nMaksimum Değer: {max_val:.2f}"

            result_window = tk.Toplevel(self.root)
            result_window.title("Analiz Sonuçları")
            result_label = tk.Label(result_window, text=result)
            result_label.pack(padx=20, pady=10)
        else:
            messagebox.showwarning("Uyarı", "Lütfen önce bir veri kümesi yükleyin.")

    def visualize_data(self):
        if self.data is not None:
            visualize_window = tk.Toplevel(self.root)
            visualize_window.title("Veri Görselleştirme")

            fig_hist = Figure(figsize=(5, 4), dpi=100)
            ax_hist = fig_hist.add_subplot(111)
            ax_hist.hist(self.data, bins=20, alpha=0.7)
            ax_hist.set_title('Veri Histogramı')
            ax_hist.set_xlabel('Değer')
            ax_hist.set_ylabel('Frekans')
            canvas_hist = FigureCanvasTkAgg(fig_hist, master=visualize_window)
            canvas_hist.get_tk_widget().pack()

            def save_histogram():
                file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Dosyaları", "*.png")])
                if file_path:
                    fig_hist.savefig(file_path)

            save_button = tk.Button(visualize_window, text="Histogramı Kaydet", command=save_histogram)
            save_button.pack()

            toolbar = NavigationToolbar2Tk(canvas_hist, visualize_window)
            toolbar.update()
            canvas_hist.get_tk_widget().pack()

        else:
            messagebox.showwarning("Uyarı", "Lütfen önce bir veri kümesi yükleyin.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DataAnalysisApp(root)
    root.mainloop()
