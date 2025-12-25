# 1. Start with a lightweight Python Linux image
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the requirements file into the container
COPY requirements.txt .

# 4. Install dependencies
# --no-cache-dir keeps the image small
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your code into the container
COPY . .

# 6. Expose the port Streamlit uses
EXPOSE 8501

# 7. The command to run your app when the container starts
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]