from tkinter import Label, PhotoImage, Tk
from tkinter import ttk
import handling_game_events as game_events


whose_move=None
field, cells, positions = game_events.creation_storages()

def window_creation():
    # создание окна

    height = 200
    width = 250
    root = Tk()
    root.title("tic-tac-toe")
    icon = PhotoImage(file = "images\icon.png")
    root.iconphoto(False, icon)
    root.geometry(f"{width}x{height}")
    
    return root


def main_menu(root):
    # заполнение главного меню

    new_text = Label(text='Меню',  font=("Arial", 14))
    new_text.pack(anchor='center', padx=20, pady=20)

    game_btn = ttk.Button(text="Играть", command=lambda: clicked_game(root, new_text, game_btn, exit_btn))
    game_btn.pack(anchor='center', padx=5, pady=5)

    exit_btn = ttk.Button(text="Выход", command=exit)
    exit_btn.pack(anchor='center', padx=5, pady=5)

    root.mainloop()


def destroy_main_menu(root, text, game_btn, exit_btn):
    # очистка окна от меню 

    text.destroy()
    game_btn.destroy()
    exit_btn.destroy()


def mode_selection(root):
    # заполнение меню выбора режима игры

    new_text = Label(text='Выберите режим',  font=("Arial", 14))
    new_text.pack(anchor='center', padx=20, pady=20)

    pve_game_btn = ttk.Button(text="Против копмьютера", command=lambda: clicked_pve(root, new_text, 
                                                                                    pve_game_btn,
                                                                                    pvp_game_btn,
                                                                                    back_btn))
    pve_game_btn.pack(anchor='center', padx=5, pady=5)

    pvp_game_btn = ttk.Button(text="Игрок против игрока", command=lambda: clicked_pvp(root, new_text, 
                                                                                      pve_game_btn,
                                                                                      pvp_game_btn,
                                                                                      back_btn))
    pvp_game_btn.pack(anchor='center', padx=5, pady=5)

    back_btn = ttk.Button(text="Вернуться", command=lambda: clicked_back(root, new_text, 
                                                                         pve_game_btn,
                                                                         pvp_game_btn,
                                                                         back_btn))
    back_btn.pack(anchor='center', padx=5, pady=5)


def destroy_mode_selection(root, new_text, pve_game_btn, pvp_game_btn, back_btn):
    # очистка меню выбора режима

    new_text.destroy()
    pve_game_btn.destroy()
    pvp_game_btn.destroy()
    back_btn.destroy()
    

def clicked_game(root, new_text, game_btn, exit_btn):
    # кнопка для начала игры

    destroy_main_menu(root, new_text, game_btn, exit_btn)
    mode_selection(root)


def clicked_pvp(root, new_text, pve_game_btn, pvp_game_btn, back_btn):
    # кнопка для игры против игрока 

    destroy_mode_selection(root, new_text, pve_game_btn, pvp_game_btn, back_btn)
    choice_move(root)


def clicked_pve(root, new_text, pve_game_btn, pvp_game_btn, back_btn):
    # кнопка для игры против компьютера 

    destroy_mode_selection(root, new_text, pve_game_btn, pvp_game_btn, back_btn)
    pass


def clicked_back(root, new_text, pve_game_btn, pvp_game_btn, back_btn):
    # кнопка для возвращения в главное меню

    destroy_mode_selection(root, new_text, pve_game_btn, pvp_game_btn, back_btn)
    main_menu(root)


def choice_move(root):
    # выбор орла или решки

    new_text = Label(text='Игрок 1 выбирает',  font=("Arial", 14))
    new_text.pack(anchor='center', padx=20, pady=20)
    
    eagle = PhotoImage(file = "images\eagle.png", width=100, height=100)
    eagle_btn = ttk.Button(text="Орел" ,image=eagle, command=lambda: drawing_roll_dice('Орел', new_text, eagle_btn, tails_btn, root))
    eagle_btn.pack(anchor='center', padx=10, pady=10)

    tails = PhotoImage(file = r"images\tails.png", width=100, height=100)
    tails_btn = ttk.Button(text="Решка" ,image=tails, command=lambda: drawing_roll_dice('Решка', new_text, eagle_btn, tails_btn, root))
    tails_btn.pack(anchor='center', padx=10, pady=10)


def destroy_choice_move(new_text, eagle_btn, tails_btn):
    # очитска меню выбора орла и решки

    new_text.destroy()
    eagle_btn.destroy()
    tails_btn.destroy()


