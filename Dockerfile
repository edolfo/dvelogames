# You could use `gitpod/workspace-full` as well.
FROM gitpod/workspace-python

RUN pyenv install 3.10 \
    && pyenv global 3.10

RUN sudo apt-get update && sudo apt-get install -y ffmpeg
RUN pip install poetry && poetry config virtualenvs.in-project true
COPY Makefile pyproject.toml poetry.lock ./
RUN make install
COPY . .
