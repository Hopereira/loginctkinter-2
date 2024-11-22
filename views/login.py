import customtkinter as ctk
from tkinter import *
from PIL import Image
from customtkinter import CTkImage
from tkinter import messagebox

janela = ctk.CTk()

class LoginView():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.tela_login()
        janela.mainloop()

    def tela(self):
        janela.geometry("700x400")
        janela.title("Sistema de Login")
        janela.iconbitmap("img/icon.ico")
        janela.resizable(False, False)

    def tela_login(self):
        try:
            original_image = Image.open("img/logo.png")
            resized_image = CTkImage(light_image=original_image, size=(250, 250))
            label_img = ctk.CTkLabel(master=janela, image=resized_image, text="")
            label_img.place(x=40, y=65)
        except FileNotFoundError:
            print("Erro: Verifique se o arquivo 'img/logo.png' existe.")

        ctk.CTkLabel(
            master=janela,
            text="Bem-vindo ao Sistema de Login",
            font=("Roboto", 20),
            text_color="#00b0f0",
        ).place(x=30, y=10)

        self.frame_login = ctk.CTkFrame(master=janela, width=350, height=390)
        self.frame_login.pack(side=RIGHT)

        ctk.CTkLabel(
            master=self.frame_login, text="Sistema de Login", font=("Roboto", 20)
        ).place(x=100, y=20)

        login_entry = ctk.CTkEntry(
            master=self.frame_login, width=300, placeholder_text="E-mail", font=("Roboto", 14)
        )
        login_entry.place(x=25, y=100)

        ctk.CTkLabel(
            master=self.frame_login,
            text="*E-mail obrigatório!",
            font=("Roboto", 12),
            text_color="red",
        ).place(x=100, y=130)

        senha_entry = ctk.CTkEntry(
            master=self.frame_login,
            width=300,
            placeholder_text="Senha",
            font=("Roboto", 14),
            show="*",
        )
        senha_entry.place(x=25, y=170)

        ctk.CTkLabel(
            master=self.frame_login,
            text="*Senha obrigatória!",
            font=("Roboto", 12),
            text_color="red",
        ).place(x=130, y=200)

        check_botao = ctk.CTkCheckBox(
            master=self.frame_login, text="Lembrar-me", font=("Roboto", 12)
        ).place(x=25, y=240)
        #criação da função logar
        def logar():
          #verifica se o campo de email está vazio
            if login_entry.get() == "":
                messagebox.showinfo("Erro", "O campo de e-mail é obrigatório!")
          #verifica se o campo de senha está vazio
            elif senha_entry.get() == "":
                messagebox.showinfo("Erro", "O campo de senha é obrigatório!")
          #se tudo estiver correto, loga
            else:
                messagebox.showinfo("Sucesso", "Login realizado com sucesso!")

        login_botao = ctk.CTkButton(
            master=self.frame_login, text="Login", font=("Roboto", 16),command=logar, width=100
        ).place(x=125, y=280)

        # Definindo as cores
        normal_color = "#00b0f0"
        hover_color = "red"

        # Criando o label "Esqueci a senha"
        esqueci_senha = ctk.CTkLabel(
            master=self.frame_login,
            text="Esqueci a senha",
            font=("Roboto", 12),
            text_color=normal_color,
        )
        esqueci_senha.place(x=50, y=330)

        # Bind para mudar a cor ao passar o mouse
        esqueci_senha.bind("<Enter>", lambda e: esqueci_senha.configure(text_color=hover_color))
        esqueci_senha.bind("<Leave>", lambda e: esqueci_senha.configure(text_color=normal_color))
        esqueci_senha.bind("<Button-1>", lambda e: print("Cliquei no 'Esqueci a senha'"))


        # Criando o label de cadastro
        register_label = ctk.CTkLabel(
            master=self.frame_login,
            text="Ainda não tem uma conta? Cadastre-se",
            font=("Roboto", 12),
            text_color="#00b0f0"
        )
        register_label.place(x=50, y=350)

        # Bind para mudar a cor ao passar o mouse
        register_label.bind("<Enter>", lambda e: register_label.configure(text_color="red"))
        register_label.bind("<Leave>", lambda e: register_label.configure(text_color="#00b0f0"))
        register_label.bind("<Button-1>", lambda e: self.tela_cadastro())
    #remove frames de login
    def tela_cadastro(self):
      self.frame_login.pack_forget()
      #cria frame de cadastro e seus elementos basiado no frame de login
      self.frame_cadastro = ctk.CTkFrame(master=janela, width=350, height=390)
      self.frame_cadastro.pack(side=RIGHT)
      ctk.CTkLabel(
                master=self.frame_cadastro, text="Entre com seus dados", font=("Roboto", 20)
            ).place(x=90, y=20)
      login_entry = ctk.CTkEntry(
                    master=self.frame_cadastro, width=300, placeholder_text="Seu E-mail", font=("Roboto", 14)
                )
      login_entry.place(x=25, y=100)
      ctk.CTkLabel(
                        master=self.frame_cadastro,
                        text="*Email obrigatório!",
                        font=("Roboto", 12),
                        text_color="red",
                    ).place(x=100, y=130)
      senha_entry = ctk.CTkEntry(
                            master=self.frame_cadastro,
                            width=300,
                            placeholder_text="Senha",
                            font=("Roboto", 14),
                            show="*",
                        )
      senha_entry.place(x=25, y=170)
      ctk.CTkLabel(
                                    master=self.frame_cadastro,
                                    text="*Senha obrigatória!",
                                    font=("Roboto", 12),
                                    text_color="red",
                                ).place(x=130, y=200)
        #repetir se as senhas conferem ou não
      senha_entry2 = ctk.CTkEntry(
                                master=self.frame_cadastro,
                                width=300,
                                placeholder_text="Repita a senha",
                                font=("Roboto", 14),
                                show="*",
                            )
      senha_entry2.place(x=25, y=230)

      # criação do checkbox termos de uso
      self.check_botao = ctk.CTkCheckBox(
                                    master=self.frame_cadastro, text="Aceito os termos de uso", font=("Roboto", 12)
                                )
      self.check_botao.place(x=25, y=280)
