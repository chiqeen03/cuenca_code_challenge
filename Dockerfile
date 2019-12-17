FROM python:3
ADD src/constants.py /
ADD src/board.py /
ADD src/main.py /
CMD [ "python", "./src/main.py" ]