from streamlit_TTS import text_to_speech

def synthesize(text, langs):
    """
    Gera narração nos idiomas selecionados.
    Retorna apenas o último arquivo de áudio (player no front-end Streamlit).
    """
    for lang in langs:
        text_to_speech(text=text, language=lang)
    # Não gera arquivo físico, play direto no app
    return None
