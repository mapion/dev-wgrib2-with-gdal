FROM --platform=linux/x86_64 ochonjo/wgrib2-with-gdal:3.4.2
USER root

RUN apt-get update

RUN apt-get install -y python3-pip
# RUN pip install requests
