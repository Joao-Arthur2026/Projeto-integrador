import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

janela = customtkinter.CTk()
janela.title("Meus Lembretes")
janela.geometry("800x750")


tamanho_letra = 26  

limite = 6  

textos_dos_lembretes = []


def atualizar_contador():
    quantidade = len(textos_dos_lembretes)

    if quantidade == 0:
        contador.configure(text="Nenhum lembrete. Aproveita o descanso!")
    elif quantidade == 1:
        contador.configure(text="Você tem 1 lembrete")
    else:
        contador.configure(text="Você tem " + str(quantidade) + " lembretes")


def adicionar():
    texto = entrada.get()

    if texto == "":
        contador.configure(text="Escreve um lembrete primeiro!")
        return  

    if len(textos_dos_lembretes) >= limite:
        contador.configure(text="Lista cheia! Conclui um lembrete antes.")
        return

    caixinha = customtkinter.CTkFrame(master=frame_lista)
    caixinha.pack(padx=10, pady=5, fill="x")

    texto_lembrete = customtkinter.CTkLabel(
        master=caixinha, 
        text=texto,
        font=("Arial", tamanho_letra), 
        wraplength=550)
    texto_lembrete.pack(side="left", padx=15, pady=10)

    textos_dos_lembretes.append(texto_lembrete)

    def concluir():
        textos_dos_lembretes.remove(texto_lembrete)  
        caixinha.destroy()  
        atualizar_contador()

    btn_feito = customtkinter.CTkButton(master=caixinha, text="Feito ✓", width=120, height=50,
                                        font=("Arial", 22), fg_color="#2E7D32",  
                                        command=concluir)
    btn_feito.pack(side="right", padx=10, pady=10)

    entrada.delete(0, "end")
    atualizar_contador()

def adicionar_especial():
    texto = entrada.get()

    if texto == "":
        contador.configure(text="Escreve um lembrete primeiro!")
        return  

    if len(textos_dos_lembretes) >= limite:
        contador.configure(text="Lista cheia! Conclui um lembrete antes.")
        return

    caixinha = customtkinter.CTkFrame(master=frame_lista,fg_color="#FFF000")
    caixinha.pack(padx=10, pady=5, fill="x")

    texto_lembrete_especial = customtkinter.CTkLabel(
        master=caixinha, 
        text=texto,
        font=("Arial", tamanho_letra),
        text_color="#000000", 
        wraplength=550)
    texto_lembrete_especial.pack(side="left", padx=15, pady=10)

    textos_dos_lembretes.append(texto_lembrete_especial)

    def concluir():
        textos_dos_lembretes.remove(texto_lembrete_especial)  
        caixinha.destroy()  
        atualizar_contador()

    btn_feito = customtkinter.CTkButton(master=caixinha, text="Feito ✓", width=120, height=50,
                                        font=("Arial", 22), fg_color="#2E7D32",  
                                        command=concluir)
    btn_feito.pack(side="right", padx=10, pady=10)


    entrada.delete(0, "end")
    atualizar_contador()

def aumentar():
    global tamanho_letra

    if tamanho_letra < 60:
        tamanho_letra = tamanho_letra + 4
        for texto_lembrete in textos_dos_lembretes:
            texto_lembrete.configure(font=("Arial", tamanho_letra))
        info_tamanho.configure(text="Letra: " + str(tamanho_letra))


def diminuir():
    global tamanho_letra

    if tamanho_letra > 16:
        tamanho_letra = tamanho_letra - 4
        for texto_lembrete in textos_dos_lembretes:
            texto_lembrete.configure(font=("Arial", tamanho_letra))
        info_tamanho.configure(text="Letra: " + str(tamanho_letra))


def trocar_tema():
    tema_atual = customtkinter.get_appearance_mode()

    if tema_atual == "Dark":
        customtkinter.set_appearance_mode("light")
        btn_tema.configure(text="Modo escuro")
    else:
        customtkinter.set_appearance_mode("dark")
        btn_tema.configure(text="Modo claro")

