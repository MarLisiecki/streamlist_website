# Use the Python 3.11 Bullseye image as the base image
FROM python:3.11-bullseye

# Set the working directory inside the container
WORKDIR /root/private/streamlit_website

# Copy the current directory contents into the container
COPY . .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables (Optional)
ENV PYTHONPATH=.

# Run your command when the container starts
CMD ["sh", "-c", "streamlit run website/main_page.py"]