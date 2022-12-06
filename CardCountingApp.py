import streamlit as st
import logging
import queue
from streamlit_webrtc import (
    RTCConfiguration,
    WebRtcMode,
    WebRtcStreamerContext,
    webrtc_streamer,
)

logger = logging.getLogger(__name__)

def main():

    st.title("Blackjack Card Counting with Computer Vision")

    # project description section
    with st.container():
        st.text("This application is meant to show that computer vision " +
            "and AI can be use to aid Blackjack players win.")
        st.text("The application uses a model trained with a Convolutional Neural Network " +
            "to keep a running count of the cards seen and suggest the next best moved.")

    # dataset description section
    with st.container():
        st.text("The dataset comes from")
        st.markdown("[The Complete Playing Cards](https://kaggle.com)")

# model training section

# model results section

# live demo
def app_sendonly_video():
    """A sample to use WebRTC in sendonly mode to transfer frames
    from the browser to the server and to render frames via `st.image`."""
    webrtc_ctx = webrtc_streamer(
        key="video-sendonly",
        mode=WebRtcMode.SENDONLY,
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={"video": True},
    )

    image_place = st.empty()

    while True:
        if webrtc_ctx.video_receiver:
            try:
                video_frame = webrtc_ctx.video_receiver.get_frame(timeout=1)
            except queue.Empty:
                logger.warning("Queue is empty. Abort.")
                break

            img_rgb = video_frame.to_ndarray(format="rgb24")
            image_place.image(img_rgb)
        else:
            logger.warning("AudioReciver is not set. Abort.")
            break

if __name__ == "__main__":
    import os

    DEBUG = os.environ.get("DEBUG", "false").lower() not in ["false", "no", "0"]

    logging.basicConfig(
        format="[%(asctime)s] %(levelname)7s from %(name)s in %(pathname)s:%(lineno)d: "
        "%(message)s",
        force=True,
    )

    logger.setLevel(level=logging.DEBUG if DEBUG else logging.INFO)

    st_webrtc_logger = logging.getLogger("streamlit_webrtc")
    st_webrtc_logger.setLevel(logging.DEBUG)

    main()