def aumentar_quantidade_limite():
    global limite
    if limite < 20:
        limite = limite + 1
        info_limite.configure(text="Limite de notas: " + str(limite))

def diminuir_quantidade_limite():
    global limite
    if limite > 2:
        limite = limite - 1
        info_limite.configure(text="Limite de notas: " + str(limite))
    
frame_barra = customtkinter.CTkFrame(master=janela)
frame_barra.pack(padx=10, pady=10, fill="x")

btn_diminuir = customtkinter.CTkButton(master=frame_barra, text="A-", width=60, height=50,
                                       font=("Arial", 22), command=diminuir,fg_color="#000000",text_color="#FFFF00")
btn_diminuir.pack(side="left", padx=5, pady=10)

btn_aumentar = customtkinter.CTkButton(master=frame_barra, text="A+", width=60, height=50,
                                       font=("Arial", 22), command=aumentar,fg_color="#000000",text_color="#FFFF00")
btn_aumentar.pack(side="left", padx=5, pady=10)

info_tamanho = customtkinter.CTkLabel(master=frame_barra, text="Letra: 26", font=("Arial", 20))
info_tamanho.pack(side="left", padx=15)

btn_diminuir_limite = customtkinter.CTkButton(master=frame_barra, text="Q-", width=60, height=50,
                                       font=("Arial", 22), command=diminuir_quantidade_limite,fg_color="#000000",text_color="#FFFF00" )
btn_diminuir_limite.pack(side="left", padx=5, pady=10)

btn_aumentar_limite = customtkinter.CTkButton(master=frame_barra, text="Q+", width=60, height=50,
                                       font=("Arial", 22), command=aumentar_quantidade_limite,fg_color="#000000",text_color="#FFFF00")
btn_aumentar_limite.pack(side="left", padx=5, pady=10)

info_limite = customtkinter.CTkLabel(master=frame_barra, text="Limite de notas: 6", font=("Arial", 20))
info_limite.pack(side="left", padx=15)

btn_tema = customtkinter.CTkButton(master=frame_barra, text="Modo claro",fg_color="#000000",text_color="#FFFF00", height=50,
                                   font=("Arial", 20), command=trocar_tema)
btn_tema.pack(side="right", padx=10, pady=10)

frame_entrada = customtkinter.CTkFrame(master=janela)
frame_entrada.pack(padx=10, pady=10, fill="x")

entrada = customtkinter.CTkEntry(master=frame_entrada, height=50, font=("Arial", 24),
                                 placeholder_text="Ex.: Tomar remédio às 8h")
entrada.pack(side="left", padx=10, pady=10, fill="x", expand=True)

btn_adicionar = customtkinter.CTkButton(master=frame_entrada,fg_color="#000000",text_color="#FFFF00", text="Adicionar", height=50,
                                        font=("Arial", 22), command=adicionar)
btn_adicionar.pack(side="right", padx=10, pady=10)

btn_adicionar_especial = customtkinter.CTkButton(master=frame_entrada,fg_color="#FFFF00",text_color="#000000", text="Adicionar(Estrela) ", height=50,
                                        font=("Arial", 22),command=adicionar_especial)
btn_adicionar_especial.pack(side="right", padx=10, pady=10)


frame_lista = customtkinter.CTkScrollableFrame(
    master=janela,
    fg_color=("gray90", "gray10"))
frame_lista.pack(padx=10, pady=10, fill="both", expand=True)



frame_rodape = customtkinter.CTkFrame(
    master=janela, 
    fg_color="transparent")
frame_rodape.pack(padx=10, pady=10, fill="x")

contador = customtkinter.CTkLabel(
    master=frame_rodape, 
    text="Nenhum lembrete. Aproveita o descanso!",
    font=("Arial", 22))
contador.pack(pady=5)


janela.mainloop()