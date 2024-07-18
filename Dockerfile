# You could use `gitpod/workspace-full` as well.
FROM gitpod/workspace-python

RUN cd /home/gitpod/.pyenv/plugins/python-build/../.. && git pull && cd -

RUN pyenv install 3.12.4 \
    && pyenv global 3.12.4

RUN sudo apt-get update && sudo apt-get install -y ffmpeg
RUN pip install poetry && poetry config virtualenvs.in-project true
COPY Makefile pyproject.toml poetry.lock ./
RUN make install
COPY . .
