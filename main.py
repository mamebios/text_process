'''
 This is the UI module

 Following the MVC (model-view-control) architecture,
 this represents the UI (view-control), with graphic 
 elements and logic components that provide the interface
 between the user and the AI langauge models on the
 processing module

'''

from nicegui import ui
import asyncio
from processing import *

#Processing modules
p = Summarizer()
t = Topicfier()

#Defining the tab panels
with ui.tabs() as tabs:
    ui.tab('Resumir', icon=None)
    ui.tab('Topificar', icon=None)

with ui.tab_panels(tabs, value='Resumir'):
    #Summary mode tab panel
    with ui.tab_panel('Resumir'):
        ui.label('Resumir').classes('font-black text-2xl')

        #Process command button; when it's clicked a loading animation appears,
        #and it becomes unable to be clicked again until the Summarizer processor module returns the output
        with ui.row().classes('center no-wrap'):
            with ui.column().classes('w-[12.6rem]'):
                async def g():
                    button.props(add='loading')
                    await asyncio.sleep(1)
                    result.set_text((textarea.value == '') or p.process(textarea.value))
                    button.props(remove='loading')
                
            button = ui.button('Processar', on_click = g)

            #Slider for changing the model's Criatividade aka temperature param
            with ui.column():
                with ui.row().classes('no-wrap'):
                    ui.label('Criatividade (?)').tooltip('Criatividade é um hiperparâmetro que pode ser usado para controlar a aleatoriedade do texto gerado. ' \
                                                       'Uma criatividade alta (>1.5) pode gerar textos ininteligíveis.')
                with ui.row().classes('w-[50rem] no-wrap'):
                    slider = ui.slider(min=0, max=2, value=1, step=0.1, on_change = lambda: p.change_temperature(slider.value)).props('label')
                    ui.label().bind_text_from(slider, 'value')

        #Areas to input text and show the processed output
        with ui.row().classes('w-full no-wrap'):
            with ui.column().classes('w-[38rem]'):
                with ui.card().classes('w-full'):
                    textarea = ui.textarea(label='Texto', placeholder='Insira o texto',
                                           on_change=lambda e: None).classes('w-full').props('autogrow')
            with ui.column().classes('w-[38rem]'):
                    with ui.card().classes('w-full'):
                        ui.label("Resultado:\n")
                        result = ui.label().classes('w-full hyphens-auto')

    #Topic mode tab panel
    with ui.tab_panel('Topificar'):
        ui.label('Topificar').classes('font-black text-2xl')

        #Process command button; when it's clicked a loading animation appears,
        #and it becomes unable to be clicked again until the Topicfier processor module returns the output
        with ui.row().classes('center no-wrap'):
            with ui.column().classes('w-[12.6rem]'):
                async def g_t():
                    button_t.props(add='loading')
                    await asyncio.sleep(1)
                    result_t.set_text((textarea_t.value == '') or t.process(textarea_t.value))
                    button_t.props(remove='loading')
                
            button_t = ui.button('Processar', on_click = g_t)

        #Areas to input text and show the processed output
        with ui.row().classes('w-full no-wrap'):
            with ui.column().classes('w-[38rem]'):
                with ui.card().classes('w-full'):
                    textarea_t = ui.textarea(label='Texto', placeholder='Insira o texto',
                                           on_change=lambda e: None).classes('w-full').props('autogrow')
            with ui.column().classes('w-[38rem]'):
                    with ui.card().classes('w-full'):
                        ui.label("Resultado:\n")
                        result_t = ui.label().classes('w-full whitespace-pre')
        

ui.run(title='Text Process', port = 3036)