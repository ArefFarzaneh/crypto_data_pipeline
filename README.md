# 📈 Real-Time Cryptocurrency Data Pipeline

![Pipeline Architecture](https://i.imgur.com/JQ8w0Rn.png)  
*A Dockerized streaming pipeline for processing live crypto prices with Redpanda (Kafka-compatible)*

## 🌟 Key Features
- **Real-time price streaming** from CoinLore API
- **On-the-fly metrics** (moving averages, volatility)
- **Fault-tolerant design** with auto-recovery
- **Ready for extensions** (alerts, dashboards, ML)

## 🚀 Quick Start

### Prerequisites
- Docker ([Install Guide](https://docs.docker.com/get-docker/))
- rpk CLI (*optional for local inspection*):
  ```bash
  curl -1sLf 'https://dl.redpanda.com/nzc4ZYQK3WRGd9sy/redpanda/cfg/setup/bash.rpm.sh' | sudo bash && sudo apt-get install -y rpk
  # Clone the repository
git clone https://github.com/yourusername/crypto-data-pipeline.git
cd crypto-data-pipeline

# Start all services (Redpanda + Producer + Consumer)
docker-compose up -d

# Verify all containers are running
docker-compose ps
