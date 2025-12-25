import tkinter as tk
from tkinter import ttk

class ControlIluminacionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Control de Iluminación - Sala")
        self.root.geometry("600x350")
        self.root.configure(bg="white")

        # Variables de estado
        self.modo_automatico = False # False = Manual, True = Automático
        self.luz_encendida = False   # Estado de la bombilla
        self.intensidad_luz = 0      # Valor del slider (sensor simulado)

        # --- TÍTULO ---
        lbl_titulo = tk.Label(root, text="Control de Iluminación - Sala", 
                              font=("Arial", 20, "bold"), fg="purple", bg="white", 
                              highlightbackground="purple", highlightthickness=1)
        lbl_titulo.pack(pady=20)

        # --- CONTENEDOR PRINCIPAL ---
        frame_main = tk.Frame(root, bg="white")
        frame_main.pack(expand=True, fill="both", padx=20)

        # COLUMNA IZQUIERDA (CONTROLES)
        frame_controls = tk.Frame(frame_main, bg="white")
        frame_controls.pack(side="left", expand=True, fill="both")

        # Botón Modo Automático
        self.btn_auto = tk.Button(frame_controls, text="Modo Automático: OFF", 
                                  font=("Arial", 12), command=self.toggle_modo,
                                  bg="#e1f5fe", fg="#0277bd", width=20)
        self.btn_auto.pack(pady=10)

        # Botón Manual (Interruptor)
        tk.Label(frame_controls, text="Control Manual", font=("Arial", 12, "bold"), fg="#8d6e63", bg="white").pack(pady=(20, 5))
        self.btn_manual = tk.Button(frame_controls, text="ENCENDER LUZ", 
                                    font=("Arial", 10, "bold"), command=self.toggle_luz_manual,
                                    bg="#fbe9e7", fg="#d84315", height=2, width=15)
        self.btn_manual.pack(pady=5)

        # Slider de Intensidad (Sensor Simulado)
        tk.Label(frame_controls, text="Intensidad de Luz Ambiental", 
                 font=("Arial", 11, "bold"), fg="#64dd17", bg="white").pack(pady=(30, 5))
        
        self.slider = ttk.Scale(frame_controls, from_=0, to=100, orient="horizontal", 
                                command=self.actualizar_sensor, length=250)
        self.slider.pack()
        
        self.lbl_valor_sensor = tk.Label(frame_controls, text="0%", bg="white")
        self.lbl_valor_sensor.pack()

        # COLUMNA DERECHA (INDICADOR VISUAL)
        frame_visual = tk.Frame(frame_main, bg="white")
        frame_visual.pack(side="right", expand=True)

        # Canvas para dibujar la bombilla
        self.canvas = tk.Canvas(frame_visual, width=150, height=200, bg="white", highlightthickness=0)
        self.canvas.pack()
        
        # Dibujar bombilla (círculo y base)
        self.bulb = self.canvas.create_oval(25, 25, 125, 125, fill="gray", outline="gray") # La luz
        self.canvas.create_rectangle(50, 125, 100, 160, fill="silver", outline="gray") # La rosca
        self.canvas.create_text(75, 180, text="Indicador Visual", font=("Arial", 12, "bold"), fill="orange")

        # --- PIE DE PÁGINA (AUTOR) ---
        lbl_autor = tk.Label(root, text="Rubén Darío De La Puente Castro\n203036_111", 
                             font=("Arial", 10), bg="white", fg="black")
        lbl_autor.pack(side="bottom", pady=10)

        # Estado inicial
        self.actualizar_interfaz()

    def toggle_modo(self):
        """Alterna entre modo Manual y Automático"""
        self.modo_automatico = not self.modo_automatico
        if self.modo_automatico:
            self.btn_auto.config(text="Modo Automático: ON", bg="#b3e5fc")
            self.btn_manual.config(state="disabled", text="BLOQUEADO")
            # Ejecutar lógica automática inmediatamente al activar
            self.logica_automatica()
        else:
            self.btn_auto.config(text="Modo Automático: OFF", bg="#e1f5fe")
            self.btn_manual.config(state="normal")
            self.actualizar_interfaz()

    def toggle_luz_manual(self):
        """Enciende o apaga la luz en modo manual"""
        if not self.modo_automatico:
            self.luz_encendida = not self.luz_encendida
            self.actualizar_interfaz()

    def actualizar_sensor(self, valor):
        """Lee el slider y ejecuta lógica si está en automático"""
        self.intensidad_luz = int(float(valor))
        self.lbl_valor_sensor.config(text=f"{self.intensidad_luz}%")
        
        if self.modo_automatico:
            self.logica_automatica()

    def logica_automatica(self):
        """
        Lógica del paso 3 según la guía:
        - Luz < 50% -> Bombilla ENCENDIDA
        - Luz > 50% -> Bombilla APAGADA
        """
        if self.intensidad_luz < 50: # 
            self.luz_encendida = True
        else: # 
            self.luz_encendida = False
        self.actualizar_interfaz()

    def actualizar_interfaz(self):
        """Actualiza el color de la bombilla y textos según el estado"""
        if self.luz_encendida:
            self.canvas.itemconfig(self.bulb, fill="orange", outline="orange") # Luz ON
            if not self.modo_automatico:
                self.btn_manual.config(text="APAGAR LUZ")
        else:
            self.canvas.itemconfig(self.bulb, fill="gray", outline="gray") # Luz OFF
            if not self.modo_automatico:
                self.btn_manual.config(text="ENCENDER LUZ")

# Ejecutar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = ControlIluminacionApp(root)
    root.mainloop()