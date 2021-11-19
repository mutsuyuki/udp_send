IMAGE_REPOSITORY=my_udp_send
IMAGE_TAG=latest
IMAGE_FULLNAME=${IMAGE_REPOSITORY}:${IMAGE_TAG}

# docker build if changed.
docker build -t ${IMAGE_FULLNAME} .

# allow display connection
xhost +

# run container 
docker run \
--interactive \
--tty \
--rm \
--mount=type=bind,src="$(pwd)",dst=/root/share \
--gpus=all \
--env=DISPLAY=${DISPLAY} \
--net=host \
--name=${IMAGE_REPOSITORY}_${IMAGE_TAG}_$(date "+%Y_%m%d_%H%M%S") \
${IMAGE_FULLNAME} bash
