import tkinter as tk
from tkinter import ttk

class SistemaDomotico:
    def __init__(self, root):
        self.root = root
        self.root.title("Escenario 5: Control Domótico UNAD")
        self.root.geometry("400x500")
        
        # Variables de estado
        self.modo_automatico = tk.BooleanVar(value=False) # False = Manual, True = Auto
        self.luz_encendida = False
        self.nivel_luz_ambiente = 0
        
        # --- INTERFAZ GRÁFICA (Paso 2) ---
        
        # 1. Título y Autores 
        lbl_titulo = tk.Label(root, text="Control de Iluminación - Sala", font=("Arial", 16, "bold"))
        lbl_titulo.pack(pady=10)
        
        lbl_autores = tk.Label(root, text="Autor: Estudiante de Ingeniería", font=("Arial", 10, "italic"))
        lbl_autores.pack(pady=5)

        # 2. Indicador Visual (Bombilla) 
        self.canvas_luz = tk.Canvas(root, width=100, height=100)
        self.dibujo_luz = self.canvas_luz.create_oval(10, 10, 90, 90, fill="gray")
        self.texto_estado = self.canvas_luz.create_text(50, 50, text="OFF", fill="white")
        self.canvas_luz.pack(pady=20)
        
        # Etiqueta de intensidad actual
        self.lbl_estado_texto = tk.Label(root, text="Estado: APAGADO | Intensidad: 0%", font=("Arial", 10))
        self.lbl_estado_texto.pack(pady=5)

        # 3. Selección de Modo [cite: 45]
        frame_modos = tk.LabelFrame(root, text="Selección de Modo", padx=10, pady=10)
        frame_modos.pack(fill="x", padx=20, pady=10)
        
        rb_manual = tk.Radiobutton(frame_modos, text="Modo Manual", variable=self.modo_automatico, 
                                   value=False, command=self.actualizar_modo)
        rb_manual.pack(anchor="w")
        
        rb_auto = tk.Radiobutton(frame_modos, text="Modo Automático", variable=self.modo_automatico, 
                                 value=True, command=self.actualizar_modo)
        rb_auto.pack(anchor="w")

        # 4. Control Manual (Botón) 
        self.btn_interruptor = tk.Button(root, text="ENCENDER / APAGAR", bg="#dddddd", 
                                         command=self.accion_boton_manual)
        self.btn_interruptor.pack(fill="x", padx=20, pady=10)

        # 5. Sensor Simulado (Slider 0-100) [cite: 38, 50]
        lbl_slider = tk.Label(root, text="Simulación Sensor de Luz (0 - 100%)")
        lbl_slider.pack(pady=(10,0))
        
        self.slider = tk.Scale(root, from_=0, to=100, orient="horizontal", command=self.lectura_sensor)
        self.slider.pack(fill="x", padx=20, pady=5)

    # --- LÓGICA DE PROGRAMACIÓN (Paso 3) ---

    def actualizar_modo(self):
        """Habilita o deshabilita el botón manual según el modo."""
        if self.modo_automatico.get():
            # Modo Automático activado
            self.btn_interruptor.config(state="disabled", bg="#f0f0f0")
            self.aplicar_logica_automatica() # Revisar estado inmediatamente
        else:
            # Modo Manual activado
            self.btn_interruptor.config(state="normal", bg="#dddddd")

    def accion_boton_manual(self):
        """Lógica para el modo manual """
        if not self.modo_automatico.get():
            self.cambiar_estado_luz(not self.luz_encendida)

    def lectura_sensor(self, valor):
        """Se ejecuta cuando mueves el slider"""
        self.nivel_luz_ambiente = int(valor)
        
        # Si está en automático, aplicamos la lógica inmediatamente
        if self.modo_automatico.get():
            self.aplicar_logica_automatica()
        
        # Actualizamos texto de intensidad siempre
        self.actualizar_indicadores()

    def aplicar_logica_automatica(self):
        """Lógica para el modo automático [cite: 48]"""
        # Si la luz es baja (< 50%), encender bombilla 
        if self.nivel_luz_ambiente < 50:
            self.cambiar_estado_luz(True)
        # Si la luz es alta (> 50%), apagar bombilla 
        else:
            self.cambiar_estado_luz(False)

    def cambiar_estado_luz(self, encender):
        self.luz_encendida = encender
        self.actualizar_indicadores()

    def actualizar_indicadores(self):
        """Actualiza el color del círculo y el texto [cite: 53]"""
        estado_str = "ENCENDIDA" if self.luz_encendida else "APAGADA"
        color = "yellow" if self.luz_encendida else "gray"
        texto_color = "black" if self.luz_encendida else "white"
        
        # Actualizar gráfico
        self.canvas_luz.itemconfig(self.dibujo_luz, fill=color)
        self.canvas_luz.itemconfig(self.texto_estado, text="ON" if self.luz_encendida else "OFF", fill=texto_color)
        
        # Actualizar etiqueta de texto
        self.lbl_estado_texto.config(text=f"Estado: {estado_str} | Sensor Luz: {self.nivel_luz_ambiente}%")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = SistemaDomotico(ventana)
    ventana.mainloop()