FROM python:3.9

# Set a proper working directory
WORKDIR /app

# Copy all files into the container
COPY . /app

# Install dependencies (make sure you have requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit default port
EXPOSE 8501

# Run your Streamlit app
CMD ["streamlit", "run", "matchpredictor.py", "--server.port=8501", "--server.address=0.0.0.0"]
