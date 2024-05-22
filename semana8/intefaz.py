import tkinter as tk
from tkinter import messagebox


class MatrixMultiplierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Operaciones con Matrices")

        self.dimension_label = tk.Label(root, text="Ingrese las dimensiones de las matrices (Max 5x5):")
        self.dimension_label.pack()

        # Dimensiones para Matriz 1
        self.dimension1_frame = tk.Frame(root)
        self.dimension1_frame.pack()

        self.dimension1_label = tk.Label(self.dimension1_frame, text="Dimensiones de Matriz 1 (Filas x Columnas):")
        self.dimension1_label.grid(row=0, column=0, columnspan=2)

        tk.Label(self.dimension1_frame, text="Filas:").grid(row=1, column=0)
        self.rows1_entry = tk.Entry(self.dimension1_frame, width=5)
        self.rows1_entry.grid(row=1, column=1)

        tk.Label(self.dimension1_frame, text="Columnas:").grid(row=1, column=2)
        self.cols1_entry = tk.Entry(self.dimension1_frame, width=5)
        self.cols1_entry.grid(row=1, column=3)

        # Dimensiones para Matriz 2
        self.dimension2_frame = tk.Frame(root)
        self.dimension2_frame.pack()

        self.dimension2_label = tk.Label(self.dimension2_frame, text="Dimensiones de Matriz 2 (Filas x Columnas):")
        self.dimension2_label.grid(row=0, column=0, columnspan=2)

        tk.Label(self.dimension2_frame, text="Filas:").grid(row=1, column=0)
        self.rows2_entry = tk.Entry(self.dimension2_frame, width=5)
        self.rows2_entry.grid(row=1, column=1)

        tk.Label(self.dimension2_frame, text="Columnas:").grid(row=1, column=2)
        self.cols2_entry = tk.Entry(self.dimension2_frame, width=5)
        self.cols2_entry.grid(row=1, column=3)

        self.dimension_button = tk.Button(root, text="Confirmar Dimensiones", command=self.create_matrix_entries)
        self.dimension_button.pack()

        self.matrix_frame = tk.Frame(root)
        self.matrix_frame.pack()

        self.matrix1_entries = []
        self.matrix2_entries = []

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        self.operations_frame = tk.Frame(root)
        self.operations_frame.pack()

        self.add_button = tk.Button(self.operations_frame, text="Sumar", command=self.add_matrices)
        self.add_button.grid(row=0, column=0)

        self.subtract_button = tk.Button(self.operations_frame, text="Restar", command=self.subtract_matrices)
        self.subtract_button.grid(row=0, column=1)

        self.multiply_button = tk.Button(self.operations_frame, text="Multiplicar", command=self.multiply_matrices)
        self.multiply_button.grid(row=0, column=2)

        self.divide_button = tk.Button(self.operations_frame, text="Dividir", command=self.divide_matrices)
        self.divide_button.grid(row=0, column=3)

    def create_matrix_entries(self):
        try:
            rows1 = int(self.rows1_entry.get())
            cols1 = int(self.cols1_entry.get())
            rows2 = int(self.rows2_entry.get())
            cols2 = int(self.cols2_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese dimensiones válidas.")
            return

        if rows1 > 5 or cols1 > 5 or rows2 > 5 or cols2 > 5:
            messagebox.showerror("Error", "Las dimensiones no pueden ser mayores a 5.")
            return

        self.clear_matrix_entries()

        self.matrix1_entries = [[tk.Entry(self.matrix_frame, width=5) for _ in range(cols1)] for _ in range(rows1)]
        self.matrix2_entries = [[tk.Entry(self.matrix_frame, width=5) for _ in range(cols2)] for _ in range(rows2)]

        tk.Label(self.matrix_frame, text="Matriz 1:").grid(row=0, column=0, columnspan=cols1)
        for i in range(rows1):
            for j in range(cols1):
                self.matrix1_entries[i][j].grid(row=i + 1, column=j)

        tk.Label(self.matrix_frame, text="Matriz 2:").grid(row=rows1 + 1, column=0, columnspan=cols2)
        for i in range(rows2):
            for j in range(cols2):
                self.matrix2_entries[i][j].grid(row=i + rows1 + 2, column=j)

    def clear_matrix_entries(self):
        for widget in self.matrix_frame.winfo_children():
            widget.destroy()

    def get_matrix_from_entries(self, entries):
        matrix = []
        for row in entries:
            matrix_row = []
            for entry in row:
                value = entry.get()
                if value == "":
                    messagebox.showerror("Error", "Faltan ingresar datos en la matriz.")
                    raise ValueError("Faltan datos")
                matrix_row.append(float(value))
            matrix.append(matrix_row)
        return matrix

    def add_matrices(self):
        try:
            matrix1 = self.get_matrix_from_entries(self.matrix1_entries)
            matrix2 = self.get_matrix_from_entries(self.matrix2_entries)

            if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
                messagebox.showerror("Error", "Las matrices deben tener las mismas dimensiones para sumarlas.")
                return

            result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

            self.result_label.config(text=f"Resultado:\n{self.format_matrix(result)}")
        except ValueError as e:
            messagebox.showerror("Error", f"No se puede sumar las matrices: {e}")

    def subtract_matrices(self):
        try:
            matrix1 = self.get_matrix_from_entries(self.matrix1_entries)
            matrix2 = self.get_matrix_from_entries(self.matrix2_entries)

            if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
                messagebox.showerror("Error", "Las matrices deben tener las mismas dimensiones para restarlas.")
                return

            result = [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

            self.result_label.config(text=f"Resultado:\n{self.format_matrix(result)}")
        except ValueError as e:
            messagebox.showerror("Error", f"No se puede restar las matrices: {e}")

    def multiply_matrices(self):
        try:
            matrix1 = self.get_matrix_from_entries(self.matrix1_entries)
            matrix2 = self.get_matrix_from_entries(self.matrix2_entries)

            if len(matrix1[0]) != len(matrix2):
                messagebox.showerror("Error",
                                     "El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")
                return

            result = [
                [sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix1[0]))) for j in range(len(matrix2[0]))] for
                i in range(len(matrix1))]

            self.result_label.config(text=f"Resultado:\n{self.format_matrix(result)}")
        except ValueError as e:
            messagebox.showerror("Error", f"No se puede multiplicar las matrices: {e}")

    def divide_matrices(self):
        try:
            matrix1 = self.get_matrix_from_entries(self.matrix1_entries)
            matrix2 = self.get_matrix_from_entries(self.matrix2_entries)

            if len(matrix2) != len(matrix2[0]):
                messagebox.showerror("Error", "La segunda matriz debe ser cuadrada para calcular su inversa.")
                return

            inverse_matrix2 = self.inverse_matrix(matrix2)

            if inverse_matrix2 is None:
                messagebox.showerror("Error", "La segunda matriz no es invertible.")
                return

            result = [[sum(matrix1[i][k] * inverse_matrix2[k][j] for k in range(len(matrix1[0]))) for j in
                       range(len(inverse_matrix2[0]))] for i in range(len(matrix1))]

            self.result_label.config(text=f"Resultado:\n{self.format_matrix(result)}")
        except ValueError as e:
            messagebox.showerror("Error", f"No se puede dividir las matrices: {e}")

    def inverse_matrix(self, matrix):
        # Implementar el método de la matriz inversa
        import numpy as np
        try:
            inverse = np.linalg.inv(matrix).tolist()
            return inverse
        except np.linalg.LinAlgError:
            return None

    def format_matrix(self, matrix):
        formatted_matrix = "[\n"
        for row in matrix:
            formatted_matrix += "  " + " ".join(map(str, row)) + "\n"
        formatted_matrix += "]"
        return formatted_matrix


if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixMultiplierApp(root)
    root.mainloop()
