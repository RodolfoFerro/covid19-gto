## Setup

Clone the repository.

```bash
git clone https://github.com/RodolfoFerro/covid19-gto.git
```

We need to install Docker. To install Docker on a Linux (tested on Ubuntu 18.04 LTS) machine, we need to run the following.

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install -y docker-ce
```

Now that we have Docker installed, we can proceed to create the container image:

```bash
docker build -t gto_covid19:latest .
```

> **TIP:**
> To see the Docker images in your computer, you can run:
> ```bash
> docker images
> ```
> If you want to see all image containers that are running:
> ```bash
> docker ps
> ```
> And to stop running containers:
> ```bash
> docker kill <CONTAINER ID>
> ```

Finally, we run the application inside the container.

```bash
docker run -d -p 5000:5000 -v $(pwd):/app gto_covid19:latest
```
