import os

os.makedirs(
    "datasets/computer_vision/gtsrb",
    exist_ok=True
)

os.system(
    "kaggle datasets download "
    "-d meowmeowmeowmeowmeow/gtsrb-german-traffic-sign "
    "--unzip "
    "-p datasets/computer_vision/gtsrb"
)