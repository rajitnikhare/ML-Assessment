FROM python:3.7

# install dependencies
RUN pip3 install fastapi uvicorn joblib scikit-learn 

# Copy the code to the container
COPY ./app /app

# Open the required port
EXPOSE 8000

# Run the Uvicorn app using the command
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]



