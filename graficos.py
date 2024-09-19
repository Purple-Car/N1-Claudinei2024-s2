import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from entregasBasic import get_data_from_json, find_best_sequence
from entregasSwarmco import carregar_dados_json, aco

class AuctionSimulator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulação de Entregas")
        self.geometry("800x600")

        # Exibir o gráfico ao iniciar
        self.plot_results()

    def plot_results(self):
        # Algoritmo Básico
        destinations, matrix, deliveries = get_data_from_json()
        best_sequence_basic, max_profit_basic = find_best_sequence(destinations, matrix, deliveries)

        # Algoritmo ACO
        conexoes, entregas = carregar_dados_json()
        melhor_rota_aco, melhor_bonus_aco = aco(conexoes, entregas)

        fig, ax = plt.subplots()
        bars = ax.bar(['Método Básico', 'ACO'], [max_profit_basic, melhor_bonus_aco], color=['orange', 'blue'])
        ax.set_ylabel('Lucro Total')
        ax.set_title('Comparação de Lucros')

        # Adicionar os valores em cima das barras
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = AuctionSimulator()
    app.mainloop()
