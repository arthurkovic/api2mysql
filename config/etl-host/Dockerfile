FROM ubuntu:19.04
LABEL maintainer="Steven Ammon"

RUN apt-get update && apt-get dist-upgrade -q -y && apt-get -q -y install iputils-ping curl gnupg jq python3 python3-pip
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com --recv-keys 5072E1F5
RUN echo "deb http://repo.mysql.com/apt/ubuntu/ disco mysql-8.0\n \
deb http://repo.mysql.com/apt/ubuntu/ disco mysql-apt-config\n \
deb http://repo.mysql.com/apt/ubuntu/ disco mysql-tools" > /etc/apt/sources.list.d/mysql.list \
&& apt-get update && apt-get install -q -y mysql-client mysql-shell

ADD 1-Shell/load.sh /1-Shell/load.sh
ADD 2-Python /2-Python
ADD config/etl-host/loader.sql /config/etl-host/loader.sql

RUN chmod 777 /1-Shell/load.sh
RUN pip3 install -r /2-Python/requirements.txt

ENTRYPOINT ["tail", "-f", "/dev/null"]