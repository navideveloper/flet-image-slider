from ui.components import ImageSlider
import flet

def main(page:flet.Page):
    page.bgcolor = 'white'
    page.title = 'Image Slider'
    page.padding = 0
    page.horizontal_alignment = flet.MainAxisAlignment.CENTER
    page.vertical_alignment = flet.MainAxisAlignment.CENTER

    page.add(
        ImageSlider([
            flet.Image('image_1.jpg',aspect_ratio=16/9,fit=flet.BoxFit.COVER),
            flet.Image('image_2.jpg',aspect_ratio=16/9,fit=flet.BoxFit.COVER),
            flet.Image('image_3.jpg',aspect_ratio=16/9,fit=flet.BoxFit.COVER)
        ])
    )

flet.run(main,assets_dir='assets')