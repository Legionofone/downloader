FROM python:3.9

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN pip install --no-cache-dir --upgrade fastapi[standard]

COPY ./main.py /code/app/

RUN adduser \
    --disabled-password \
    --gecos "" \
    --ingroup "users" \
    --no-create-home \
    --uid "99" \
    appuser

RUN chown -R 99:100 /code

USER 99:100

CMD ["fastapi", "run", "app/main.py", "--port", "80", "--proxy-headers"]