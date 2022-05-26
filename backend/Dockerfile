FROM python:3.9
RUN apt-get update && apt-get install -y \
  sudo \
  vim \
  git \
  make \
  curl \
  xz-utils \
  file \
  g++ \
  unzip

WORKDIR /opt

RUN pip install \
  numpy \
  scikit-learn \
  fastapi \
  tensorflow \
  transformers["ja"] \
  uvicorn[standard]
