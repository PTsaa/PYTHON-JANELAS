import customtkinter as ctk


def clique():
    print("Teste")


master = ctk.CTk()
master.geometry("500x300")

titulo = ctk.CTkLabel(master, text="Efetuar Login")
titulo.pack(padx=10, pady=10)

email = ctk.CTkEntry(master, placeholder_text="Insira seu e-mail")
email.pack(padx=10, pady=10)

senha = ctk.CTkEntry(master, placeholder_text="Senha", show="*")
senha.pack(padx=10, pady=10)

botao = ctk.CTkButton(master, text="Login", command=clique)
botao.pack(padx=10, pady=10)

master.mainloop()
