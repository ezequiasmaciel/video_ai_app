import whisper

def gen_subtitles(audio_path, langs):
    """
    Gera legendas em pt/en/es usando Whisper.
    Retorna dict de paths de .srt.
    """
    model = whisper.load_model("base")
    results = model.transcribe(audio_path, language=langs[0])
    # TODO: adicionar suporte multilíngue completo
    srt_path = f"output/subs_{langs[0]}.srt"
    with open(srt_path, "w") as s:
        s.write(results["text"])
    return {langs[0]: srt_path}
