FROM sindriainc/python:1.1.5-3.8

ARG TAG_VERSION
ARG HOST_USER_UID
ARG TIMEZONE

WORKDIR /var/www/app

LABEL \
        name="aubergina" \
        image="registry.sindria.org/dorjecurreli/aubergina" \
        tag="${TAG_VERSION}" \
        vendor="sindria"

ENV DEBIAN_FRONTEND="noninteractive"
ENV TZ=${TIMEZONE}
ENV SINDRIA_USER="sindria"
ENV SINDRIA_USER_HOME="/home/sindria"

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install application
COPY ./ /var/www/app
RUN pip install -r requirements.txt && \
    rm -f /var/www/app/requirements.txt && \
    ln -s /var/www/app/app/main.py /var/www/app/bin/app && \
    ln -s /var/www/app/bin/app /usr/local/bin/app && \
    chmod -R 771 /var/www/app && \
    chown -R ${SINDRIA_USER}:${SINDRIA_USER} /var/www/app


CMD ["app"]