import flet

class ImageSlider(flet.Container):
    def __init__(self,images=list[flet.Image]):
        super().__init__()
        self.images = images
        self.width = 768
        self.border_radius = 8
        self.shadow = flet.BoxShadow(0,20,'black')

        self.buttons = self._create_buttons()
        self.switcher = flet.AnimatedSwitcher(
            images[0],
            duration=500,reverse_duration=500
        )
        self.content = flet.Stack([
            self.switcher,
            flet.Row(self.buttons,bottom=24,alignment=flet.MainAxisAlignment.CENTER)
        ],alignment=flet.Alignment.CENTER)
    
    def did_mount(self):
        self.set_current(0)
    
    def set_current(self,index:int):
        for i, button in enumerate(self.buttons):
            button.opacity = 1 if i == index else 0.5
            
        # Updating controls
        self.switcher.content = self.images[index]
        self.switcher.update()

    def _create_buttons(self):
        return [
            flet.Container(
                width=16,height=16,
                border_radius=360,bgcolor='white',
                opacity=0.5,data=index,
                on_click=self._on_button_click
            )
            for index in range(len(self.images))
        ]

    def _on_button_click(self,e:flet.ControlEvent):
        self.set_current(e.control.data) #data contains the index of image