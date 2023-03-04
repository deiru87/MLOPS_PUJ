
# MLOPS_PUJ
Repo with all related to Advances Machine learning Class in PUJ

below are all the details of the projects and activities related to the class on advanced topics of AI.

# Simple Inference

Project with simple example of docker and FastApi.

Clone the project

```
git clone https://github.com/deiru87/MLOPS_PUJ.git
```

## Build docker images

you have to be located in the directory of the project, so execute.

```
cd MLOPS_PUJ/simple_inference
```
after, execute.

```
docker build -f .\infra\Dockerfile -t simple_model .
```

## Create container from docker image built

execute

```
docker run --name simple_model -p  8091:80 simple_model
```
