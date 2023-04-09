from nicegui import ui
import asyncio
from processing import *

p = Processor()

# ui.label('Resumir').classes('font-black text-2xl')
# ui.icon('sentiment_very_dissatisfied')


with ui.tabs() as tabs:
    ui.tab('Resumir', icon=None) #home
    ui.tab('Topificar', icon=None) #info


with ui.tab_panels(tabs, value='Resumir'):
    with ui.tab_panel('Resumir'):
        ui.label('Resumir').classes('font-black text-2xl')
        with ui.row().classes('center no-wrap'):
            with ui.column().classes('w-[12.6rem]'):
                async def g():
                    button.props(add='loading')
                    await asyncio.sleep(1)
                    result.set_text((textarea.value == '') or p.process(textarea.value))
                    button.props(remove='loading')
                
            button = ui.button('Process', on_click = g)

            with ui.column():
                with ui.row().classes('no-wrap'):
                    ui.label('Criatividade')
                with ui.row().classes('w-[50rem] no-wrap'):
                    slider = ui.slider(min=0, max=2, value=1, step=0.1, on_change = lambda: p.change_temperature(slider.value)).props('label')
                    ui.label().bind_text_from(slider, 'value')
            #spinner = ui.spinner(size='lg').set_visibility('false')

        with ui.row().classes('w-full no-wrap'):
            with ui.column().classes('w-[38rem]'):
                with ui.card().classes('w-full'):
                    textarea = ui.textarea(label='Texto', placeholder='Insira o texto',
                                           on_change=lambda e: None).classes('w-full').props('autogrow') #result.set_text(e.value)
            with ui.column().classes('w-[38rem]'):
                    with ui.card().classes('w-full'):
                        ui.label("Resultado:\n")
                        result = ui.label().classes('w-full')

    with ui.tab_panel('Topificar'):
        ui.label('This is the second tab')

#ui.run(title='GPT 9000', dark='true')
#ui.run(title='Ferramenta', port=3036)
ui.run(title='Ferramenta')


