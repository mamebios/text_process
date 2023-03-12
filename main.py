from nicegui import ui
from processing import *

#processador que vai fazer a summarization
p = Processor()


#result = ui.label()
#print(result.text)

with ui.row():
    ui.textarea(label='Text', placeholder='start typing',
            on_change=lambda e: result.set_text(p.process(e.value))
            )
    result = ui.label()

ui.run(port=3036)