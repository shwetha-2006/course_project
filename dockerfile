FROM python:3.13
WORKDIR /course_project
COPY . .
RUN pip install --no-cache-dir pytest
# Run tests at build time (CI)
RUN pytest
# FIXED entrypoint (never replaced)
ENTRYPOINT ["python", "student.py"]