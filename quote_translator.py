import flet as ft

def main(page:ft.Page):

    original_quote = "All our dreams can come true, if we have the courage to pursue them. -Walt Disney."
    translations = {
        "Danish": "Alle vores drømme kan gå i opfyldelse, hvis vi har modet til at forfølge dem.",
        "Spanish": "Todos nuestros sueños pueden hacerse realidad, si tenemos el coraje de perseguirlos."
    }

    def translate_quote(event):
        selected_language = language_selector.value
        if selected_language in translations:
            quote_display.value = translations[selected_language]
        else:
            quote_display.value = original_quote
        page.update()

    heading = ft.Text(value="Select a language you want to translate the quote to:")
    
    language_selector = ft.RadioGroup(
        content=ft.Column(
            controls=[
                ft.Radio(label="Original", value="Original"),
                ft.Radio(label="Danish", value="Danish"),
                ft.Radio(label="Spanish", value="Spanish"),
            ]
        ),
        on_change=translate_quote
    )

    quote_display = ft.Text(original_quote, size=24)

    page.add(heading, language_selector, quote_display)

ft.app(target=main)