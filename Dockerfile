FROM alpine:3
RUN mkdir -p /usr/local/debug
WORKDIR /usr/local/debug
RUN apk add --update python3

COPY . .
