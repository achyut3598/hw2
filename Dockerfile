FROM python:3.6-alpine
COPY hw2.py /
WORKDIR /
RUN mkdir home; exit 0
RUN mkdir -p home/data
RUN mkdir -p home/output
COPY /home/data/file1.txt /home/data
COPY /home/data/file2.txt /home/data
COPY /home/data/file3.txt /home/data
CMD [ "python", "-u", "hw2.py" ]