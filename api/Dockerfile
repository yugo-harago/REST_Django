#Same as Roster
FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN buildDeps='build-essential libpq-dev libffi-dev libheif-dev libde265-dev' && \
    apt-get update && apt-get install -y --no-install-recommends $buildDeps \
    # load_bank_csv
    make postgresql-client \
    # pdf2image
    poppler-utils \
    # libheif
    libheif1 \
    # wkhtmltopdf
    wkhtmltopdf \
    fonts-ipafont \
    fonts-noto-cjk \
    # i18n
    gettext \
    # libfaketime
    libfaketime \
    # graph_models
    graphviz \
    libgraphviz-dev \
    pkg-config \
    && \
    pip install poetry

COPY ./pyproject.toml ./poetry.lock ./
COPY ./scripts ./scripts
RUN poetry config virtualenvs.create false && poetry install

# libfaketime
RUN ln -s /usr/lib/`arch`-linux-gnu/faketime/libfaketime.so.1 /usr/lib && ldconfig
ENV LD_PRELOAD=libfaketime.so.1
ENV FAKETIME_TIMESTAMP_FILE=/tmp/.faketimerc

# create_test_data
ENV DEV_MODE=true

#CMD ["scripts/wait_for_it.sh", "db:5433", "--", "python", "-m", "debugpy", "--listen", "0.0.0.0:5679", "manage.py", "runserver", "0.0.0.0:8081"]
