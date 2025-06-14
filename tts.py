from TTS.api import TTS

tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v1")

def synthesize(text, langs):
    """
    Gera narração para o texto dado nos idiomas listados.
    Retorna o caminho para o arquivo audio.wav
    """
    # TODO: dividir texto por idioma e concatenação
    output = "output/audio.wav"
    tts.tts_to_file(text=text, file_path=output)
    return output
