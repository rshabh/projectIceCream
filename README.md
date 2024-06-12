# Ice Cream Parlor Application

Welcome to the Ice Cream Parlor application repository!

## Getting Started

### Prerequisites

- Docker: [Install Docker](https://docs.docker.com/get-docker/)

### Building and Running the Application with Docker

1. Clone this repository:

   bash
   
   git clone https://github.com/rshabh/projectIceCream.git


2.Build the Docker image:

bash

docker build -t ice-cream-manage .

3.Run the Docker container:

docker run -p 8501:8501 ice-cream-manage

This command will run the Docker container based on the previously built image. It will expose port 8501, which is the default port used by the Streamlit application.



Open your web browser and navigate to http://localhost:8501 to access the Ice Cream Parlor application.
