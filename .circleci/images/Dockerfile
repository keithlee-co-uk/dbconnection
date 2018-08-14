# --------------------------------------------------------------------------
# This is a Dockerfile to build an Debian Stretch 9 Docker image for python3
# with pymssql and FreeTDS
#
# Use a command like:
#     docker build -t pymssql/pymssql .
# --------------------------------------------------------------------------

FROM  circleci/python:3.6-stretch-node
MAINTAINER  Keith Lee <code@keithlee.co.uk>

# Install apt packages
RUN apt-get update && apt-get install -y \
    freetds-bin \
    freetds-common \
    freetds-dev

RUN pip install Cython
# RUN pip install ipython
# RUN pip install SQLAlchemy
# RUN pip install pandas
# RUN pip install Alembic

RUN apt-get install -y python-pymssql
RUN pip install pymssql

CMD ["python"]
