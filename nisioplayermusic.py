'''
NISIO - Player Music
'''
from tkinter import *
import pygame
from tkinter import filedialog

class App:
    def __init__(self):
        self.root = root
        self.tela()
        root.mainloop()
        
    def tela(self):
        self.root.title('BEM-VINDO(A)')
        self.root.geometry('480x680+850+6')
        self.root.resizable(False, False)
        # Ícone
        self.root.iconbitmap('IconeNisio.ico')

        # Imagem/ Botão de Entrada
        self.root.img1 = PhotoImage(file='CapaNisio.png')
        self.root.img_btn1 = Button(self.root, image=self.root.img1, command = self.clica_entrar)
        self.root.img_btn1.pack()

    # Metódos de invocação de uma nova janela
    def clica_entrar(self):  # Comando do botão
        self.hide()
        self.subframe = Musicas(self)  # Próxima janela para ser aberta

    def hide(self):
        self.root.withdraw()

    def show(self):
        self.root.update()
        self.root.deiconify()

class Musicas(Toplevel):
    # Cores do Aplicativo
    cor_rosa_medio = '#E70641'
    cor_rosa_escuro = '#BE175A'
    cor_azul_escuro = '#035371'
    cor_azul_claro = '#339989'
    cor_roxo_escuro = '#3a0ca3'
    def __init__(self, original):
        self.original_frame = original
        Toplevel.__init__(self)  # Importando o Metódo Construtor
        self.title('MÚSICAS')
        self.geometry('480x680+850+6')
        self.configure(background = 'black')
        self.resizable(False, False)
        # Ícone
        self.iconbitmap('IconeNisio.ico')
        self.menu()
        self.widgets()
        root.mainloop()

    # Iniciar o Pygame Mixer
    pygame.mixer.init()

    # Adicionar a Função Song
    def add_song(self):
        self.song = filedialog.askopenfilename(initialdir='c:\\Users\\Gabriel\\Downloads\\MP3', title='Choose A Song',filetypes=(("mp3 Files", "*.mp3"),))

        # Arrumando a saída do diretório de informação do .mp3
        self.song = self.song.replace("C:/Users/Gabriel/Downloads/MP3/", "")
        self.song = self.song.replace(".mp3", "")

        # Add a música no ListBox
        self.song_box.insert(END, self.song)

    # Adicionar a Função várias músicas
    def add_many_songs(self):
        songs = filedialog.askopenfilenames(initialdir='c:\\Users\\Gabriel\\Downloads\\MP3', title='Choose A Song',filetypes=(("mp3 Files", "*.mp3"),))

        # Loop thru do song
        for self.song in songs:
            self.song = self.song.replace("C:/Users/Gabriel/Downloads/MP3/", "")
            self.song = self.song.replace(".mp3", "")
            # Inserir á PLaylist
            self.song_box.insert(END, self.song)

        # Ativando o Play da Música Selecionada
    def play(self):
        self.song = self.song_box.get(ACTIVE)
        self.song = f'C:/Users/Gabriel/Downloads/MP3/{self.song}.mp3'

        pygame.mixer.music.load(self.song)
        pygame.mixer.music.play(loops=0)

    def stop(self):
        pygame.mixer.music.stop()
        self.song_box.selection_clear(ACTIVE)

    def next_song(self):
        # Criando a correte de música atraves do número
        self.next_one = self.song_box.curselection()
        self.next_one = self.next_one[0] + 1
        self.song = self.song_box.get(self.next_one)
        # Grab song com o título para a playlist
        self.song = f'C:/Users/Gabriel/Downloads/MP3/{self.song}.mp3'

        pygame.mixer.music.load(self.song)
        pygame.mixer.music.play(loops=0)

        # Movendo a barra de atividade para a música tocando no momento
        self.song_box.selection_clear(0, END)
        self.song_box.activate(self.next_one)

        # Selecionando a barra de uma música
        self.song_box.selection_set(self.next_one, last=None)

    def previous_song(self):
        # Criando a correte de música atraves do número
        self.next_one = self.song_box.curselection()
        self.next_one = self.next_one[0] - 1
        self.song = self.song_box.get(self.next_one)
        # Grab song com o título para a playlist
        self.song = f'C:/Users/Gabriel/Downloads/MP3/{self.song}.mp3'

        pygame.mixer.music.load(self.song)
        pygame.mixer.music.play(loops=0)

        # Movendo a barra de atividade para a música tocando no momento
        self.song_box.selection_clear(0, END)
        self.song_box.activate(self.next_one)

        # Selecionando a barra de uma música
        self.song_box.selection_set(self.next_one, last=None)

        # Deletando uma Música
    def delete_song(self):
        self.song_box.delete(ANCHOR)
        pygame.mixer.music.stop()

    # Deletando Todas as Músicas da Playlist
    def delete_all_songs(self):
        self.song_box.delete(0, END)
        pygame.mixer.music.stop()

    # Criando uma variavel global para a pause
    global paused
    paused = False

    def pause(self, is_paused):
        global paused
        paused = is_paused

        if paused:
            pygame.mixer.music.unpause()
            paused = False
        else:
            pygame.mixer.music.pause()
            paused = True

    def menu(self):
        # Criando um Menu Para as músicas
        my_menu = Menu(self)
        self.config(menu=my_menu)

        # Add música ao menu
        self.add_song_menu = Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label="Add Música", menu=self.add_song_menu)
        self.add_song_menu.add_command(label="Add Uma Música À Playlist", command=self.add_song)

        # Add mais de uma música à PLaylist ao mesmo tempo
        self.add_song_menu.add_command(label="Add Mais de Uma Música À Playlist", command=self.add_many_songs)

        # Deletando uma música
        remove_song_menu = Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label="Remover Música", menu=remove_song_menu)
        remove_song_menu.add_command(label="Deletar Uma Música da Playlist", command=self.delete_song)
        remove_song_menu.add_command(label="Deletar Todas as Múscias da PLaylist", command=self.delete_all_songs)

    def widgets(self):
        # Imagens - Título
        self.img1 = PhotoImage(file='FundoNisio1.PNG')
        self.fundo_img = Label(self, image=self.img1, border=0)
        self.fundo_img.place(relx=0.33, rely=0)

        self.img2 = PhotoImage(file='FundoNisio2.PNG')
        self.fundo2_img = Label(self, image=self.img2, border=0)
        self.fundo2_img.place(relx=0, rely=0.8)

        # Frame do ListBox
        self.janela_principal = Frame(self, bg='black')
        self.janela_principal.place(relx=0, rely=0.25, relwidth=1, relheight=0.5)

        # Criar a PlayList Box
        self.song_box = Listbox(self.janela_principal, bg='black', font='14', width=60, fg=self.cor_azul_escuro, selectbackground='white', selectforeground=self.cor_rosa_escuro, borderwidth=20)
        self.song_box.pack(padx = 20, pady = 5)

        # Botões de Controle
        self.back_btn_img = PhotoImage(file='Back_bntNisio.PNG')
        self.back_btn = Button(self.janela_principal, image=self.back_btn_img, borderwidth=0, command=self.previous_song)
        self.back_btn.place(relx = 0.03, rely = 0.75)

        self.stop_btn_img = PhotoImage(file='Stop_btnNisio.PNG')
        self.stop_btn = Button(self.janela_principal, image=self.stop_btn_img, borderwidth=0, command=self.stop)
        self.stop_btn.place(relx = 0.23, rely = 0.75)

        self.play_btn_img = PhotoImage(file='Play_btnNisio.PNG')
        self.play_btn = Button(self.janela_principal, image=self.play_btn_img, borderwidth=0, command=self.play)
        self.play_btn.place(relx = 0.43, rely = 0.75)

        self.pause_btn_img = PhotoImage(file='Pause_btnNisio.PNG')
        self.pause_btn = Button(self.janela_principal, image=self.pause_btn_img, borderwidth=0, command=lambda:self.pause(paused))
        self.pause_btn.place(relx = 0.63, rely = 0.75)

        self.next_btn_img = PhotoImage(file='Next_btnNisio.PNG')
        self.next_btn = Button(self.janela_principal, image=self.next_btn_img, borderwidth=0, command=self.next_song)
        self.next_btn.place(relx = 0.83, rely = 0.75)

##### PROGRAMA PRINCIPAL #####
root = Tk()
App()