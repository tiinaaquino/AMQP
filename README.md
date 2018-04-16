# AMQP

## Requirements

To run this code you need to install the `pika` package version 0.10.0 or later. To install it, run

    pip install pika==0.11.0

You may first need to run

    easy_install pip
    
## Code

There are two programs: 
    A sender (producer) that sends a single message.
    A receiver (consumer) that receives messages and prints them out.
    
## Usage

$ python consumer.py /n
$ python producer.py
