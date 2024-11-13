import tkinter as tk

def solarenergy(hours_of_sunlight_per_day, panel_efficiency, solar_irradience, solar_panel_area):
    power_output = solar_panel_area * solar_irradience * (panel_efficiency / 100)
    energy_production = power_output * hours_of_sunlight_per_day
    return energy_production

def calculate_energy():
    try:
        solar_panel_area = float(area_entry.get())
        solar_irradience = float(irradience_entry.get())
        panel_efficiency = float(efficiency_entry.get())
        hours_of_sunlight_per_day = float(hours_entry.get())
        
        energy_produced = solarenergy(hours_of_sunlight_per_day, panel_efficiency, solar_irradience, solar_panel_area)
        result_label.config(text=f"Energy Produced: {energy_produced:.2f} W/h")
        recalculate_button.pack(pady=10)
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

def recalculate():
    result_label.config(text="")
    recalculate_button.pack_forget()

# Create the main window
root = tk.Tk()
root.title("Solar Energy Calculator")
root.geometry("400x400")
root.configure(bg="#f4f4f4")

# Create a title label
title_label = tk.Label(root, text="Solar Energy Calculator", bg="#ffcc00", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Create and place labels and entry fields with styling
entry_frame = tk.Frame(root, bg="#f4f4f4")
entry_frame.pack(pady=10, padx=20)

tk.Label(entry_frame, text="Solar Panel Area (sq. meter):", bg="#f4f4f4", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=(5, 10), padx=(10, 10))
area_entry = tk.Entry(entry_frame, width=25, font=("Arial", 12))
area_entry.grid(row=0, column=1, pady=(5, 10), padx=(10, 10))

tk.Label(entry_frame, text="Solar Irradiance (W/sq. meter):", bg="#f4f4f4", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=(5, 10), padx=(10, 10))
irradience_entry = tk.Entry(entry_frame, width=25, font=("Arial", 12))
irradience_entry.grid(row=1, column=1, pady=(5, 10), padx=(10, 10))

tk.Label(entry_frame, text="Panel Efficiency (%):", bg="#f4f4f4", font=("Arial", 12)).grid(row=2, column=0, sticky="w", pady=(5, 10), padx=(10, 10))
efficiency_entry = tk.Entry(entry_frame, width=25, font=("Arial", 12))
efficiency_entry.grid(row=2, column=1, pady=(5, 10), padx=(10, 10))

tk.Label(entry_frame, text="Hours of Sunlight per Day (hrs):", bg="#f4f4f4", font=("Arial", 12)).grid(row=3, column=0, sticky="w", pady=(5, 10), padx=(10, 10))
hours_entry = tk.Entry(entry_frame, width=25, font=("Arial", 12))
hours_entry.grid(row=3, column=1, pady=(5, 10), padx=(10, 10))

# Create and place the calculate button with styling
calculate_button = tk.Button(root, text="Calculate Energy", command=calculate_energy, bg="#4CAF50", fg="white", font=("Arial", 14, "bold"), padx=10, pady=10)
calculate_button.pack(pady=20)

# Result label
result_label = tk.Label(root, text="", bg="#f4f4f4", font=("Arial", 14))
result_label.pack(pady=10)

# Recalculate button
recalculate_button = tk.Button(root, text="Recalculate", command=recalculate, bg="#FFA500", fg="white", font=("Arial", 14, "bold"), padx=10, pady=10)

# Run the application
root.mainloop()
