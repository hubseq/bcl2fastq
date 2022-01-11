# Use Python image base from Dockerhub
FROM python:3.7

# Metadata
LABEL container.base.image = "python:3.7"
LABEL software.name = "bcl2fastq"

# Install system packages and AWS CLI
RUN apt-get -y update && \
    apt-get -y install python3-pip
RUN pip install awscli boto3

WORKDIR /

# Install bcl2fastq
RUN mkdir -p /bcl2fastq
COPY misc/bcl2fastq2-v2-20-0.tar.gz /
RUN tar -xzvf /bcl2fastq2-v2-20-0.tar.gz -C /bcl2fastq
ENV PATH="/bcl2fastq/usr/local/bin/:$PATH"

# copy relevant scripts to root dir
RUN mkdir -p global_utils/src
COPY src/run_program.py /
COPY src/global_utils/src/module_utils.py /global_utils/src/
COPY src/global_utils/src/file_utils.py /global_utils/src/
COPY src/global_utils/src/global_keys.py /global_utils/src/
COPY src/global_utils/src/aws_s3_utils.py /global_utils/src/
ENV PATH="/usr/local/bin/:$PATH"

ENTRYPOINT ["python","/run_program.py"]                                           
