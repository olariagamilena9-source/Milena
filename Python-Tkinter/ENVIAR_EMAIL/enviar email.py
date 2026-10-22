import os
import sys
from email.message import EmailMessage
import smtplib
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# ----------------- CONFIGURACIÓN DE PALETA MORADA -----------------
COLOR_FONDO = "#2A0845"         # Morado oscuro de fondo
COLOR_TARJETA = "#3B155B"       # Morado medio para paneles
COLOR_TEXTO = "#FFFFFF"         # Blanco para el texto
COLOR_ACCENTO = "#8E2DE2"       # Violeta brillante
COLOR_BOTON = "#4A154B"         # Morado profundo para botones
COLOR_ENTRADA = "#1D0533"       # Morado muy oscuro para cajas de texto

# ----------------- VENTANA PRINCIPAL -----------------
ventana = Tk()
ventana.title("Aplicación de Mensajería")
ventana.geometry("420x620")
ventana.resizable(0, 0)
ventana.config(bg=COLOR_FONDO)

# Variables
remitente_email = "olariagamilena0607@gmail.com"
asunto_var = StringVar(ventana)
opcion_destinatario_var = StringVar(ventana)

# Lista de emails 
LISTA_EMAILS = [
    "Seleccionar contactos: ",
    "fjcoronati@gmail.com",                 
    "Mfedullo@gmail.com"                    
]

opcion_destinatario_var.set(LISTA_EMAILS[0])

# ----------------- FUNCIÓN PARA RUTA DE RECURSOS (PyInstaller) -----------------
def obtener_ruta_recurso(ruta_relativa):
    """ Obtiene la ruta absoluta del recurso, compatible con PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, ruta_relativa)

# ----------------- LÓGICA DEL MENÚ DE DESTINATARIOS -----------------
def seleccionar_email_menu(seleccion):
    if seleccion == "Escribir manualmente / Otro":
        entry_destinatario.delete(0, END)
        entry_destinatario.config(state="normal")
    else:
        entry_destinatario.delete(0, END)
        entry_destinatario.insert(0, seleccion)

# ----------------- FUNCIÓN ENVIAR CORREO -----------------
def enviar_email():
    correo_destino = entry_destinatario.get().strip()
    asunto_texto = asunto_var.get().strip()
    cuerpo_mensaje = mensaje_text.get(1.0, END).strip()

    if not correo_destino or not asunto_texto or not cuerpo_mensaje:
        messagebox.showwarning("Campos Incompletos", "Por favor completa todos los campos antes de enviar.")
        return

    try:
        # Construir estructura del correo
        email = EmailMessage()
        email["From"] = remitente_email
        email["To"] = correo_destino
        email["Subject"] = asunto_texto
        email.set_content(cuerpo_mensaje)

        # Conexión SMTP SSL con Gmail
        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtp.login(remitente_email, "waus elzx wvhh wouh")
        smtp.sendmail(remitente_email, correo_destino, email.as_string())
        
        messagebox.showinfo("ÉXITO", f"El correo se envió correctamente a:\n{correo_destino}")
        smtp.quit()

        # Limpiar formulario
        asunto_var.set("")
        mensaje_text.delete(1.0, END)
        entry_destinatario.delete(0, END)
        opcion_destinatario_var.set(LISTA_EMAILS[0])

    except Exception as e:
        messagebox.showerror("ERROR DE ENVÍO", f"No se pudo enviar el correo:\n{e}")

# ----------------- INTERFAZ GRÁFICA (TKINTER) -----------------

# Título
Label(
    ventana,
    text="ENVIAR CORREO VÍA GMAIL",
    fg=COLOR_TEXTO,
    bg=COLOR_FONDO,
    font=("Arial", 14, "bold"),
    pady=10
).pack()

# Carga de Imagen
ruta_img = obtener_ruta_recurso("minion morado.jpg")
imagen = Image.open(ruta_img)
imagen_res = imagen.resize((120, 85))
render_img = ImageTk.PhotoImage(imagen_res)
label_img = Label(ventana, image=imagen, bg=COLOR_FONDO)
label_img.image = render_img
label_img.pack(pady=2)

# Banner del Remitente
Label(
    ventana,
    text=f"Remitente: {remitente_email}",
    fg="#D1C4E9",
    bg=COLOR_TARJETA,
    font=("Arial", 9, "bold"),
    padx=10,
    pady=4
).pack(pady=8)

# Panel Contenedor de Entradas
frame_form = Frame(ventana, bg=COLOR_FONDO)
frame_form.pack(padx=25, pady=5, fill="both", expand=True)

#Menú Desplegable (OptionMenu)
Label(frame_form, text="Seleccionar Destinatario:", fg=COLOR_TEXTO, bg=COLOR_FONDO, font=("Arial", 9, "bold"), anchor="w").pack(fill="x")
menu_emails = OptionMenu(frame_form, opcion_destinatario_var, *LISTA_EMAILS, command=seleccionar_email_menu)
menu_emails.config(bg=COLOR_TARJETA, fg="white", activebackground=COLOR_ACCENTO, activeforeground="white", highlightthickness=0, font=("Arial", 9))
menu_emails["menu"].config(bg=COLOR_TARJETA, fg="white")
menu_emails.pack(fill="x", pady=(2, 8))

#Entrada Manual de Destinatario
Label(frame_form, text="Escribir correo destinatario:", fg=COLOR_TEXTO, bg=COLOR_FONDO, font=("Arial", 9, "bold"), anchor="w").pack(fill="x")
entry_destinatario = Entry(
    frame_form,
    bg=COLOR_ENTRADA,
    fg="white",
    insertbackground="white",
    relief="solid",
    bd=1,
    font=("Arial", 10)
)
entry_destinatario.pack(fill="x", pady=(2, 8))

# Asunto
Label(frame_form, text="Asunto:", fg=COLOR_TEXTO, bg=COLOR_FONDO, font=("Arial", 9, "bold"), anchor="w").pack(fill="x")
Entry(
    frame_form,
    textvariable=asunto_var,
    bg=COLOR_ENTRADA,
    fg="white",
    insertbackground="white",
    relief="solid",
    bd=1,
    font=("Arial", 10)
).pack(fill="x", pady=(2, 8))

# Mensaje
Label(frame_form, text="Mensaje:", fg=COLOR_TEXTO, bg=COLOR_FONDO, font=("Arial", 9, "bold"), anchor="w").pack(fill="x")
mensaje_text = Text(
    frame_form,
    height=4,
    bg=COLOR_ENTRADA,
    fg="white",
    insertbackground="white",
    relief="solid",
    bd=1,
    font=("Arial", 10)
)
mensaje_text.pack(fill="x", pady=(2, 10))

# Botón de Envío
Button(
    ventana,
    text="ENVIAR CORREO",
    command=enviar_email,
    bg=COLOR_ACCENTO,
    fg="white",
    activebackground=COLOR_BOTON,
    activeforeground="white",
    font=("Arial", 11, "bold"),
    cursor="hand2",
    relief="flat",
    padx=15,
    pady=8
).pack(pady=(0, 15))

ventana.mainloop() 