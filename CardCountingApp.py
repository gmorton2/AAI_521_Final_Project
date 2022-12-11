import streamlit as st
import logging
# import queue
import Blackjack_model as blackjack

# from streamlit_webrtc import (
#     RTCConfiguration,
#     WebRtcMode,
#     WebRtcStreamerContext,
#     webrtc_streamer,
# )

target_dict={'10C': 0,
 '10D': 1,
 '10H': 2,
 '10S': 3,
 '2C': 4,
 '2D': 5,
 '2H': 6,
 '2S': 7,
 '3C': 8,
 '3D': 9,
 '3H': 10,
 '3S': 11,
 '4C': 12,
 '4D': 13,
 '4H': 14,
 '4S': 15,
 '5C': 16,
 '5D': 17,
 '5H': 18,
 '5S': 19,
 '6C': 20,
 '6D': 21,
 '6H': 22,
 '6S': 23,
 '7C': 24,
 '7D': 25,
 '7H': 26,
 '7S': 27,
 '8C': 28,
 '8D': 29,
 '8H': 30,
 '8S': 31,
 '9C': 32,
 '9D': 33,
 '9H': 34,
 '9S': 35,
 'AC': 36,
 'AD': 37,
 'AH': 38,
 'AS': 39,
 'JC': 40,
 'JD': 41,
 'JH': 42,
 'JS': 43,
 'KC': 44,
 'KD': 45,
 'KH': 46,
 'KS': 47,
 'QC': 48,
 'QD': 49,
 'QH': 50,
 'QS': 51}

logger = logging.getLogger(__name__)

def main():
    header_section = st.container()
    project_description = st.container()
    dataset_description = st.container()
    model_training = st.container()
    model_result = st.container()
    demo_section = st.container()

    # header section
    with header_section:
         st.title("Blackjack Card Counting with Computer Vision")

    # project description section
    with project_description:
        st.subheader("Project Description")
        st.write("This application is meant to show that computer vision ",
            "and AI can be use to aid Blackjack players win.",
            "The application uses a model trained with a Convolutional Neural Network ",
            "to keep a running count of the cards seen and suggest the next best moved.")

    # dataset description section
    with dataset_description:
        st.subheader("Dataset")
        st.write("When utilizing deep learning model, ",
        "it is necessary to have an adequate data to train the model.",
        "That is the reason this project uses the dataset from, "
        "[The Complete Playing Cards](https://www.kaggle.com/datasets/jaypradipshah/the-complete-playing-card-dataset).",
        "This Kaggle repository was choosen because is provides a large dataset ",
        "that can be used with some image augmentation techniques ",
        "to generalize a model with high accuracy.",
        "The dataset contains over 2000 images where it has 50 images of each card.",
        "In addition the dataset has the annotations of the type of cards in three forms such ",
        "as YOLO, COCO, and Pascal-VOC.",
        "This different annotation types are useful when training the model.")

    # model training section
    with model_training:
        st.subheader("Model Training")
        st.write("The process of training the model starts with data preprocessing. The preprocessing steps ",
        "difference depending on the training method used. For this project different techniques were ",
        "considered for model training, such as YOLOv4. However, in the end the method that gave the ",
        "best result was the Deep Convolutional Neural Network. The model trained after 15 epochs was ",
        "of 98% accuracy and going higher in epochs didn't improve the accuracy.")

    # model results section
    with model_result:
        st.subheader("Model Result")

    # demo section
    with demo_section:
        st.subheader("Demo")
        st.write("Press the button belows to see a simulated game.")
        new_game = st.button("New Game")

        if new_game:
            blackjack.black_jack(target_dict)

# # live demo
# def app_sendonly_video():
#     """A sample to use WebRTC in sendonly mode to transfer frames
#     from the browser to the server and to render frames via `st.image`."""
#     webrtc_ctx = webrtc_streamer(
#         key="video-sendonly",
#         mode=WebRtcMode.SENDONLY,
#         rtc_configuration=RTC_CONFIGURATION,
#         media_stream_constraints={"video": True},
#     )

#     image_place = st.empty()

#     while True:
#         if webrtc_ctx.video_receiver:
#             try:
#                 video_frame = webrtc_ctx.video_receiver.get_frame(timeout=1)
#             except queue.Empty:
#                 logger.warning("Queue is empty. Abort.")
#                 break

#             img_rgb = video_frame.to_ndarray(format="rgb24")
#             image_place.image(img_rgb)
#         else:
#             logger.warning("AudioReciver is not set. Abort.")
#             break

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