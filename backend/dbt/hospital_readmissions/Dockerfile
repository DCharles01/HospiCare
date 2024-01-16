# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /dbt
WORKDIR /dbt

# Install dbt and required dependencies
RUN pip install dbt

# Copy the dbt project directory into the container at /dbt
COPY . /dbt

# Set the entrypoint for dbt commands
ENTRYPOINT ["dbt"]

# install dbt dependencies
CMD ["dbt", "deps"]

# Default command is to display dbt help
CMD ["--help"]
