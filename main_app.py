import tkinter as tk
from tkinter import ttk, messagebox
from doubly_linked_list import PCMasterInventory

class PCMasterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PC MASTER - Elite Hardware Management")
        self.root.geometry("1000x650")
        self.root.configure(bg="#020617") # Slate 950
        
        self.inventory = PCMasterInventory()
        self.setup_styles()
        self.load_data()
        self.inventory.current = self.inventory.head
        
        self.create_layout()
        self.refresh_display()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("PC.TFrame", background="#0f172a", relief="flat")
        style.configure("Title.TLabel", background="#020617", foreground="#38bdf8", font=("Orbitron", 20, "bold"))
        style.configure("Model.TLabel", background="#0f172a", foreground="#f8fafc", font=("Verdana", 24, "bold"))

    def create_layout(self):
        # Header con el nombre solicitado
        header = tk.Frame(self.root, bg="#020617", pady=20)
        header.pack(fill=tk.X)
        tk.Label(header, text="PC MASTER", bg="#020617", fg="#38bdf8", font=("Arial Black", 28)).pack()
        tk.Label(header, text="SISTEMA DE GESTIÓN DE INVENTARIO", bg="#020617", fg="#94a3b8", font=("Consolas", 10)).pack()

        # Contenedor Central
        self.display_card = ttk.Frame(self.root, style="PC.TFrame", padding=40)
        self.display_card.pack(pady=40, padx=60, fill=tk.BOTH, expand=True)

        self.lbl_model = ttk.Label(self.display_card, text="", style="Model.TLabel")
        self.lbl_model.pack(anchor="w")

        self.lbl_specs = tk.Label(self.display_card, text="", bg="#0f172a", fg="#94a3b8", 
                                 font=("Segoe UI", 12), justify=tk.LEFT, wraplength=700)
        self.lbl_specs.pack(anchor="w", pady=25)

        self.lbl_price = tk.Label(self.display_card, text="", bg="#0f172a", fg="#22c55e", font=("Arial", 32, "bold"))
        self.lbl_price.pack(anchor="w")

        # Controles Inferiores
        btn_frame = tk.Frame(self.root, bg="#020617")
        btn_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=30)

        # Botones con estilo moderno
        btn_config = {"font": ("Segoe UI", 10, "bold"), "fg": "white", "borderwidth": 0, "padx": 25, "pady": 12, "cursor": "hand2"}
        
        tk.Button(btn_frame, text="◀ ANTERIOR", command=self.prev_pc, bg="#334155", **btn_config).pack(side=tk.LEFT, padx=60)
        tk.Button(btn_frame, text="SIGUIENTE ▶", command=self.next_pc, bg="#334155", **btn_config).pack(side=tk.LEFT)
        tk.Button(btn_frame, text="RETIRAR DE TIENDA", command=self.delete_pc, bg="#b91c1c", **btn_config).pack(side=tk.RIGHT, padx=60)

    def load_data(self):
        self.inventory.insert_at_end(1, "ASUS ROG ZEPHYRUS", "Intel i9-13900H, RTX 4090, 64GB DDR5, 2TB NVMe", "$4,200")
        self.inventory.insert_at_end(2, "RAZER BLADE 16", "Intel i9, RTX 4080, OLED 240Hz, 32GB RAM", "$3,599")
        self.inventory.insert_at_end(3, "CORSAIR VENGEANCE PC", "Ryzen 7 7800X3D, RTX 4070 Ti, Liquid Cooling", "$2,850")

    def refresh_display(self):
        if self.inventory.current:
            pc = self.inventory.current
            self.lbl_model.config(text=pc.model)
            self.lbl_specs.config(text=f"ESPECIFICACIONES TÉCNICAS:\n\n{pc.specifications}")
            self.lbl_price.config(text=pc.price)
        else:
            self.lbl_model.config(text="STOCK AGOTADO")
            self.lbl_specs.config(text="No hay más unidades en el sistema de PC MASTER.")
            self.lbl_price.config(text="--")

    def next_pc(self):
        if self.inventory.current and self.inventory.current.next:
            self.inventory.current = self.inventory.current.next
            self.refresh_display()

    def prev_pc(self):
        if self.inventory.current and self.inventory.current.prev:
            self.inventory.current = self.inventory.current.prev
            self.refresh_display()

    def delete_pc(self):
        if self.inventory.current:
            self.inventory.remove_current()
            self.refresh_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = PCMasterApp(root)
    root.mainloop()