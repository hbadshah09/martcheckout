# mart Checkout

This is a simple supermarket checkout system implemented in Python. It calculates the total price of items in a cart, applying discounts where applicable.

## Setup

### Prerequisites

- Python 3.x
- Docker (optional)

### Running Locally

1. Clone the repository.
2. Navigate to the project directory.
3. Run the application:

   ```bash
   python3 main.py

# run test 
python3 -m unittest test_checkout.py

# run locally
python3 main.py

 # Dockerization
To run the application using Docker

# Build the Docker image:

 
docker build -t checkout 

# Run the Docker container:

 
docker run --rm checkout

# Run Tests:

python3 -m unittest test_checkout.py