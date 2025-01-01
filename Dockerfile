# Use an official Ubuntu as a base image
FROM ubuntu:20.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    git \
    cmake \
    make \
    build-essential \
    mediainfo \
    ffmpeg \
    mkvtoolnix \
    && rm -rf /var/lib/apt/lists/*

# Clone the Bento4 repository
RUN git clone https://github.com/axiomatic-systems/Bento4.git /opt/Bento4

# Build Bento4
WORKDIR /opt/Bento4
RUN mkdir cmakebuild && cd cmakebuild && \
    cmake -DCMAKE_BUILD_TYPE=Release .. && \
    make && \
    make install

# Set environment variables if needed
ENV PATH="/opt/Bento4/bin:${PATH}"

# Set the default command (optional)
CMD ["bash"]
