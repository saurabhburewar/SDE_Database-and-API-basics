import requests
import json


def test_detect():
    url = 'http://127.0.0.1:5001/face_detect'

    files = {'file': open('images/img_03.jpg', 'rb')}

    resp = requests.post(url, files=files)
    print('face_detect response:\n', json.dumps(resp.json()))


if __name__ == '__main__':
    test_detect()
