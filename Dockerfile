FROM python:3.6-alpine as base

RUN mkdir /pkgs

RUN apk add --update \
    gcc \
    musl-dev \
    linux-headers

COPY . /pkgs
WORKDIR /pkgs
RUN pip install wheel && pip wheel . --wheel-dir=/pkgs/wheels
RUN ls /pkgs/wheels


FROM python:3.6-alpine
COPY --from=base /pkgs /pkgs

WORKDIR /pkgs

RUN pip install --no-index --find-links=/pkgs/wheels pcapfilter

CMD [ "pcapfilter", "-d" ]
