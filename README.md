# Real-Time Cryptocurrency Data Pipeline with Redpanda

*A scalable streaming pipeline for cryptocurrency market data*

## 🚀 Features
- **Real-time price streaming** from CoinLore API
- **Moving average calculations** using Quix Streams
- **Redpanda** (Kafka-compatible) for high-throughput messaging
- **Dockerized** for easy deployment

## 🛠️ Prerequisites
1. **Docker** ([Install Guide](https://docs.docker.com/get-docker/))
2. **rpk CLI** (for topic inspection):
   ```bash
   # Linux/macOS installation
   curl -1sLf 'https://dl.redpanda.com/nzc4ZYQK3WRGd9sy/redpanda/cfg/setup/bash.rpm.sh' | sudo bash
   sudo apt-get install -y rpk

# Clone the repository
git clone https://github.com/yourusername/crypto-data-pipeline.git
cd crypto-data-pipeline

# Start the pipeline
docker-compose up -d

# Verify services
docker-compose ps
