FROM ubuntu:19.04
LABEL maintainer="Steven Ammon"

RUN apt-get update && apt-get dist-upgrade -q -y && apt-get -q -y install iputils-ping curl gnupg jq
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com --recv-keys 5072E1F5
RUN echo "deb http://repo.mysql.com/apt/ubuntu/ disco mysql-8.0\n \
deb http://repo.mysql.com/apt/ubuntu/ disco mysql-apt-config\n \
deb http://repo.mysql.com/apt/ubuntu/ disco mysql-tools" > /etc/apt/sources.list.d/mysql.list \
&& apt-get update && apt-get install -q -y mysql-client mysql-shell
ADD 1-Shell/load.sh /load.sh
ADD config/etl-host/loader.sql loader.sql
RUN chmod 777 load.sh
ENTRYPOINT ["tail", "-f", "/dev/null"]