def drawing_roll_dice(choice, new_text, eagle_btn, tails_btn, root):
    # вывод результатов броска монеты

    global whose_move
    destroy_choice_move(new_text, eagle_btn, tails_btn)
    result, move = game_events.determining_first_move(choice)
    
    if result:
        whose_move = 0
        text_1 = Label(text=f"Выпало: {move}", font=("Arial", 11))
        text_2 = Label(text="Игрок 1 ходит первым", font=("Arial", 11))
        text_1.pack(anchor='center', padx=5, pady=20)
        text_2.pack(anchor='center', padx=5, pady=20)
    else:
        whose_move = 1
        text_1 = Label(text=f"Выпало: {move}", font=("Arial", 11))
        text_2 = Label(text="Игрок 2 ходит первым", font=("Arial", 11))
        text_1.pack(anchor='center', padx=5, pady=20)
        text_2.pack(anchor='center', padx=5, pady=20)
    
    begin_btn = ttk.Button(text="Начать играть", command=lambda: begin_play(root, text_1, text_2, begin_btn))
    begin_btn.pack(anchor='center', padx=5, pady=5)


def begin_play(root, text_1, text_2, begin_btn):
    # очистка окна от результатов броска монеты и запуск отрисовки поля
    
    text_1.destroy()
    text_2.destroy()
    begin_btn.destroy()
    game_drawing(root)


def game_drawing(root):
    # рисование поля игры

    global whose_move, field, cells, positions
    
    walking_now = Label(text=f"Ход игрока {whose_move+1}", font=("Arial", 11))
    walking_now.grid(columnspan=3, row=0)
    
    surr_btn = ttk.Button(text='Сдаться', command=lambda: clicked_surr(root, walking_now, cells, surr_btn))
    surr_btn.grid(row=4, column=2)

    for key in positions:
        cells[key] = create_btn(root, key, walking_now, positions, field, key, surr_btn, cells)
        cells[key].grid(row=positions[key][0]+1, column=positions[key][1],
                      ipadx=5, ipady=10)


def create_btn(root, value, walking_now, positions, field, key, surr_btn, cells):
    # создание кнопки игрового поля

    value = ttk.Button(text='', command=lambda: clicked_move(root, value, walking_now, positions, field, key, surr_btn, cells))
    return value


def destroy_game_drawing(walking_now, cells_btn, surr_btn):
    # очистка поля игры
    global whose_move, field, cells, positions

    walking_now.destroy()
    for key in cells_btn:
        cells_btn[key].destroy()
    surr_btn.destroy()

    field, cells, positions = game_events.creation_storages()
    


def clicked_surr(root, walking_now, cells, surr_btn):
    # кнопка для сдачи

    destroy_game_drawing(walking_now, cells, surr_btn)
    surrender_notice(root)


def surrender_notice(root):
    # объявление о сдаче

    global whose_move
    new_text = Label(text=f'Игрок {whose_move+1} сдался',  font=("Arial", 14))
    new_text.pack(anchor='center', padx=20, pady=20)

    menu_btn = ttk.Button(text='В главное меню', command=lambda: clicked_on_menu(root, new_text, menu_btn))
    menu_btn.pack(anchor='center', padx=5, pady=5)


def clicked_on_menu(root, new_text, menu_btn):
    # кнопка для возвращения в главное меню

    new_text.destroy()
    menu_btn.destroy()
    main_menu(root)


def clicked_move(root, cell_btn, walking_now, positions, field, key, surr_btn, cells):
    # кнопка поля игры 

    global whose_move

    if [cell_btn.grid_info()['row']-1, cell_btn.grid_info()['column']] in positions.values():
        if whose_move==1:
            cell_btn.configure(text='X')
            field[positions[key][0]][positions[key][1]] =  "X"
            positions.pop(key)
            
        else:
            cell_btn.configure(text='O')
            field[positions[key][0]][positions[key][1]] =  "O"
            positions.pop(key)

        vin_position = game_events.create_vin_position()
        examination = game_events.victory_check(field, vin_position)
        if examination!=-1:
            victory_announcement(root, cells, surr_btn, walking_now)
        elif len(positions)==0:
            draw_announcement(root, cells, surr_btn, walking_now)
        else:
            whose_move=not whose_move
            walking_now['text'] = f"Ход игрока {whose_move+1}"


def victory_announcement(root, cells, surr_btn, walking_now):
    # Объявление победы

    destroy_game_drawing(walking_now, cells, surr_btn)

    global whose_move
    new_text = Label(text=f'Игрок {whose_move+1} победил',  font=("Arial", 14))
    new_text.pack(anchor='center', padx=20, pady=20)

    menu_btn = ttk.Button(text='В главное меню', command=lambda: clicked_on_menu(root, new_text, menu_btn))
    menu_btn.pack(anchor='center', padx=5, pady=5)


def draw_announcement(root, cells, surr_btn, walking_now):
    # объявление ничьи
    destroy_game_drawing(walking_now, cells, surr_btn)

    global whose_move
    new_text = Label(text='Ничья',  font=("Arial", 14))
    new_text.pack(anchor='center', padx=20, pady=20)

    menu_btn = ttk.Button(text='В главное меню', command=lambda: clicked_on_menu(root, new_text, menu_btn))
    menu_btn.pack(anchor='center', padx=5, pady=5)


root = window_creation()
main_menu(root)
