FROM python:3.8.5

WORKDIR /tmp

# fontのインスコ
RUN wget https://noto-website-2.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip && \
    unzip NotoSansCJKjp-hinted.zip && \
    mkdir -p /usr/share/fonts/truetype/noto && \
    cp *otf /usr/share/fonts/truetype/noto && \
    fc-cache -f -v

WORKDIR /code

ADD . .

RUN pip install pipenv && pipenv install --system

CMD ["python", "main.py"]
