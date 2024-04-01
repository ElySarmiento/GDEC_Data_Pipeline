# EC2 Setup for Running Airflow via Astro CLI

## Installing dependencies

To run Airflow via Astro CLI, the following packages are required:

- Python
- Docker
- Astro CLI

Follow these steps to install the dependencies:

1. Update package list and install latest versions:
```bash
sudo apt update
sudo apt upgrade
```
2. Check if Python is already installed:
```shell
python3 --version
```
![[Pasted image 20240331164532.png]]
3. Install Docker software updates:
```shell
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
```
4. Add the Docker Repository GPG Key:
```shell
curl -fsSL [https://download.docker.com/linux/ubuntu/gpg](https://download.docker.com/linux/ubuntu/gpg) | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```
5. Add the Docker APT Repository:
```shell
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] [https://download.docker.com/linux/ubuntu](https://download.docker.com/linux/ubuntu) $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
6. Update packages again:
```shell
sudo apt update
```
7. Install Docker:
```shell
sudo apt install -y docker-ce docker-ce-cli [containerd.io](http://containerd.io/)
```
8. Start the Docker service and enable it to start automatically on boot:
```shell
sudo systemctl start docker
sudo systemctl enable docker
```
9. Verify that Docker is installed:
```shell
sudo docker --version
```
10. Install latest version of Astro CLI directly to PATH:
```shell
curl -sSL install.astronomer.io | sudo bash -s
```
11. Check Astro CLI version:
```shell
sudo astro version
```

## Running DAGs on Airflow

1. Clone the repo:
```shell
git clone https://github.com/Great-Deals-E-commerce-Corp/dbt_snowflake.git
```
2. Go to `develop` branch:
```shell
git checkout develop
```
3. Run Airflow via Astro CLI:
```shell
sudo astro dev start
```

