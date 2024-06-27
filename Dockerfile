FROM python:3.11-bullseye

WORKDIR /root/private/streamlit_website

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=.

CMD ["sh", "-c", "streamlit run website/main_page.py"]