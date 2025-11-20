# 1. Use an official lightweight Python image
FROM python:3.9-slim

# 2. Set the working directory inside the container to /app
WORKDIR /app

# 3. Copy all files from your computer to the container
COPY . .

# 4. Install the required libraries
# We use --no-cache-dir to keep the image small
RUN pip install --no-cache-dir -r requirements.txt

# 5. Expose the port Streamlit runs on
EXPOSE 8501

# 6. Command to run the app when the container starts
CMD ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]