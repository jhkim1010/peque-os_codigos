import PySimpleGUI as sg

Nome = ''
Quantidade = ''
Preco = ''
Id = ''

        
cols = 4
rows = 20
col_width = 22


all_listbox = [[sg.Listbox(Nome,size=(15, rows), pad=(0, 0),
no_scrollbar=True, enable_events=False, key=f'listbox {i}',
select_mode=sg.LISTBOX_SELECT_MODE_SINGLE) for i in range(cols)]]



#layout
layout = [
    [sg.Text('Selecione a classe que deseja ver:',size= (15,0)),sg.InputCombo(('Circuito','Transistor','Membrana'),size=(20,0),key='combo')],
    [sg.Button('Consultar')], 
        [sg.Text('Id'.center(col_width), pad=(0, 0)),
        sg.Text('Nome'.center(col_width), pad=(0, 0)),
        sg.Text('Quantidade'.center(col_width), pad=(0, 0)),
        sg.Text('Preço'.center(col_width), pad=(0, 0))],
    [sg.Column(all_listbox, size=(440, 200), pad=(0, 0),scrollable=True,
        vertical_scroll_only=True,key='test')],

    [sg.Button('Deletar')],
    [sg.Button('Sair'),sg.Button('Voltar')]
    ]
    
#janela
window = sg.Window("adicionar ao Estoque",layout)



while True:
    event,values = window.read()

    try:
        if event.startswith('listbox'):
            row = window[event].get_indexes()[0]
            user_event = False
            for i in range(cols):
                window[f'listbox {i}'].set_value([])
                window[f'listbox {i}'].Widget.selection_set(row)

        
        if event == 'Consultar':
            f = values['combo']
            Id = filtrar2(f)
            Nome = filtrar(f)
            Quantidade = filtrar3(f)
            Preco = filtrar4(f)
            
            
            window.find_element(f'listbox {1}').Update(Nome)
            window.find_element(f'listbox {0}').Update(Id)
            window.find_element(f'listbox {2}').Update(Quantidade)
            window.find_element(f'listbox {3}').Update(Preco)