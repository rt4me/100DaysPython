FROM python:3.11-slim

RUN apt-get update && apt-get install -y tk libgl1-mesa-glx

# Install git using the package manager (apt-get)
# Install system-level dependencies for Tkinter and graphics
# tk-dev, tcl-dev, and python3-tk are crucial for tkinter's C bindings
# libgl1-mesa-glx is for general OpenGL/graphics support, often needed for GUI
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    tk-dev \
    tcl-dev \
    python3-tk \
    libgl1-mesa-glx \
    # Clean up apt lists to reduce image size
    && rm -rf /var/lib/apt/lists/*   

# Install git using the package manager
RUN apt-get update && apt-get install -y git \
    # Clean up apt lists again (or combine with the first cleanup if convenient)
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["bash"]