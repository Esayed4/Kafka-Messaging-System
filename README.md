# Kafka Messaging System

This project demonstrates a basic implementation of Kafka producers and consumers. The producer sends messages to a Kafka topic, and the consumer reads messages from the Kafka topic. This can be useful for understanding the fundamentals of Apache Kafka and message-driven architectures.

## Files

- `create_topic_practice.py`: Script for creating a Kafka topic named `practice` with 3 partitions.
- `create_producer.py`: Script for creating a Kafka producer that sends messages to the `practice` topic.
- `create_consumer.py`: Script for creating a Kafka consumer that reads messages from the `practice` topic.
- `create_concumer1.py`: Similar to `create_consumer.py`, but processes keys and values differently.

## Requirements

- Python 3.x
- Apache Kafka
- `kafka-python` library

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/kafka-messaging-system.git
    cd kafka-messaging-system
    ```

2. **Install dependencies**:
    ```sh
    pip install kafka-python
    ```

3. **Setup Kafka**:
    - Ensure you have Kafka installed and running on your machine.
    - By default, the scripts use `localhost:9092` as the Kafka bootstrap server and `practice` as the topic name. You can change these settings in the scripts if needed.

## Usage

### Running the Producer

1. Open a terminal and navigate to the project directory.
2. Run the producer script:
    ```sh
    python create_producer.py
    ```
3. Enter messages in the format `key:value`. For example:
    ```
    1:Hello Kafka
    ```
   Enter `11` as the key to send multiple close messages.

### Running the Consumer

1. Open another terminal and navigate to the project directory.
2. Run the consumer script:
    ```sh
    python create_consumer.py
    ```
3. The consumer will start reading messages from the Kafka topic and print them to the console.

### Running the Alternative Consumer

1. Open another terminal and navigate to the project directory.
2. Run the alternative consumer script:
    ```sh
    python create_concumer1.py
    ```
3. This consumer behaves similarly but decodes keys and values differently and prints all consumed messages.

## Additional Information

- **Kafka Producer**: Produces messages to the Kafka topic. It allows sending a special message when the key `11` is entered to trigger multiple close messages.
- **Kafka Consumer**: Consumes messages from the Kafka topic. It prints the messages and stops if it receives a message with the key `11`.
- **Alternative Kafka Consumer**: Similar to the standard consumer but with different key/value processing.

## Contributing

If you wish to contribute to this project, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
