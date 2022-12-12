import streamlit as st
import logging
from PIL import Image
import Blackjack_model as blackjack

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
        st.write("The model is promising because it has a 98% accuracy. The images below show ",
        "the learning curves i.e. the accuracy and loss curves of the model over the 15 epochs.",
        "")
        image = Image.open('LearningCurves.png')
        st.image(image, caption='Learning Curves')

        st.write("Because of these values wee believe that our model can be use is multiple ",
        "scenarios one of this is this web application, but it can be embedded in other ",
        "devices.")

    # demo section
    with demo_section:
        st.subheader("Demo")
        st.write("Press the button belows to see a simulated game.")
        new_game = st.button("New Game")

        if new_game:
            blackjack.black_jack(blackjack.target_dict)

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