FROM python:3.10.12-bookworm

# Install using conda

# COPY pyproject.toml ./

# # Install Poetry
# RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 && \
#   cd /usr/local/bin && \
#   ln -s /opt/poetry/bin/poetry && \
#   poetry config virtualenvs.create false

# # Allow installing dev dependencies to run tests
# ARG INSTALL_DEV=false
# RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"
RUN pip install --upgrade pip
RUN pip install tmkit==0.0.4

RUN mkdir -p /workspace
WORKDIR /workspace

CMD ["/bin/bash"]
