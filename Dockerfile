FROM python:3.10-slim
ARG RUN_ID
ENV MODEL_ID=$RUN_ID

WORKDIR /app

RUN echo "Downloading model for Run ID: ${MODEL_ID}" > model_status.txt

CMD ["cat", "model_status.txt"]
