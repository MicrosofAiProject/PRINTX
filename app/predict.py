# The steps implemented in the object detection sample code: 
# 1. for an image of width and height being (w, h) pixels, resize image to (w', h'), where w/h = w'/h' and w' x h' = 262144
# 2. resize network input size to (w', h')
# 3. pass the image to network and do inference
# (4. if inference speed is too slow for you, try to make w' x h' smaller, which is defined with DEFAULT_INPUT_SIZE (in object_detection.py or ObjectDetection.cs))
import datetime
import logging
import pathlib
from urllib.request import urlopen
import numpy as np
from PIL import Image

try:
    import tflite_runtime.interpreter as tflite
except ImportError:
    import tensorflow.lite as tflite

from object_detection import ObjectDetection

MODEL_FILENAME = 'model.tflite'
LABELS_FILENAME = 'labels.txt'

od_model = None
logger = logging.getLogger(__name__)


class TFObjectDetection(ObjectDetection):
    """Object Detection class for TensorFlow"""
    def __init__(self, model_filename, labels):
        super().__init__(labels)
        self._interpreter = tflite.Interpreter(model_path=model_filename)
        self._interpreter.allocate_tensors()

        input_details = self._interpreter.get_input_details()
        output_details = self._interpreter.get_output_details()
        assert len(input_details) == 1
        assert len(output_details) == 1
        self._input_index = input_details[0]['index']
        self._output_index = output_details[0]['index']
        self._input_shape = (int(input_details[0]['shape'][1]), int(input_details[0]['shape'][2]))

    def predict(self, image):
        input_array = np.array(image, dtype=np.float32)[np.newaxis, :, :, (2, 1, 0)]  # RGB -> BGR

        new_input_shape = input_array.shape[1:3]
        if new_input_shape != self._input_shape:
            self._input_shape = new_input_shape
            self._interpreter.resize_tensor_input(self._input_index, [1, *new_input_shape, 3])
            self._interpreter.allocate_tensors()

        self._interpreter.set_tensor(self._input_index, input_array)
        self._interpreter.invoke()

        outputs = self._interpreter.get_tensor(self._output_index)
        return outputs[0]


def log_msg(msg):
    print("{}: {}".format(datetime.now(), msg))


def initialize():
    labels = [s.strip() for s in pathlib.Path(LABELS_FILENAME).read_text().splitlines()]
    logger.info(f"Loaded {len(labels)} labels.")

    global od_model
    od_model = TFObjectDetection(MODEL_FILENAME, labels)


def predict_url(image_url):
    logger.info(f"Predicting from url: {image_url}")
    with urlopen(image_url) as image_binary:
        image = Image.open(image_binary)
        return predict_image(image)


def predict_image(image):
    logger.info(f"Predicting from image: size={image.size}")

    predictions = od_model.predict_image(image)

    response = {
        'id': '',
        'project': '',
        'iteration': '',
        'created': datetime.datetime.utcnow().isoformat(),
        'predictions': predictions}

    logger.info(f"Response: {response}")
    return response
