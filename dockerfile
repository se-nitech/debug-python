FROM python:slim

RUN apt -y update && apt -y install git

# Python tools
RUN pip install pytest coverage line_profiler

# only for cli (vscode extentions work for editor)
RUN pip install flake8 autopep8

WORKDIR /mnt
