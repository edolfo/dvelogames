# You could use `gitpod/workspace-full` as well.
FROM gitpod/workspace-python

RUN apt-get install -y ffmpeg
RUN pip install poetry && poetry config virtualenvs.in-project true
COPY Makefile pyproject.toml poetry.lock ./
RUN make install
COPY . .
