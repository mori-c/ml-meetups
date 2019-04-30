FROM alpine:3.7

RUN apk add --no-cache \
    openssh-client \
    git \
    mongodb \
    nodejs && \
    dos2unix && \
    mkdir -p /data/db /code

COPY ./entrypoint.sh /

RUN dos2unix /entrypoint.sh

CMD "./entrypoint.sh"
