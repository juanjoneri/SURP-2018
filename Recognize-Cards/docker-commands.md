```
## basics
docker create REPOSITORY_NAME:TAG
docker images
docker ps -l

## run interactive terminal
docker run -it IMAGE_ID bash
docker stop CONTAINER_ID

## save a stopped container
docker commit CONTAINTER_ID juanjoner/NAME:TAG

docker rmi -f IMAGE_ID

```
