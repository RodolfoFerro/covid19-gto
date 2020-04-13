# [WIP] COVID-19 cases in Guanajuato

[![](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/covid19-gto/images/0)](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/covid19-gto/links/0)[![](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/covid19-gto/images/1)](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/covid19-gto/links/1)[![](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/covid19-gto/images/2)](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/covid19-gto/links/2)[![](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/covid19-gto/images/3)](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/covid19-gto/links/3)[![](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/covid19-gto/images/4)](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/covid19-gto/links/4)[![](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/covid19-gto/images/5)](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/covid19-gto/links/5)[![](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/covid19-gto/images/6)](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/covid19-gto/links/6)[![](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/covid19-gto/images/7)](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/covid19-gto/links/7)

This project is a WIP (_Work In Progress_) about serving simple and clean data about COVID-19 reported cases from the official source (https://coronavirus.guanajuato.gob.mx) in Guanajuato.

### Features:

- **All information is served simple and clean**.
- **Total cases** served as they appear in the offical source.
- **Hoverable map** with traffic light symbology per city (red=confirmed cases, yellow=suspicious case, green=no cases).
- **Embedded table** containing the cases per city.

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

## Roadmap

- [ ] Update about section
- [ ] Add a cron job to scrape data
- [ ] Create a webhook for auto-deployment in server
- [ ] Propose a way to extend scraped info (in order to create a more complete dashboard)

## Contributing

1. Create an issue and mention any project admin ([@RodolfoFerro](https://github.com/RodolfoFerro) or [@scratchmex](https://github.com/scratchmex)).
2. Fork the repo and clone your fork.
3. Create a new branch and add your changes.
4. Open a PR containing a detailed descrition about your changes and mention the associated issue.