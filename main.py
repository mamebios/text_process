from nicegui import ui
from processing import *

p = Processor()

#ui.label('Resumir').classes('font-black text-2xl')
#ui.icon('sentiment_very_dissatisfied')


with ui.tabs() as tabs:
    ui.tab('Resumir', icon=None) #home
    ui.tab('Topificar', icon=None) #info


with ui.tab_panels(tabs, value='Resumir'):
    with ui.tab_panel('Resumir'):
        ui.label('Resumir').classes('font-black text-2xl')
        with ui.row().classes('center'):
            button = ui.button('Process', on_click = lambda: result.set_text(p.process(textarea.value)))
            #spinner = ui.spinner(size='lg').set_visibility('false')
        with ui.card().classes('center w-300') as card: #max-w-sm min-w-500
            with ui.row().classes('center'):
                with ui.column().classes('w-300 center'):
                    textarea = ui.textarea(label='Texto', placeholder='Insira o texto',
                                on_change=lambda e: None).classes('rounded-md w-96') #result.set_text(e.value)
            with ui.row().classes('center'): #'' or p.process(e.value) * (len(e.value) > 0)
                with ui.column().classes('w-300 center'):
                    ui.label("Resultado:\n").classes('text-sky-400')
                    result = ui.label().classes('break-all')

    with ui.tab_panel('Topificar'):
        ui.label('This is the second tab')



#ui.run(title='GPT 9000', dark='true')
ui.run(title='Ferramenta', port=3036)