import streamlit as st
from image_gen import gen_images
from video_search import download_clip
from tts import synthesize
from subtitle import gen_subtitles
from editor import compose_video

st.title("🎬 Gerador de Vídeo IA")

uploads = st.file_uploader("1–5 imagens do personagem (opcional)", type=["png","jpg"], accept_multiple_files=True)
roteiro = st.text_area("Cole o roteiro aqui")
langs = st.multiselect("Idiomas (nar. + legendas)", ["pt","en","es"], default=["pt"])
modo = st.selectbox("Modo de criação", ["Imagens IA", "Vídeos gratuitos"])

if st.button("Gerar vídeo"):
    with st.spinner("Gerando vídeo..."):
        if modo == "Imagens IA":
            imgs = gen_images(uploads, roteiro)
        else:
            imgs = [download_clip(seg) for seg in roteiro.split("\n") if seg.strip()]
        audio = synthesize(roteiro, langs)
        subs = gen_subtitles(audio, langs)
        video_path = compose_video(imgs, audio, subs)
    st.success("Vídeo pronto!")
    st.video(video_path)
    st.download_button("📥 Baixar vídeo", open(video_path, "rb"), "video_final.mp4", "video/mp4")
