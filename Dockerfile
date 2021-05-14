FROM cycleplatform/debug:no-volume
RUN mkdir -p /usr/local/debug
WORKDIR /usr/local/debug
RUN apk add --update python3

COPY . .
RUN mv /traps.sh ./
CMD ["/bin/bash", "./traps.sh"]