#criação da função de voltar para login
      def voltar_login():
        #remove frame de cadastro
            self.frame_cadastro.pack_forget()
        #chama a função de login
            self.tela_login()
      #botao de voltar para login
      botao_voltar = ctk.CTkButton(master=self.frame_cadastro, text="Voltar", font=("Roboto", 16),command=voltar_login, width=100).place(x=40, y=320)
      #função de salvar cadastro
      def save_cadastrar():
        #verifica se o campo de email está vazio
        if login_entry.get() == "":
          messagebox.showinfo("Erro", "O campo de e-mail é obrigatório!")
        #verifica se o campo de senha está vazio
        elif login_entry.get() == "":
          messagebox.showinfo("Erro", "O campo de senha é obrigatório!")
        #verifica se o campo de repetir senha está vazio
        elif senha_entry2.get() == "":
          messagebox.showinfo("Erro", "O campo de repetir senha é obrigatório!")
        #verifica se as senhas são iguais
        elif senha_entry.get() != senha_entry2.get():
          messagebox.showinfo("Erro", "As senhas não conferem!")
        #verifica se o checkbox está marcado
        elif not self.check_botao.get():
          messagebox.showinfo("Erro", "Você precisa aceitar os termos de uso!")

        #se tudo estiver correto, salva o cadastro
        else:
          messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
          self.frame_cadastro.pack_forget()
          self.tela_login()
      #botao de voltar para login 
      botao_cadastrar = ctk.CTkButton(master=self.frame_cadastro, text="Cadastrar", font=("Roboto", 16),command=save_cadastrar, width=100).place(x=200, y=320) 

# Executando o aplicativo
LoginView()
